

# Slot: questionRepresentationLanguage 


_The language of the question text, represented as a BCP 47 language tag (e.g., 'en', 'fr', 'es')._





URI: [https://w3id.org/faqir/datamodel/questionRepresentationLanguage](https://w3id.org/faqir/datamodel/questionRepresentationLanguage)
Alias: questionRepresentationLanguage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionRepresentation](QuestionRepresentation.md) | The text representation of the question, in a specific language |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[a-z]{2}(-[A-Z]{2})?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/questionRepresentationLanguage |
| native | https://w3id.org/faqir/datamodel/questionRepresentationLanguage |




## LinkML Source

<details>
```yaml
name: questionRepresentationLanguage
description: The language of the question text, represented as a BCP 47 language tag
  (e.g., 'en', 'fr', 'es').
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: questionRepresentationLanguage
owner: QuestionRepresentation
domain_of:
- QuestionRepresentation
range: string
required: true
pattern: ^[a-z]{2}(-[A-Z]{2})?$

```
</details>