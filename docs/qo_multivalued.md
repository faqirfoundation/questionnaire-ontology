

# Slot: qo_multivalued 


_Indicates whether this question allows more than one answer (true) or only one (false)._





URI: [qo:multivalued](https://ns.faqir.org/q-o#multivalued)
Alias: qo_multivalued

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:multivalued |
| native | qo:qo_multivalued |




## LinkML Source

<details>
```yaml
name: qo_multivalued
description: Indicates whether this question allows more than one answer (true) or
  only one (false).
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:multivalued
ifabsent: 'False'
alias: qo_multivalued
domain_of:
- qo_Question
range: boolean

```
</details>