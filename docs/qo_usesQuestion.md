

# Slot: qo_usesQuestion 


_The Question(s) that this ScoreDefinition is based on._





URI: [qo:usesQuestion](https://ns.faqir.org/q-o#usesQuestion)
Alias: qo_usesQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoScoreDefinition](QoScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [QoQuestion](QoQuestion.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:usesQuestion |
| native | qo:qo_usesQuestion |




## LinkML Source

<details>
```yaml
name: qo_usesQuestion
description: The Question(s) that this ScoreDefinition is based on.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: qo_ScoreDefinition
slot_uri: qo:usesQuestion
alias: qo_usesQuestion
domain_of:
- qo_ScoreDefinition
range: qo_Question
required: true
multivalued: true

```
</details>