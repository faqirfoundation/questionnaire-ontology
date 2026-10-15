# FAQIR Questionnaire Ontology: SPARQL Competency Questions

This directory contains the SPARQL queries that answer the competency questions (CQs) of the **FAQIR Questionnaire Ontology (QO)**, together with their results over the example knowledge graphs in [`../output`](../output).

---

## 📁 Competency Questions

| CQ | Folder | Competency question | Example input | Data |
|----|--------|---------------------|---------------|------|
| CQ1 | [`cq1_composition`](cq1_composition) | Which atomic questions and sections constitute a given questionnaire template, and what are their positional sequence indices? | WHOQOL-BREF questionnaire | WHOQOL-BREF |
| CQ2 | [`cq2_datatype_constraints`](cq2_datatype_constraints) | What input datatype, permissible coding options, or numeric range parameters govern a specific atomic question? | EQ-5D-5L questions 01 and VAS; WHOQOL-BREF question G4 | EQ-5D-5L / WHOQOL-BREF |
| CQ3 | [`cq3_temporal_validity`](cq3_temporal_validity) | Is a patient's previously recorded answer to an atomic question still valid at the timestamp of a new survey session? | Answer `answer_WHOQOL_BREF_02_a01`, session on `2026-07-10T09:34:10` | WHOQOL-BREF |
| CQ4 | [`cq4_deferral_eligibility`](cq4_deferral_eligibility) | Which questions in a new questionnaire can be automatically deferred or pre-filled based on valid, consent-authorized historical answers? | WHOQOL-BREF for `patient123`, session on `2026-07-10T09:34:10` | WHOQOL-BREF |
| CQ5 | [`cq5_cross_instrument`](cq5_cross_instrument) | Which distinct validated instruments share the same atomic question or SNOMED CT clinical concept tag? | WHOQOL-BREF vs EQ-5D-5L | WHOQOL-BREF + EQ-5D-5L |

Each folder contains the query (`query.rq`, or one query per instrument for CQ2) and its result (`results.json`) in the standard [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json/).

---

## 🛠 Requirements

The queries are executed with the `sparql` command of [Apache Jena](https://jena.apache.org/) (requires a Java runtime; Homebrew installs one as a dependency). The results in this directory were produced with Jena 6.2.0.

```bash
# macOS (Homebrew)
brew install jena

# Check the installation
sparql --version
```

On other platforms, download the `apache-jena` binary distribution from the [Jena downloads page](https://jena.apache.org/download/) and add its `bin/` directory to your `PATH`.

> **Note:** CQ3 and CQ4 add an `xsd:dayTimeDuration` to an `xsd:dateTime`. Jena, GraphDB and RDF4J support this, but `rdflib` does not, so these two queries cannot be run with `rdflib`.

---

## ▶️ Executing the Queries

Run the commands from the repository root. `--data` loads an example graph (it can be repeated to load several), `--query` selects the query file and `--results` selects the output format.

### Print the results in the terminal

```bash
sparql --data examples/output/whoqol-bref-questionnaire.ttl --query examples/sparql/cq1_composition/query.rq
```

The default output is a text table. Use `--results=csv`, `--results=tsv`, `--results=xml` or `--results=json` for other formats.

### Regenerate the stored results

**CQ1 - Composition**

```bash
sparql --data examples/output/whoqol-bref-questionnaire.ttl --query examples/sparql/cq1_composition/query.rq --results=json > examples/sparql/cq1_composition/results.json
```

**CQ2 - Datatype constraints**

```bash
sparql --data examples/output/eq5d5l-questionnaire.ttl --query examples/sparql/cq2_datatype_constraints/query-eq5d5l.rq --results=json > examples/sparql/cq2_datatype_constraints/results-eq5d5l.json
```

```bash
sparql --data examples/output/whoqol-bref-questionnaire.ttl --query examples/sparql/cq2_datatype_constraints/query-whoqol-bref.rq --results=json > examples/sparql/cq2_datatype_constraints/results-whoqol-bref.json
```

**CQ3 - Temporal validity**

```bash
sparql --data examples/output/whoqol-bref-questionnaire.ttl --query examples/sparql/cq3_temporal_validity/query.rq --results=json > examples/sparql/cq3_temporal_validity/results.json
```

**CQ4 - Deferral eligibility**

```bash
sparql --data examples/output/whoqol-bref-questionnaire.ttl --query examples/sparql/cq4_deferral_eligibility/query.rq --results=json > examples/sparql/cq4_deferral_eligibility/results.json
```

**CQ5 - Cross-instrument overlap** (needs both graphs)

```bash
sparql --data examples/output/whoqol-bref-questionnaire.ttl --data examples/output/eq5d5l-questionnaire.ttl --query examples/sparql/cq5_cross_instrument/query.rq --results=json > examples/sparql/cq5_cross_instrument/results.json
```

Jena writes its log messages to stderr, so they never end up in the result files.

---

## ⚙️ Changing the Query Inputs

Each query is parameterised with a `VALUES` block at the top of its `WHERE` clause, marked with the comment `(replace as needed)`. Edit it to run the same question over other entities:

| CQ | Parameters in `VALUES` |
|----|------------------------|
| CQ1 | `?questionnaire` |
| CQ2 | `?question` (one or more) |
| CQ3 | `?answer`, `?sessionTime` |
| CQ4 | `?questionnaire`, `?patient`, `?sessionTime` |
| CQ5 | `?instrumentA`, `?instrumentB` (one row per pair) |

Session timestamps must be typed `xsd:dateTime` literals, for example `"2026-07-10T09:34:10.168913+00:00"^^xsd:dateTime`. Remember to load every graph the new inputs live in with additional `--data` arguments.

---

## 📝 Modelling Assumptions

* **Temporal validity (CQ3, CQ4):** `qo:temporalValidity` can be declared on the `qo:Questionnaire`, `qo:OrderedSection`, `qo:Section`, `qo:OrderedQuestion` and `qo:Question` that contain an answered question. The most restrictive (earliest) expiry wins. An expired level with `qo:hardValidity true` invalidates the answer; an expired soft level only sets `?reAdministrationRecommended`. Durations are converted from UCUM units (`s`, `min`, `h`, `d`, `wk`, `mo` = 30.4375 d, `a` = 365.25 d).
* **Conditional validity (CQ3, CQ4):** `qo:conditionalValidity` rules are free-text statements; they are returned for review but not evaluated.
* **Deferral (CQ4):** only the patient's latest answer to each `qo:Question` before the session is considered, with its validity evaluated in the context where it was recorded. Only deferrable questions are returned. Consent is not modelled in the schema and is assumed to be checked outside the query.
* **Cross-instrument matching (CQ5):** two questions match when they are the same `qo:Question` or share at least one `qo:tag`. Matching is exact, so related but different SNOMED CT concepts (e.g. subsumption) are not paired. Each shared tag is returned in its own row.
