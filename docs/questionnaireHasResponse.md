

# Slot: questionnaireHasResponse 


_The QuestionnaireResponse that is associated with this Questionnaire._





URI: [datamodel:questionnaireHasResponse](https://w3id.org/faqir/datamodel/questionnaireHasResponse)
Alias: questionnaireHasResponse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [QuestionnaireResponse](QuestionnaireResponse.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:questionnaireHasResponse |
| native | https://w3id.org/faqir/datamodel/questionnaireHasResponse |
| undefined | fhir:QuestionnaireResponse |




## LinkML Source

<details>
```yaml
name: questionnaireHasResponse
description: The QuestionnaireResponse that is associated with this Questionnaire.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse
rank: 1000
domain: Questionnaire
slot_uri: datamodel:questionnaireHasResponse
alias: questionnaireHasResponse
domain_of:
- Questionnaire
inverse: responseToQuestionnaire
range: QuestionnaireResponse
multivalued: true

```
</details>