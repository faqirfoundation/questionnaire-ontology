

# Slot: scoreValueBasedOnScoreDefinition 


_The ScoreDefinition that this ScoreValue is based on._





URI: [faqir:scoreValueBasedOnScoreDefinition](https://faqir.org/datamodel/scoreValueBasedOnScoreDefinition)
Alias: scoreValueBasedOnScoreDefinition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreValue](ScoreValue.md) | The score value calculated from a QuestionnaireResponse following a ScoreDefi... |  no  |







## Properties

* Range: [ScoreDefinition](ScoreDefinition.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreValueBasedOnScoreDefinition |
| native | https://w3id.org/faqir/datamodel/scoreValueBasedOnScoreDefinition |




## LinkML Source

<details>
```yaml
name: scoreValueBasedOnScoreDefinition
description: The ScoreDefinition that this ScoreValue is based on.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: ScoreValue
slot_uri: faqir:scoreValueBasedOnScoreDefinition
alias: scoreValueBasedOnScoreDefinition
domain_of:
- ScoreValue
inverse: scoreDefinitionHasScoreValue
range: ScoreDefinition
required: true
multivalued: false

```
</details>