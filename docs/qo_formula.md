

# Slot: qo_formula 


_The formula used to calculate the score._





URI: [qo:formula](https://ns.faqir.org/q-o#formula)
Alias: qo_formula

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoScoreDefinition](QoScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:formula |
| native | qo:qo_formula |




## LinkML Source

<details>
```yaml
name: qo_formula
description: The formula used to calculate the score.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:formula
alias: qo_formula
owner: qo_ScoreDefinition
domain_of:
- qo_ScoreDefinition
range: string
required: true

```
</details>