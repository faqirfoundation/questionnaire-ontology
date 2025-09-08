

# Slot: questionUsedInScoreDefinition 


_The ScoreDefinition that this Question is used in._





URI: [faqir:questionUsedInScoreDefinition](https://faqir.org/datamodel/questionUsedInScoreDefinition)
Alias: questionUsedInScoreDefinition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [ScoreDefinition](ScoreDefinition.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionUsedInScoreDefinition |
| native | https://w3id.org/faqir/datamodel/questionUsedInScoreDefinition |




## LinkML Source

<details>
```yaml
name: questionUsedInScoreDefinition
description: The ScoreDefinition that this Question is used in.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Question
slot_uri: faqir:questionUsedInScoreDefinition
alias: questionUsedInScoreDefinition
domain_of:
- Question
inverse: scoreDefinitionUsesQuestion
range: ScoreDefinition
required: false
multivalued: true

```
</details>