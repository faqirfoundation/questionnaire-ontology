

# Slot: subject 


_The Vault this questionnaireResponse belongs to._





URI: [datamodel:subject](https://w3id.org/faqir/datamodel/subject)
Alias: subject

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [Vault](Vault.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:subject |
| native | https://w3id.org/faqir/datamodel/subject |
| undefined | fhir:QuestionnaireResponse.subject |




## LinkML Source

<details>
```yaml
name: subject
description: The Vault this questionnaireResponse belongs to.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.subject
rank: 1000
slot_uri: datamodel:subject
alias: subject
domain_of:
- QuestionnaireResponse
range: Vault
required: true

```
</details>