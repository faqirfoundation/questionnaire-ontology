# FAQIR Questionnaire Ontology (QO)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![LinkML](https://img.shields.io/badge/Schema-LinkML-green.svg)](https://linkml.io)
[![W3C RDF/OWL](https://img.shields.io/badge/Format-RDF%2FOWL%2FSHACL-orange.svg)](project/)

The **FAQIR Questionnaire Ontology (QO)** is a FAIR-by-design semantic framework that transforms static, document-based questionnaire artifacts (e.g., PDFs, paper forms) into queryable, machine-readable Knowledge Graphs. 

**QO** decouples atomic, context-agnostic inquiry items (`qo:Question`) from survey-specific layout wrappers (`qo:OrderedQuestion`). It introduces machine-actionable **temporal validity reasoning** (`qo:temporalValidity`, `qo:hardValidity`) to actively mitigate question-survey fatigue in longitudinal patient care.

> 📖 **Paper Reference:** This repository contains the official semantic source schema, generated artifacts, and validation use cases for the paper:  
> *"A Semantic Model for Reusable Questionnaires and Temporal Answer Validity in Healthcare"* (submitted to SWAT4HCLS 2027).

---

## 🚀 Key Features

* **Dual-Level Architecture:** Separates atomic content definitions from contextual questionnaire layout wrappers to enable global question reusability and prevent graph fragmentation.
* **Blank Node Mitigation:** Assigns global URIs across all core structural components (Questionnaires, Questions, Wrappers, Answers), restricting anonymous blank nodes strictly to inline datatype parameters (e.g., `fhir:Coding`).
* **Upper-Ontology Grounding:** Direct mapping and subclassing from W3C PROV-O (`prov:Entity`), Dublin Core (`dcterms:`), FOAF (`foaf:Agent`), and ETSI SAREF (`saref:PropertyValue`).
* **Historical Auditability:** Reifies resource state tracking (`qo:QuestionnaireStatus`, `qo:QuestionnaireResponseStatus`) linked to SNOMED CT (`snomed:263490005`) and FHIR status value sets.
* **LinkML Tooling:** Authorship grounded in LinkML, compiling automatically into W3C OWL (`.owl.ttl`), SHACL (`.shacl.ttl`), JSON-Schema, and Markdown documentation.

---

## 📂 Repository Structure

```text
.
├── src/
│   ├── questionnaire_ontology/
│   │   └── schema/
│   │       └── questionnaire_ontology.yaml # Canonical LinkML Source Schema
│   └── data/examples/
│       └── valid/                          # Input source example graphs (EQ-5D, WHOQOL)
├── project/                                # Auto-generated schema artifacts
│   ├── owl/                                # Post-processed W3C OWL ontologies (.owl.ttl)
│   ├── shacl/                              # Derived W3C SHACL shape targets (.shacl.ttl)
│   └── prefixmap/                          # URI Prefix mappings (prefixmap.yaml)
├── examples/                               # Executable Knowledge Graph instantiations
│   └── output/                             # Validated RDF Turtle instance graphs
│       ├── eq5d5l-questionnaire.ttl
│       └── whoqol-bref-questionnaire.ttl
├── diagrams/                               # Architecture & UML Mermaid diagrams (PNG/SVG)
├── docs/                                   # LinkML auto-generated Markdown docs & submitted paper
├── scripts/
│   ├── post_process_owl.py                 # OWL schema post-processing script
│   ├── pdfToQO.py                          # Read a table-based PDF questionnaire and write qo: TTL files
│   └── extracting_questions.py             # PDF-to-RDF extraction pipeline for legacy surveys
├── tests/                                  # Automated python schema validation suite
├── justfile / project.justfile             # Task runner automation rules
├── pyproject.toml / poetry.lock            # Python environment configuration
└── README.md
```

## 🛠️ Installation & Setup
This project uses Poetry for dependency management and **Just** as a command runner.

**Prerequisites**
- Python $\ge$ 3.10
- Poetry
- [just](https://github.com/casey/just/)

### Quickstart
1. Clone the repository:
```
git clone [https://github.com/faqirfoundation/questionnaire-ontology.git](https://github.com/faqirfoundation/questionnaire-ontology.git)
cd questionnaire-ontology
```

2. Install dependencies:
```
poetry install
```

3. Run the full build and verification pipeline:
```
# Test schema, pytests and examples
poetry run just test

# Generate documentation site locally
poetry run just testdoc

# List all pre-defined tasks
poetry run just --list
```

## 🔬 Validation & Example Knowledge Graphs
The repository includes complete Knowledge Graph instantiations for two real-world, validated Patient-Reported Outcome Measures (PROMs):
- EuroQol EQ-5D-5L (examples/output/eq5d5l-questionnaire.ttl)
- WHOQOL-BREF (examples/output/whoqol-bref-questionnaire.ttl)

### Automatic Ingestion from PDF
You can extract questions from legacy PDF survey questionnaires directly into structured formats using our extraction pipeline:
```
# Generic text PDF questionnaire
poetry run python scripts/extracting_questions.py path/to/questionnaire.pdf --json questions.json

# Table-based PDF questionnaire
poetry run python pdfToQO.py <pdf-or-folder> [--name NAME]
```

## 📑 Generating Schema Artifacts
If you modify the source LinkML schema (src/questionnaire_ontology/schema/questionnaire_ontology.yaml), re-compile the down-stream artifacts (OWL, SHACL, Markdown docs) using:
```
# Generate all project targets and examples via Just
poetry run just gen-project

# Run post-processing repair on generated OWL
poetry run python scripts/post_process_owl.py
```

Generated outputs will be updated automatically in `project/` and `docs/.``

## 👥 Authors & Acknowledgments
The FAQIR Questionnaire Ontology is developed and maintained by the FAQIR Foundation.
- Namespace URI: `https://ns.faqir.org/q-o#` (Prefix: qo:)
- Issue Tracker: GitHub Issues

We welcome contributions! Please review `CONTRIBUTING.md` and our `CODE_OF_CONDUCT.md` before submitting Pull Requests.

## 📄 License
This repository is distributed under the terms of the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. See `LICENSE` for details.