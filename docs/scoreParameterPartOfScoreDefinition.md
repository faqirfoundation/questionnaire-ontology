

# Slot: scoreParameterPartOfScoreDefinition 


_The ScoreDefinition(s) that this ScoreParameter is part of._





URI: [faqir:scoreParameterPartOfScoreDefinition](https://faqir.org/datamodel/scoreParameterPartOfScoreDefinition)
Alias: scoreParameterPartOfScoreDefinition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreParameter](ScoreParameter.md) | Parameters for score definitions, such as min/max values, categories or const... |  no  |







## Properties

* Range: [ScoreDefinition](ScoreDefinition.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreParameterPartOfScoreDefinition |
| native | https://w3id.org/faqir/datamodel/scoreParameterPartOfScoreDefinition |




## LinkML Source

<details>
```yaml
name: scoreParameterPartOfScoreDefinition
description: The ScoreDefinition(s) that this ScoreParameter is part of.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: ScoreParameter
slot_uri: faqir:scoreParameterPartOfScoreDefinition
alias: scoreParameterPartOfScoreDefinition
domain_of:
- ScoreParameter
inverse: scoreDefinitionHasScoreParameter
range: ScoreDefinition
required: true
multivalued: false

```
</details>