

# Slot: questionHasQuestionRepresentation 


_QuestionRepresentations that describe the question in each language._





URI: [faqir:questionHasQuestionRepresentation](https://faqir.org/datamodel/questionHasQuestionRepresentation)
Alias: questionHasQuestionRepresentation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [QuestionRepresentation](QuestionRepresentation.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionHasQuestionRepresentation |
| native | https://w3id.org/faqir/datamodel/questionHasQuestionRepresentation |




## LinkML Source

<details>
```yaml
name: questionHasQuestionRepresentation
description: QuestionRepresentations that describe the question in each language.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Question
slot_uri: faqir:questionHasQuestionRepresentation
alias: questionHasQuestionRepresentation
domain_of:
- Question
inverse: questionRepresentationOfQuestion
range: QuestionRepresentation
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>