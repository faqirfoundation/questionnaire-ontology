#!/usr/bin/env python3
"""pdfToQO.py — read a table-based PDF questionnaire and write qo: TTL files.

Expects a folder holding one PDF whose questions sit in ruled tables. Each
black-bordered frame is a section: a header row carrying the answer scale,
followed by one question per row.

    ┌─────────────────────────────────────────────────────┐
    │        │        │ Very poor │ Poor │ ... │ Very good │   <- header row
    ├─────────────────────────────────────────────────────┤
    │ 1      │ (F1.4) │ How would you rate your ...       │   <- question row
    │ 2      │ (F2.1) │ How satisfied are you with ...    │
    └─────────────────────────────────────────────────────┘

A question row that continues on the next page is merged back into the
question above it. Questions appearing before any header row end up in one
implicit section with an empty scale.

Writes beside the PDF, one file per question plus one for the questionnaire:

    Question-<NAME>_01.ttl ... Questionnaire-<NAME>.ttl

Usage:
    python3 pdfToQO.py <pdf-or-folder> [--name NAME]

--name sets the questionnaire name used in the URIs, the questionTag and the
file names; it defaults to WHOQOL_BREF. Underscores become hyphens in the
human-readable label, so --name EQ_5D_5L gives questionnaire_EQ_5D_5L in the
URIs and "EQ-5D-5L" as the label.

A folder holding several PDFs is ambiguous: the alphabetically first one is
read and the rest are logged as skipped. Pass the PDF itself to choose.

Still hard-coded: the BASE namespace (https://pods.faqir.org/) and the
prov:wasAttributedTo attribution (https://www.who.int).
"""

import argparse
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import pdfplumber
from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, XSD
from rdflib.term import Node

# Shared helpers live one folder up.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logging_setup import configure_logging

QO = Namespace("https://ns.faqir.org/q-o#")
FHIR = Namespace("https://www.hl7.org/fhir/")
PROV = Namespace("http://www.w3.org/ns/prov#")
BASE = "https://pods.faqir.org/"

# Questionnaire name used in the URIs and file names; override with --name.
DEFAULT_NAME = "WHOQOL_BREF"

# Minimum scale cells for a header row; scales vary in length (3, 5, 7, ...).
MIN_SCALE_CELLS = 2

logger = logging.getLogger(__name__)


def clean(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def scale_labels(row: list) -> list[str]:
    """Return the non-empty scale-label cells of a row (columns 2 onward)."""
    return [clean(cell) for cell in row[2:] if clean(cell)]


def is_header_row(row: list) -> bool:
    """A frame's header row has empty number/label cells and >= 2 scale cells."""
    if len(row) < 4:
        return False
    num_cell, label_cell = row[0], row[1]
    if clean(num_cell) or clean(label_cell):
        return False
    return len(scale_labels(row)) >= MIN_SCALE_CELLS


def is_question_row(row: list) -> bool:
    """A question row's first cell starts with the item number, e.g. '3\\n(F1.4)'."""
    return bool(re.match(r"^\d+", clean(row[0])))


def parse_number_and_code(num_cell: str | None) -> tuple[int | None, str | None]:
    text = clean(num_cell)
    match = re.match(r"^(\d+)\s*(?:\((.*?)\))?$", text)
    if not match:
        return None, None
    return int(match.group(1)), match.group(2)


def parse_continuation_code(num_cell: str | None) -> str | None:
    text = clean(num_cell)
    match = re.match(r"^\((.*?)\)$", text)
    return match.group(1) if match else None


def new_section(scale: list[str]) -> dict:
    return {"scale": scale, "questions": []}


def display_name(name: str) -> str:
    """The human-readable form of the questionnaire name (WHOQOL_BREF -> WHOQOL-BREF)."""
    return name.replace("_", "-")


def find_pdf(folder: Path) -> Path:
    """The PDF to read from a folder: the first one in alphabetical order.

    One run produces one questionnaire, so several PDFs in a folder are
    ambiguous. The choice and the alternatives are logged; pass the PDF itself
    to pick another one.
    """
    pdfs = [p for p in sorted(folder.iterdir()) if p.suffix.lower() == ".pdf"]
    if not pdfs:
        raise FileNotFoundError(f"No PDF found in {folder}")
    if len(pdfs) > 1:
        logger.warning("%d PDFs in %s; reading the alphabetically first one: %s",
                       len(pdfs), folder, pdfs[0].name)
        logger.warning("not read: %s", ", ".join(p.name for p in pdfs[1:]))
        logger.warning("pass a PDF path instead of the folder to choose another")
    return pdfs[0]


def resolve_pdf(target: Path) -> Path:
    """Accept either the PDF itself or the folder holding it."""
    return target if target.is_file() else find_pdf(target)


def extract_frames(pdf_path: Path) -> list[dict]:
    """Read every ruled table in the PDF and group questions per answer-scale frame.

    Each frame is a black-bordered box: a header row with the scale labels
    (e.g. 'Very poor' .. 'Very good') followed by one or more question rows.
    A box that is split across a page break continues without a header row,
    so its first row is merged into the previous question.

    Sections are optional. When a question appears before any header row -- a
    questionnaire that simply has no scale frames -- it is collected in an
    implicit section with an empty scale instead of crashing.
    """
    with pdfplumber.open(pdf_path) as pdf:
        raw_tables = [t.extract() for page in pdf.pages for t in page.find_tables()]

    sections = []
    current_section = None
    current_question = None

    for rows in raw_tables:
        if not rows:
            continue

        if is_header_row(rows[0]):
            current_section = new_section(scale_labels(rows[0]))
            sections.append(current_section)
            data_rows = rows[1:]
        else:
            data_rows = rows

        for row in data_rows:
            if is_question_row(row):
                if current_section is None:
                    # No header seen yet -> questionnaire without sections.
                    current_section = new_section(scale=[])
                    sections.append(current_section)
                number, code = parse_number_and_code(row[0])
                current_question = {"number": number, "code": code, "label": clean(row[1])}
                current_section["questions"].append(current_question)
            elif current_question is not None:
                code = parse_continuation_code(row[0])
                if code and not current_question["code"]:
                    current_question["code"] = code
                extra_label = clean(row[1])
                if extra_label:
                    current_question["label"] = clean(f"{current_question['label']} {extra_label}")

    return [s for s in sections if s["questions"]]


def question_type(scale: list[str]) -> Node:
    """Derive the FHIR item type: a scale means a choice, otherwise free text."""
    return FHIR.choice if scale else FHIR.string


def build_question_graph(number: int, label: str, scale: list[str],
                         name: str = DEFAULT_NAME) -> tuple[Graph, URIRef]:
    g = Graph()
    g.bind("qo", QO)
    g.bind("fhir", FHIR)
    g.bind("prov", PROV)

    q_uri = URIRef(f"{BASE}question_{name}_{number:02d}")
    g.add((q_uri, RDF.type, QO.Question))
    g.add((q_uri, PROV.wasAttributedTo, URIRef("https://www.who.int")))
    g.add((q_uri, QO.questionType, question_type(scale)))

    for idx, display in enumerate(scale, start=1):
        vc = BNode()
        g.add((vc, RDF.type, QO.ValueCoding))
        g.add((vc, QO.code, Literal(str(idx))))
        g.add((vc, QO.display, Literal(display)))
        g.add((q_uri, QO.questionCodingParams, vc))

    g.add((q_uri, QO.questionLabel, Literal(label)))
    g.add((q_uri, QO.questionRequired, Literal(True)))
    g.add((q_uri, QO.questionTag, Literal(f"q_{name}_{number:02d}")))

    return g, q_uri


def add_ordered_question(g: Graph, parent_uri: Node, link: Node,
                         number: int, order: int, name: str = DEFAULT_NAME) -> None:
    oq_uri = URIRef(f"{BASE}orderedquestion_{name}_{number:02d}")
    q_uri = URIRef(f"{BASE}question_{name}_{number:02d}")
    g.add((parent_uri, link, oq_uri))
    g.add((oq_uri, RDF.type, QO.OrderedQuestion))
    g.add((oq_uri, QO.orderedQuestionHasQuestion, q_uri))
    g.add((oq_uri, QO.questionOrder, Literal(order)))


def build_questionnaire_graph(sections: list[dict], name: str = DEFAULT_NAME) -> Graph:
    g = Graph()
    g.bind("qo", QO)
    g.bind("fhir", FHIR)
    g.bind("xsd", XSD)

    quest_uri = URIRef(f"{BASE}questionnaire_{name}")
    g.add((quest_uri, RDF.type, QO.Questionnaire))
    g.add((quest_uri, QO.questionnaireLabel, Literal(display_name(name))))
    g.add((quest_uri, QO.questionnaireVersion, Literal("1.0.0")))
    g.add((quest_uri, QO.questionnaireStatus, FHIR["resource-status-active"]))
    g.add((
        quest_uri,
        QO.questionnaireLastUpdated,
        Literal(datetime.now(timezone.utc).isoformat(), datatype=XSD.dateTime),
    ))

    if len(sections) <= 1:
        # No real sectioning: attach the questions directly to the questionnaire.
        questions = sections[0]["questions"] if sections else []
        for order, question in enumerate(questions, start=1):
            add_ordered_question(
                g, quest_uri, QO.questionnaireHasOrderedQuestion, question["number"], order
            )
        return g

    for sec_idx, section in enumerate(sections, start=1):
        osec_uri = URIRef(f"{BASE}orderedsection_{name}_{sec_idx:02d}")
        sec_uri = URIRef(f"{BASE}section_{name}_{sec_idx:02d}")

        g.add((quest_uri, QO.questionnaireHasOrderedSection, osec_uri))
        g.add((osec_uri, RDF.type, QO.OrderedSection))
        g.add((osec_uri, QO.orderedSectionHasSection, sec_uri))
        g.add((osec_uri, QO.sectionOrder, Literal(sec_idx)))

        g.add((sec_uri, RDF.type, QO.Section))
        g.add((sec_uri, QO.sectionLabel, Literal(" / ".join(section["scale"]))))

        for q_idx, question in enumerate(section["questions"], start=1):
            add_ordered_question(
                g, sec_uri, QO.sectionHasOrderedQuestion, question["number"], q_idx
            )

    return g


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", type=Path,
                        help="the PDF, or a folder holding it; the TTL is written beside it")
    parser.add_argument("--name", default=DEFAULT_NAME, metavar="NAME",
                        help="questionnaire name used in the URIs and file names "
                             "(default: %(default)s)")
    return parser.parse_args(argv)


def require_questions(sections: list[dict], pdf_path: Path) -> int:
    """Stop when the PDF yielded nothing; returns the question count otherwise."""
    question_count = sum(len(s["questions"]) for s in sections)
    if question_count == 0:
        logger.error(
            "No questions detected in %s. The PDF may lack ruled tables or use "
            "a layout this extractor does not recognise.", pdf_path
        )
        sys.exit(1)
    return question_count


def write_questions(sections: list[dict], out_dir: Path, name: str) -> None:
    """One TTL file per question, named after the questionnaire."""
    for section in sections:
        for question in section["questions"]:
            qg, _ = build_question_graph(question["number"], question["label"],
                                         section["scale"], name)
            out_path = out_dir / f"Question-{name}_{question['number']:02d}.ttl"
            qg.serialize(destination=out_path, format="turtle")
            logger.info("Wrote %s", out_path)


def write_questionnaire(sections: list[dict], out_dir: Path, name: str) -> None:
    """The questionnaire that ties the questions together."""
    quest_g = build_questionnaire_graph(sections, name)
    out_path = out_dir / f"Questionnaire-{display_name(name)}.ttl"
    quest_g.serialize(destination=out_path, format="turtle")
    logger.info("Wrote %s", out_path)


def main() -> None:
    configure_logging("pdfToQO")
    args = parse_args()

    pdf_path = resolve_pdf(args.target)
    out_dir = pdf_path.parent
    sections = extract_frames(pdf_path)

    question_count = require_questions(sections, pdf_path)
    logger.info("Detected %d question(s) in %d section(s) in %s.",
                question_count, len(sections), pdf_path.name)

    write_questions(sections, out_dir, args.name)
    write_questionnaire(sections, out_dir, args.name)


if __name__ == "__main__":
    main()
