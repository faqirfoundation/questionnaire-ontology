

# Slot: qo_question 


_Question indexed in this OrderedQuestion._





URI: [qo:question](https://ns.faqir.org/q-o#question)
Alias: qo_question


## Inheritance

* [dcterms_hasPart](dcterms_hasPart.md)
    * **qo_question**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [QoQuestion](QoQuestion.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:question |
| native | qo:qo_question |




## LinkML Source

<details>
```yaml
name: qo_question
description: Question indexed in this OrderedQuestion.
from_schema: https://ns.faqir.org/q-o
rank: 1000
is_a: dcterms_hasPart
domain: qo_OrderedQuestion
slot_uri: qo:question
alias: qo_question
domain_of:
- qo_OrderedQuestion
range: qo_Question
required: true
multivalued: true

```
</details>