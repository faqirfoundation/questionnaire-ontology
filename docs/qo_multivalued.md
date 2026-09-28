

# Slot: qo_multivalued 


_Indicates whether this question allows multiple answers (true) or it's single answer (false)._





URI: [qo:multivalued](https://ns.faqir.org/q-o#multivalued)
Alias: qo_multivalued

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | A question |  no  |







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
description: Indicates whether this question allows multiple answers (true) or it's
  single answer (false).
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