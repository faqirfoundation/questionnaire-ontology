

# Slot: qo_temporalValidity 


_The time duration during which the answer is considered valid._





URI: [qo:temporalValidity](https://ns.faqir.org/q-o#temporalValidity)
Alias: qo_temporalValidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [TimeDuration](TimeDuration.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:temporalValidity |
| native | qo:qo_temporalValidity |




## LinkML Source

<details>
```yaml
name: qo_temporalValidity
description: The time duration during which the answer is considered valid.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:temporalValidity
alias: qo_temporalValidity
domain_of:
- qo_OrderedQuestion
range: time_Duration
required: true

```
</details>