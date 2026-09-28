

# Slot: qo_basedOn 


_The ScoreDefinition that this ScoreValue is based on._





URI: [qo:basedOn](https://ns.faqir.org/q-o#basedOn)
Alias: qo_basedOn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoScoreValue](QoScoreValue.md) | The score value calculated from a QuestionnaireResponse following a ScoreDefi... |  no  |







## Properties

* Range: [QoScoreDefinition](QoScoreDefinition.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:basedOn |
| native | qo:qo_basedOn |




## LinkML Source

<details>
```yaml
name: qo_basedOn
description: The ScoreDefinition that this ScoreValue is based on.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: qo_ScoreValue
slot_uri: qo:basedOn
alias: qo_basedOn
domain_of:
- qo_ScoreValue
range: qo_ScoreDefinition
required: true
multivalued: false

```
</details>