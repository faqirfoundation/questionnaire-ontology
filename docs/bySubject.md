

# Slot: bySubject 


_The subject that has authored this QuestionnaireResponse._





URI: [datamodel:bySubject](https://w3id.org/faqir/datamodel/bySubject)
Alias: bySubject

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
| self | datamodel:bySubject |
| native | https://w3id.org/faqir/datamodel/bySubject |
| undefined | fhir:QuestionnaireResponse.subject |




## LinkML Source

<details>
```yaml
name: bySubject
description: The subject that has authored this QuestionnaireResponse.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.subject
rank: 1000
domain: QuestionnaireResponse
slot_uri: datamodel:bySubject
alias: bySubject
domain_of:
- QuestionnaireResponse
inverse: hasQuestionnaireResponse
range: Vault
required: true
multivalued: false

```
</details>