

# Slot: qo_intervalParams 


_Minimum and Maximum limiting the range the answer must be in for the question._





URI: [qo:intervalParams](https://ns.faqir.org/q-o#intervalParams)
Alias: qo_intervalParams

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | A question |  no  |







## Properties

* Range: [IntervalParams](IntervalParams.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:intervalParams |
| native | qo:qo_intervalParams |




## LinkML Source

<details>
```yaml
name: qo_intervalParams
description: Minimum and Maximum limiting the range the answer must be in for the
  question.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:intervalParams
alias: qo_intervalParams
owner: qo_Question
domain_of:
- qo_Question
range: IntervalParams
required: false
multivalued: false

```
</details>