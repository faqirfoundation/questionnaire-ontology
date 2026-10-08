# Contributing to FAQIR Questionnaire Ontology (QO)

👍 First of all: Thank you for taking the time to contribute!

The following guidelines outline how to contribute to the FAQIR Questionnaire Ontology. These guidelines are not strict rules; use your best judgment, and feel free to propose changes to this document in a Pull Request.

## Table Of Contents

* [Code of Conduct](#code-of-conduct)
* [Guidelines for Contributions and Requests](#contributions)
  * [Reporting issues and making requests](#reporting-issues)
  * [Questions and Discussion](#questions-and-discussion)
  * [Adding New Schema Elements](#adding-elements)
* [Development Workflow & Commands](#development-workflow)
* [Best Practices](#best-practices)
  * [GitHub Best Practices](#great-issues)
  * [Modeling Best Practices](#modeling-best-practices)

---

<a id="code-of-conduct"></a>

## Code of Conduct

The FAQIR team strives to create a welcoming environment for editors, users, and contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

---

<a id="contributions"></a>

## Guidelines for Contributions and Requests

<a id="reporting-issues"></a>

### Reporting Problems and Suggesting Changes 

Please use our [Issue Tracker][issues] to:
- Report errors or inconsistencies in the ontology/schema.
- Suggest new class definitions, slots, or controlled value sets.
- Propose enhancements to documentation or build pipelines.

<a id="questions-and-discussions"></a>

### Questions and Discussions
Please use our [Discussions Forum][discussions] to ask general usage questions, suggest ideas, or discuss conceptual architecture before creating formal issues.

<a id="adding-elements"></a>

### Adding new elements yourself
To submit a new term, slot, or bug fix:
1. Fork the repository and create a feature branch off `main`.
2. Update the LinkML source schema in `src/questionnaire_ontology/schema/questionnaire_ontology.yaml`.
3. Submit a [Pull Request][pulls] referencing the relevant issue.

---
<a id="development-workflow"></a>

## Development Workflow & Local Testing

Before submitting a Pull Request, ensure your changes pass all schema checks and linting rules locally:

```bash
# 1. Install dependencies
poetry install

# 2. Run linter on LinkML schema
poetry run just lint

# 3. Re-compile schema targets (OWL, SHACL, Docs)
poetry run just gen-project

# 4. Run test suite and example validation
poetry run just test
```

---
<a id="best-practices"></a>

## Best Practices

<a id="great-issues"></a>

### GitHub Best Practice

- Creating and curating issues:
    - Read ["About Issues"][[about-issues]]
    - Issues should be focused, actionable, and single-purpose
    - Complex issues should be broken down into simpler issues where possible
- Pull Requests (PRs):
    - Read ["About Pull Requests"][about-pulls]
    - Read [GitHub Pull Requests: 10 Tips to Know](https://blog.mergify.com/github-pull-requests-10-tips-to-know/)
    - PRs should be atomic and aim to close a single issue
    - Long running PRs should be avoided where possible
    - PRs should reference issues following standard conventions (e.g. “fixes #123”)
    - Schema developers should always be working on a single issue at any one time
    - Never work on the main branch, always work on an issue/feature branch
    - Always create a PR on a branch to maximize transparency of what you are doing
    - PRs should be reviewed and merged in a timely fashion by the datamodel technical leads
    - All PRs must pass GitHub Action automated checks before merging
    - In the case of git conflicts, the contributor should try and resolve the conflict
    - If a PR fails a GitHub action check, the contributor should try and resolve the issue in a timely fashion

### Understanding LinkML

Contributors editing the core schema should familiarize themselves with [LinkML site](https://linkml.io/linkml):

- [Overview](https://linkml.io/linkml/intro/overview.html)
- [Tutorial](https://linkml.io/linkml/intro/tutorial.html)
- [Schemas](https://linkml.io/linkml/schemas/index.html)
- [FAQ](https://linkml.io/linkml/faq/index.html)

### Modeling Best Practice

- Naming conventions:
    - **Classes & Enums**: `UpperCamelCase` (e.g., `Question`, `OrderedQuestion`).
    - **Slots & Properties**: `snake_case` (e.g., `temporal_validity`, `hard_validity`).
    - **Multivalued Slots**: Pluralized nouns (e.g., `coding_params`).
    - Use the LinkML linter (`poetry run just lint`) to enforce naming rules.
    - The names for classes should be nouns or noun-phrases: Person, GenomeAnnotation, Address, Sample
    - Spell out abbreviations and short forms, except where this goes against convention (e.g. do not spell out DNA)
    - Elements that are imported from outside (e.g. schema.org) need not follow the same naming conventions
- Documentation & Annotations:
    - All model elements should have documentation (descriptions) and other textual annotations (e.g. comments, notes)
    - Textual annotations on classes, slots and enumerations should be written with minimal jargon, clear grammar and no misspellings
- Include examples and counter-examples (intentionally invalid examples):
    - All new schema capabilities should be accompanied by valid RDF Turtle example graphs in `src/data/examples/valid/`.
    - If introducing strict constraints, add intentional counter-examples to `src/data/examples/invalid/` to test SHACL/LinkML validation rules.
    - Rationale: these serve as documentation and unit tests
    - Invalid example data files should be invalid for one single reason, which should be reflected in the filename. It should be possible to render the invalid example files valid by addressing that single fault.
- Use `enums` for categorical values:
    - Rationale: Open-ended string ranges encourage multiple values to represent the same entity, like “water”, “H2O” and “HOH”
    - Any slot whose values could be constrained to a finite set should use an Enum
- Reuse Existing Vocabularies:
    - Existing scheme elements should be reused where appropriate, rather than making duplicative elements
    - More specific classes can be created by refinining classes using inheritance (`is_a`)

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/faqirfoundation/questionnaire-ontology/issues
[pulls]: https://github.com/faqirfoundation/questionnaire-ontology/pulls
