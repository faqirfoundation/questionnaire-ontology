

# Slot: questionHasAnswer 


_The Answer to this Question._





URI: [faqir:questionHasAnswer](https://faqir.org/datamodel/questionHasAnswer)
Alias: questionHasAnswer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [Answer](Answer.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionHasAnswer |
| native | https://w3id.org/faqir/datamodel/questionHasAnswer |
| undefined | fhir:Questionnaire.item.answer |




## LinkML Source

<details>
```yaml
name: questionHasAnswer
description: The Answer to this Question.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.answer
rank: 1000
domain: Question
slot_uri: faqir:questionHasAnswer
alias: questionHasAnswer
domain_of:
- Question
inverse: answerToQuestion
range: Answer
required: false
multivalued: true

```
</details>