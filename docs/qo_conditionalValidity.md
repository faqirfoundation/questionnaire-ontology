

# Slot: qo_conditionalValidity 


_A machine-readable rule statement defining an intervening event or state change that revokes the validity of a recorded observation prior to its natural temporal expiration._





URI: [qo:conditionalValidity](https://ns.faqir.org/q-o#conditionalValidity)
Alias: qo_conditionalValidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





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
- qo_OrderedQuestion
range: string
required: true

```
</details>