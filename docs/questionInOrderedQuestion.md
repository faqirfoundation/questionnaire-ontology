

# Slot: questionInOrderedQuestion 


_OrderedQuestions that this Question is indexed in._





URI: [faqir:questionInOrderedQuestion](https://faqir.org/datamodel/questionInOrderedQuestion)
Alias: questionInOrderedQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [OrderedQuestion](OrderedQuestion.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionInOrderedQuestion |
| native | https://w3id.org/faqir/datamodel/questionInOrderedQuestion |




## LinkML Source

<details>
```yaml
name: questionInOrderedQuestion
description: OrderedQuestions that this Question is indexed in.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Question
slot_uri: faqir:questionInOrderedQuestion
alias: questionInOrderedQuestion
domain_of:
- Question
inverse: orderedQuestionHasQuestion
range: OrderedQuestion
required: false
multivalued: true

```
</details>