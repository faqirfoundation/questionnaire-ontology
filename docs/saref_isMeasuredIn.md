

# Slot: saref_isMeasuredIn 


_A relationship identifying the unit of measure used for a certain entity._





URI: [saref:isMeasuredIn](https://saref.etsi.org/core/isMeasuredIn)
Alias: saref_isMeasuredIn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeDuration](TimeDuration.md) | Duration of a temporal extent expressed as a decimal number scaled by a tempo... |  no  |
| [QuantityValue](QuantityValue.md) | A measured amount (or an amount that can potentially be measured) |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^ucum`





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | saref:isMeasuredIn |
| native | qo:saref_isMeasuredIn |




## LinkML Source

<details>
```yaml
name: saref_isMeasuredIn
description: A relationship identifying the unit of measure used for a certain entity.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: saref:isMeasuredIn
alias: saref_isMeasuredIn
domain_of:
- QuantityValue
- time_Duration
range: uriorcurie
required: false
multivalued: false
pattern: ^ucum

```
</details>