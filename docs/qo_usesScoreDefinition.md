

# Slot: qo_usesScoreDefinition 


_The ScoreDefinition that is applied in this Questionnaire._





URI: [qo:usesScoreDefinition](https://ns.faqir.org/q-o#usesScoreDefinition)
Alias: qo_usesScoreDefinition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  yes  |
| [QoQuestionnaire](QoQuestionnaire.md) | A questionnaire that can be answered (collection of questions) |  yes  |







## Properties

* Range: [QoScoreDefinition](QoScoreDefinition.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:usesScoreDefinition |
| native | qo:qo_usesScoreDefinition |




## LinkML Source

<details>
```yaml
name: qo_usesScoreDefinition
description: The ScoreDefinition that is applied in this Questionnaire.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:usesScoreDefinition
alias: qo_usesScoreDefinition
domain_of:
- qo_Questionnaire
- qo_Section
range: qo_ScoreDefinition
required: false
multivalued: true

```
</details>