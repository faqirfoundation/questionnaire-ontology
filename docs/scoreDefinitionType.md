

# Slot: scoreDefinitionType 


_Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values._





URI: [faqir:scoreDefinitionType](https://faqir.org/datamodel/scoreDefinitionType)
Alias: scoreDefinitionType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreDefinition](ScoreDefinition.md) | A score calculated from questions |  no  |
| [ScoreValue](ScoreValue.md) | The score value calculated from a QuestionnaireResponse following a ScoreDefi... |  no  |







## Properties

* Range: [ScoreType](ScoreType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreDefinitionType |
| native | https://w3id.org/faqir/datamodel/scoreDefinitionType |




## LinkML Source

<details>
```yaml
name: scoreDefinitionType
description: 'Type of score: numerical_continuous, numerical_integer, numerical_percentage,
  numerical_z_score, numerical_t_score or categorical. Determines valid score values.'
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
slot_uri: faqir:scoreDefinitionType
alias: scoreDefinitionType
domain_of:
- ScoreDefinition
- ScoreValue
range: ScoreType
required: true

```
</details>