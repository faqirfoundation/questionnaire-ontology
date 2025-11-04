

# Slot: scoreDefinitionHasScoreValue 


_The ScoreValue that is calculated following this ScoreDefinition._





URI: [faqir:scoreDefinitionHasScoreValue](https://faqir.org/datamodel/scoreDefinitionHasScoreValue)
Alias: scoreDefinitionHasScoreValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreDefinition](ScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [ScoreValue](ScoreValue.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreDefinitionHasScoreValue |
| native | https://w3id.org/faqir/datamodel/scoreDefinitionHasScoreValue |




## LinkML Source

<details>
```yaml
name: scoreDefinitionHasScoreValue
description: The ScoreValue that is calculated following this ScoreDefinition.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: ScoreDefinition
slot_uri: faqir:scoreDefinitionHasScoreValue
alias: scoreDefinitionHasScoreValue
domain_of:
- ScoreDefinition
inverse: scoreValueBasedOnScoreDefinition
range: ScoreValue
required: false
multivalued: true

```
</details>