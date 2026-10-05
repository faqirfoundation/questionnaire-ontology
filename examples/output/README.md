# FAQIR Questionnaire Ontology: Example Knowledge Graphs

This directory contains validated RDF Turtle (`.ttl`) Knowledge Graph instantiations generated using the **FAQIR Questionnaire Ontology (QO)**. 

These example graphs demonstrate how real-world, standardized Patient-Reported Outcome Measures (PROMs) are transformed into FAIR-compliant knowledge graphs. By decoupling atomic inquiry definitions (`qo:Question`) from contextual wrappers (`qo:OrderedQuestion`), the FAQIR model supports longitudinal answer validity tracking, multilingual representation, and global answer reusability.

---

## 📁 Included Examples

### 1. EuroQol EQ-5D-5L 3.0 Questionnaire
* **File:** [`eq5d5l-questionnaire.ttl`](eq5d5l-questionnaire.ttl)
* **Source Instrument:** [EuroQol EQ-5D-5L](https://euroqol.org/information-and-support/euroqol-instruments/eq-5d-5l/)
* **Description:**  
  The EQ-5D-5L is a standardized instrument developed by the EuroQol Group to measure health-related quality of life across five key dimensions: *Mobility*, *Self-Care*, *Usual Activities*, *Pain/Discomfort*, and *Anxiety/Depression*. 
* **Key Modeling Features:**
  * Demonstrates a lightweight, 5-item single-section questionnaire structure.
  * Binds multilingual RDF labels (`@en`, `@es`) directly to context-agnostic `qo:Question` entities.
  * Mapped to SNOMED CT observable entity concepts (`qo:tag`) to support cross-instrument data cross-walks.
  * Illustrates strict daily temporal validity (`qo:temporalValidity = P1D`) for acute daily self-evaluations (e.g., assessing health "TODAY").
  * Uses FHIR coding value sets mapped to standardized 5-point ordinal response choices.

---

### 2. WHOQOL-BREF Questionnaire
* **File:** [`whoqol-bref-questionnaire.ttl`](whoqol-bref-questionnaire.ttl)
* **Source Instrument:** [WHOQOL-BREF (World Health Organization)](https://www.who.int/tools/whoqol/whoqol-bref)
* **Description:**  
  The WHOQOL-BREF is an international, multi-domain quality-of-life assessment instrument developed by the World Health Organization. It comprises 26 items covering four primary health domains: *Physical Health*, *Psychological Health*, *Social Relationships*, and *Environment*.
* **Key Modeling Features:**
  * Demonstrates complex, multi-section questionnaire partitioning (`qo:Section` containers holding `qo:OrderedSection` wrappers).
  * Binds multilingual RDF labels (`@en`, `@es`) directly to context-agnostic `qo:Question` entities.
  * Mapped to SNOMED CT observable entity concepts (`qo:tag`) to support cross-instrument data cross-walks.
  * Configured with a default two-week temporal validity window (`qo:temporalValidity = P2W`).

---

## 🛠 Usage & Verification

These `.ttl` files are ready to be queried using SPARQL or loaded into any standard RDF triplestore (e.g., GraphDB, Apache Jena, RDF4J).

### Validating against SHACL Shapes
You can validate these output instance graphs against compiled W3C SHACL shapes using LinkML tooling or `pyshacl`:

```bash
# Validate using LinkML built-in runner from the repository root
poetry run just test