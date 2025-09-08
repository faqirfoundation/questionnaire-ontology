

# Slot: answerValue 


_The value of the answer, which may be a numeric value, dateTime, or text depending on the question type._





URI: [datamodel:answerValue](https://w3id.org/faqir/datamodel/answerValue)
Alias: answerValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [QuestionType](QuestionType.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:answerValue |
| native | https://w3id.org/faqir/datamodel/answerValue |
| undefined | fhir:QuestionnaireResponse.item.answer.valueString, fhir:QuestionnaireResponse.item.answer.valueDecimal, fhir:QuestionnaireResponse.item.answer.valueDateTime, fhir:QuestionnaireResponse.item.answer.valueCoding, fhir:QuestionnaireResponse.item.answer.AnswerOption |




## LinkML Source

<details>
```yaml
name: answerValue
description: The value of the answer, which may be a numeric value, dateTime, or text
  depending on the question type.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer.valueString
- fhir:QuestionnaireResponse.item.answer.valueDecimal
- fhir:QuestionnaireResponse.item.answer.valueDateTime
- fhir:QuestionnaireResponse.item.answer.valueCoding
- fhir:QuestionnaireResponse.item.answer.AnswerOption
rank: 1000
slot_uri: datamodel:answerValue
alias: answerValue
domain_of:
- Answer
range: QuestionType
required: false
multivalued: true

```
</details>