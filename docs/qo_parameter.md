

# Slot: qo_parameter 


_The ScoreParameter that is required for this ScoreDefinition._





URI: [qo:parameter](https://ns.faqir.org/q-o#parameter)
Alias: qo_parameter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoScoreDefinition](QoScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [QoScoreParameter](QoScoreParameter.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:parameter |
| native | qo:qo_parameter |




## LinkML Source

<details>
```yaml
name: qo_parameter
description: The ScoreParameter that is required for this ScoreDefinition.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: qo_ScoreDefinition
slot_uri: qo:parameter
alias: qo_parameter
domain_of:
- qo_ScoreDefinition
range: qo_ScoreParameter
required: false
multivalued: true

```
</details>