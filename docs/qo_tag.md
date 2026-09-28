

# Slot: qo_tag 


_Internal English identifier, e.g., 'q_pain_level'._





URI: [qo:tag](https://ns.faqir.org/q-o#tag)
Alias: qo_tag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestion](QoQuestion.md) | A question |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:tag |
| native | qo:qo_tag |




## LinkML Source

<details>
```yaml
name: qo_tag
description: Internal English identifier, e.g., 'q_pain_level'.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:tag
alias: qo_tag
owner: qo_Question
domain_of:
- qo_Question
range: string
required: true
multivalued: true

```
</details>