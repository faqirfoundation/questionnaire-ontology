

# Slot: qo_codingParams 


_Defines the permissible standardized concept codes and human-readable labels available for selection._





URI: [qo:codingParams](https://ns.faqir.org/q-o#codingParams)
Alias: qo_codingParams

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |







## Properties

* Range: [ValueCoding](ValueCoding.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:codingParams |
| native | qo:qo_codingParams |




## LinkML Source

<details>
```yaml
name: qo_codingParams
description: Defines the permissible standardized concept codes and human-readable
  labels available for selection.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:codingParams
alias: qo_codingParams
owner: qo_Question
domain_of:
- qo_Question
range: ValueCoding
required: false
multivalued: true

```
</details>