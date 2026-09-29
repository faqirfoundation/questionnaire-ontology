

# Slot: qo_hardValidity 


_Specifies the operational enforcement mechanism of a duration limit; when true, expiration acts as a strict invalidation threshold for re-use, whereas when false, it serves as a non-binding recommendation._





URI: [qo:hardValidity](https://ns.faqir.org/q-o#hardValidity)
Alias: qo_hardValidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:hardValidity |
| native | qo:qo_hardValidity |




## LinkML Source

<details>
```yaml
name: qo_hardValidity
description: Specifies the operational enforcement mechanism of a duration limit;
  when true, expiration acts as a strict invalidation threshold for re-use, whereas
  when false, it serves as a non-binding recommendation.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:hardValidity
ifabsent: 'False'
alias: qo_hardValidity
domain_of:
- qo_OrderedQuestion
range: boolean
required: false

```
</details>