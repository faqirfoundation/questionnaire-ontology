

# Slot: questionnaireHasQuestionnaireResponse 


_The QuestionnaireResponse that is associated with this Questionnaire._





URI: [faqir:questionnaireHasQuestionnaireResponse](https://faqir.org/datamodel/questionnaireHasQuestionnaireResponse)
Alias: questionnaireHasQuestionnaireResponse

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
| self | faqir:questionnaireHasQuestionnaireResponse |
| native | https://w3id.org/faqir/datamodel/questionnaireHasQuestionnaireResponse |
| undefined | fhir:QuestionnaireResponse |




## LinkML Source

<details>
```yaml
name: questionnaireHasQuestionnaireResponse
description: The QuestionnaireResponse that is associated with this Questionnaire.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse
rank: 1000
domain: Questionnaire
slot_uri: faqir:questionnaireHasQuestionnaireResponse
alias: questionnaireHasQuestionnaireResponse
domain_of:
- Questionnaire
inverse: questionnaireResponseToQuestionnaire
range: QuestionnaireResponse
multivalued: true

```
</details>