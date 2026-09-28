

# Slot: qo_categories 


_Categories for categorical scores._





URI: [qo:categories](https://ns.faqir.org/q-o#categories)
Alias: qo_categories

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoScoreDefinition](QoScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:categories |
| native | qo:qo_categories |




## LinkML Source

<details>
```yaml
name: qo_categories
description: Categories for categorical scores.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:categories
alias: qo_categories
owner: qo_ScoreDefinition
domain_of:
- qo_ScoreDefinition
range: string
required: false
multivalued: true

```
</details>