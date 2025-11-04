

# Slot: scoreDefinitionUsesQuestion 


_The Question(s) that this ScoreDefinition is based on._





URI: [faqir:scoreDefinitionUsesQuestion](https://faqir.org/datamodel/scoreDefinitionUsesQuestion)
Alias: scoreDefinitionUsesQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreDefinition](ScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [Question](Question.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreDefinitionUsesQuestion |
| native | https://w3id.org/faqir/datamodel/scoreDefinitionUsesQuestion |




## LinkML Source

<details>
```yaml
name: scoreDefinitionUsesQuestion
description: The Question(s) that this ScoreDefinition is based on.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: ScoreDefinition
slot_uri: faqir:scoreDefinitionUsesQuestion
alias: scoreDefinitionUsesQuestion
domain_of:
- ScoreDefinition
inverse: questionUsedInScoreDefinition
range: Question
required: true
multivalued: true

```
</details>