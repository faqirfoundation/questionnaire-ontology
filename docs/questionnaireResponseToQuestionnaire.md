

# Slot: questionnaireResponseToQuestionnaire 


_The Questionnaire that this QuestionnaireResponse is for._





URI: [faqir:questionnaireResponseToQuestionnaire](https://faqir.org/datamodel/questionnaireResponseToQuestionnaire)
Alias: questionnaireResponseToQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnaireResponseToQuestionnaire |
| native | https://w3id.org/faqir/datamodel/questionnaireResponseToQuestionnaire |
| undefined | fhir:questionnaireResponse.questionnaire |




## LinkML Source

<details>
```yaml
name: questionnaireResponseToQuestionnaire
description: The Questionnaire that this QuestionnaireResponse is for.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:questionnaireResponse.questionnaire
rank: 1000
domain: QuestionnaireResponse
slot_uri: faqir:questionnaireResponseToQuestionnaire
alias: questionnaireResponseToQuestionnaire
domain_of:
- QuestionnaireResponse
inverse: questionnaireHasQuestionnaireResponse
range: Questionnaire
required: true
multivalued: false

```
</details>