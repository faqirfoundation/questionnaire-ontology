

# Slot: qo_conditionalValidity 


_a condition (expressed in a machine-readable rule language) that would invalidate the answer earlier than the temporal duration, e.g., 'a documented smoking cessation intervention' invalidates the answer to 'Do you smoke?''._





URI: [qo:conditionalValidity](https://ns.faqir.org/q-o#conditionalValidity)
Alias: qo_conditionalValidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:conditionalValidity |
| native | qo:qo_conditionalValidity |




## LinkML Source

<details>
```yaml
name: qo_conditionalValidity
description: a condition (expressed in a machine-readable rule language) that would
  invalidate the answer earlier than the temporal duration, e.g., 'a documented smoking
  cessation intervention' invalidates the answer to 'Do you smoke?''.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:conditionalValidity
alias: qo_conditionalValidity
domain_of:
- qo_OrderedQuestion
range: string
required: true

```
</details>