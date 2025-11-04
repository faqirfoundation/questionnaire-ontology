

# Slot: questionnaireResponseBySubject 


_The subject that has authored this QuestionnaireResponse._





URI: [faqir:questionnaireResponseBySubject](https://faqir.org/datamodel/questionnaireResponseBySubject)
Alias: questionnaireResponseBySubject

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
| self | faqir:questionnaireResponseBySubject |
| native | https://w3id.org/faqir/datamodel/questionnaireResponseBySubject |
| undefined | fhir:questionnaireResponse.subject |




## LinkML Source

<details>
```yaml
name: questionnaireResponseBySubject
description: The subject that has authored this QuestionnaireResponse.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:questionnaireResponse.subject
rank: 1000
domain: QuestionnaireResponse
slot_uri: faqir:questionnaireResponseBySubject
alias: questionnaireResponseBySubject
domain_of:
- QuestionnaireResponse
inverse: hasQuestionnaireResponse
range: Vault
required: true
multivalued: false

```
</details>