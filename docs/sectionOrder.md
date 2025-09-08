

# Slot: sectionOrder 


_Section position in the questionnaire or section (1-based index)._





URI: [https://w3id.org/faqir/datamodel/sectionOrder](https://w3id.org/faqir/datamodel/sectionOrder)
Alias: sectionOrder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedSection](OrderedSection.md) | Section's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True

* Minimum Value: 1





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/sectionOrder |
| native | https://w3id.org/faqir/datamodel/sectionOrder |




## LinkML Source

<details>
```yaml
name: sectionOrder
description: Section position in the questionnaire or section (1-based index).
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: sectionOrder
owner: OrderedSection
domain_of:
- OrderedSection
range: integer
required: true
minimum_value: 1

```
</details>