

# Slot: qo_order 


_Position in the questionnaire or section (1-based index)._





URI: [qo:order](https://ns.faqir.org/q-o#order)
Alias: qo_order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedSection](QoOrderedSection.md) | Section's position within a specific questionnaire or section |  yes  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  yes  |







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
description: Position in the questionnaire or section (1-based index).
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