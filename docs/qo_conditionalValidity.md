

# Slot: qo_conditionalValidity 


_A machine-readable rule statement defining an intervening event or state change that revokes the validity of a recorded observation prior to its natural temporal expiration._





URI: [qo:conditionalValidity](https://ns.faqir.org/q-o#conditionalValidity)
Alias: qo_conditionalValidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:conditionalValidity |
| native | qo:qo_conditionalValidity |




## LinkML Source

<details>
```yaml
name: qo_conditionalValidity
description: A machine-readable rule statement defining an intervening event or state
  change that revokes the validity of a recorded observation prior to its natural
  temporal expiration.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:conditionalValidity
alias: qo_conditionalValidity
domain_of:
- qo_Questionnaire
- qo_OrderedSection
- qo_Section
- qo_OrderedQuestion
- qo_Question
range: string
required: false

```
</details>