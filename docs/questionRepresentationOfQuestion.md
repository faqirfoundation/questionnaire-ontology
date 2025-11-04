

# Slot: questionRepresentationOfQuestion 


_The Question that this QuestionRepresentation describes._





URI: [faqir:questionRepresentationOfQuestion](https://faqir.org/datamodel/questionRepresentationOfQuestion)
Alias: questionRepresentationOfQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionRepresentation](QuestionRepresentation.md) | The text representation of the question, in a specific language |  no  |







## Properties

* Range: [Question](Question.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionRepresentationOfQuestion |
| native | https://w3id.org/faqir/datamodel/questionRepresentationOfQuestion |




## LinkML Source

<details>
```yaml
name: questionRepresentationOfQuestion
description: The Question that this QuestionRepresentation describes.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: QuestionRepresentation
slot_uri: faqir:questionRepresentationOfQuestion
alias: questionRepresentationOfQuestion
domain_of:
- QuestionRepresentation
inverse: questionHasQuestionRepresentation
range: Question
required: true
multivalued: false

```
</details>