

# Slot: answerInQuestionnaireResponse 


_The QuestionnaireResponse that this Answer is part of._





URI: [faqir:answerInQuestionnaireResponse](https://faqir.org/datamodel/answerInQuestionnaireResponse)
Alias: answerInQuestionnaireResponse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [QuestionnaireResponse](QuestionnaireResponse.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:answerInQuestionnaireResponse |
| native | https://w3id.org/faqir/datamodel/answerInQuestionnaireResponse |
| undefined | fhir:QuestionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: answerInQuestionnaireResponse
description: The QuestionnaireResponse that this Answer is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer
rank: 1000
domain: Answer
slot_uri: faqir:answerInQuestionnaireResponse
alias: answerInQuestionnaireResponse
domain_of:
- Answer
inverse: questionnaireResponseHasAnswer
range: QuestionnaireResponse
required: true
multivalued: false

```
</details>