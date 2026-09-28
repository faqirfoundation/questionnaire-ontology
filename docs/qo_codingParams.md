

# Slot: qo_codingParams 


_Code and Display of each option offered as answer to the choice or open-choice question._





URI: [qo:codingParams](https://ns.faqir.org/q-o#codingParams)
Alias: qo_codingParams

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | A question |  no  |







## Properties

* Range: [ValueCoding](ValueCoding.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:codingParams |
| native | qo:qo_codingParams |




## LinkML Source

<details>
```yaml
name: qo_codingParams
description: Code and Display of each option offered as answer to the choice or open-choice
  question.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:codingParams
alias: qo_codingParams
owner: qo_Question
domain_of:
- qo_Question
range: ValueCoding
required: false
multivalued: true

```
</details>