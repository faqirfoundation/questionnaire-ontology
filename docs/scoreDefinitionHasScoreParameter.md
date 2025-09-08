

# Slot: scoreDefinitionHasScoreParameter 


_The ScoreParameter that is required for this ScoreDefinition._





URI: [faqir:scoreDefinitionHasScoreParameter](https://faqir.org/datamodel/scoreDefinitionHasScoreParameter)
Alias: scoreDefinitionHasScoreParameter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreDefinition](ScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [ScoreParameter](ScoreParameter.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreDefinitionHasScoreParameter |
| native | https://w3id.org/faqir/datamodel/scoreDefinitionHasScoreParameter |




## LinkML Source

<details>
```yaml
name: scoreDefinitionHasScoreParameter
description: The ScoreParameter that is required for this ScoreDefinition.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: ScoreDefinition
slot_uri: faqir:scoreDefinitionHasScoreParameter
alias: scoreDefinitionHasScoreParameter
domain_of:
- ScoreDefinition
inverse: scoreParameterPartOfScoreDefinition
range: ScoreParameter
required: false
multivalued: true

```
</details>