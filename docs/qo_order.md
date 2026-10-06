

# Slot: qo_order 


_An integer specifying the sequence or display arrangement (1-based index) of an item within a container._





URI: [qo:order](https://ns.faqir.org/q-o#order)
Alias: qo_order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  yes  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  yes  |







## Properties

* Range: [Integer](Integer.md)

* Required: True

* Minimum Value: 1





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:order |
| native | qo:qo_order |




## LinkML Source

<details>
```yaml
name: qo_order
description: An integer specifying the sequence or display arrangement (1-based index)
  of an item within a container.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:order
alias: qo_order
domain_of:
- qo_OrderedSection
- qo_OrderedQuestion
range: integer
required: true
minimum_value: 1

```
</details>