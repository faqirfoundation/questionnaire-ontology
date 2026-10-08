

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
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |







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
- qo_Questionnaire
- qo_OrderedSection
- qo_Section
- qo_OrderedQuestion
- qo_Question
range: time_Duration
required: true

```
</details>