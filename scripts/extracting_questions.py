"""Extract questions from a PDF questionnaire (WHOQOL, EQ-5D, etc.) and
list them.

Usage:
    python extracting_questions.py path/to/questionnaire.pdf
    python extracting_questions.py path/to/questionnaire.pdf --output questions.txt
    python extracting_questions.py path/to/questionnaire.pdf --json questions.json

How it works:
    1. Extract text per page with pdfplumber.
    2. Detect question lines via numbered items ("1.", "Q1.", "Vraag 1:")
       or lines ending in a question mark.
    3. Print a numbered list, optionally written to .txt or .json.

Note: questionnaire layouts vary a lot. This recognises the most common
patterns only; always check the output, especially for complex layouts
(columns, tables, scanned documents).
"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path

import pdfplumber

# Shared helpers live one folder up.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logging_setup import configure_logging

log = logging.getLogger("extracting_questions")


# Question-line patterns, ordered specific -> general (first match wins).
# Compiled once here rather than on every line of every page.
NUMBERED_PATTERNS = [
    re.compile(r"^\s*(?:Q|Vraag|Question)\s*\d+[\.\):]?\s*(.+)"),  # "Q1.", "Vraag 3:", "Question 12)"
    re.compile(r"^\s*\d{1,3}[\.\)]\s+(.+)"),                        # "1.", "23)"
]

QUESTION_MARK_PATTERN = re.compile(r"^(.{5,300}\?)\s*$")  # line ending in '?'


def looks_like_question(line: str) -> str | None:
    """Return the cleaned question text if the line is a question, else None."""
    line = line.strip()
    if not line:
        return None

    # Numbered items; many questionnaires phrase questions as statements.
    for pattern in NUMBERED_PATTERNS:
        match = pattern.match(line)
        if match:
            text = match.group(1).strip()
            if len(text) > 3:  # ignore matches too short to be a question
                return text

    # Lines ending in a question mark, even without numbering.
    match = QUESTION_MARK_PATTERN.match(line)
    if match:
        return match.group(1).strip()

    return None


def extract_questions_from_pdf(pdf_path: Path) -> list[dict]:
    """
    Read the PDF and return the questions found in it,
    each with its page number and text.
    """
    questions = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if not text:
                continue  # empty or scanned page without OCR

            for line in text.split("\n"):
                question_text = looks_like_question(line)
                if question_text:
                    questions.append({
                        "page": page_num,
                        "text": question_text
                    })

    return questions


def deduplicate(questions: list[dict]) -> list[dict]:
    """Remove exact duplicates (e.g. headers/footers repeated per page)."""
    seen = set()
    unique = []
    for q in questions:
        key = q["text"].lower()
        if key not in seen:
            seen.add(key)
            unique.append(q)
    return unique


def log_questions(questions: list[dict]) -> None:
    if not questions:
        log.warning("No questions found. Possible causes: the PDF is scanned "
                    "(image) instead of searchable text, so OCR is needed; or "
                    "the question formatting differs from the recognised "
                    "patterns (adjust NUMBERED_PATTERNS for your document).")
        return

    log.info("%d questions found", len(questions))
    for i, q in enumerate(questions, start=1):
        log.info("%3d. [p.%s] %s", i, q["page"], q["text"])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract questions from a PDF questionnaire")
    parser.add_argument("pdf_path", type=Path, help="path to the PDF questionnaire")
    parser.add_argument("--output", "-o", type=Path, metavar="FILE",
                        help="write the result to a .txt file")
    parser.add_argument("--json", "-j", type=Path, metavar="FILE",
                        help="write the result to a .json file")
    return parser.parse_args(argv)


def require_existing_pdf(pdf_path: Path) -> None:
    """Stop with a readable message when the PDF is not there."""
    if not pdf_path.exists():
        log.error("file not found: %s", pdf_path)
        sys.exit(1)


def write_text_file(questions: list[dict], path: Path) -> None:
    """Write the questions as a numbered plain-text list."""
    with path.open("w", encoding="utf-8") as f:
        for i, q in enumerate(questions, start=1):
            f.write(f"{i}. [p.{q['page']}] {q['text']}\n")
    log.info("Written to: %s", path)


def write_json_file(questions: list[dict], path: Path) -> None:
    """Write the questions as JSON, one entry per question."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    log.info("Written to: %s", path)


def main() -> None:
    configure_logging("extracting_questions")
    args = parse_args()
    require_existing_pdf(args.pdf_path)

    questions = deduplicate(extract_questions_from_pdf(args.pdf_path))
    log_questions(questions)

    if args.output:
        write_text_file(questions, args.output)
    if args.json:
        write_json_file(questions, args.json)


if __name__ == "__main__":
    main()