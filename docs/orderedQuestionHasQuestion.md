

# Slot: orderedQuestionHasQuestion 


_Question indexed in this OrderedQuestion._





URI: [faqir:orderedQuestionHasQuestion](https://faqir.org/datamodel/orderedQuestionHasQuestion)
Alias: orderedQuestionHasQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedQuestion](OrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Question](Question.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:orderedQuestionHasQuestion |
| native | https://w3id.org/faqir/datamodel/orderedQuestionHasQuestion |




## LinkML Source

<details>
```yaml
name: orderedQuestionHasQuestion
description: Question indexed in this OrderedQuestion.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: OrderedQuestion
slot_uri: faqir:orderedQuestionHasQuestion
alias: orderedQuestionHasQuestion
domain_of:
- OrderedQuestion
inverse: questionInOrderedQuestion
range: Question
required: true
multivalued: false

```
</details>