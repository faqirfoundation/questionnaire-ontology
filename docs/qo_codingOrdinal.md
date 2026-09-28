

# Slot: qo_codingOrdinal 


_Indicates if the choices in a choice or open-choice question are ordered (true) or unordered (false, categorical)._





URI: [qo:codingOrdinal](https://ns.faqir.org/q-o#codingOrdinal)
Alias: qo_codingOrdinal

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
| self | qo:codingOrdinal |
| native | qo:qo_codingOrdinal |




## LinkML Source

<details>
```yaml
name: qo_codingOrdinal
description: Indicates if the choices in a choice or open-choice question are ordered
  (true) or unordered (false, categorical).
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:codingOrdinal
ifabsent: 'False'
alias: qo_codingOrdinal
owner: qo_Question
domain_of:
- qo_Question
range: boolean

```
</details>