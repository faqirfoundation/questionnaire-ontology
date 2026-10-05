

# Slot: qo_temporalValidity 


_Defines the time extent following generation during which a recorded answer remains valid for automated longitudinal reuse without requiring re-administration._





URI: [qo:temporalValidity](https://ns.faqir.org/q-o#temporalValidity)
Alias: qo_temporalValidity


## Inheritance

* [time_hasDuration](time_hasDuration.md)
    * **qo_temporalValidity**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |






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
description: Defines the time extent following generation during which a recorded
  answer remains valid for automated longitudinal reuse without requiring re-administration.
from_schema: https://ns.faqir.org/q-o
rank: 1000
is_a: time_hasDuration
slot_uri: qo:temporalValidity
alias: qo_temporalValidity
domain_of:
- qo_OrderedQuestion
range: time_Duration
required: true

```
</details>