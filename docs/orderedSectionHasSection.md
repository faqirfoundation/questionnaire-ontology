

# Slot: orderedSectionHasSection 


_Section indexed in this OrderedSection._





URI: [faqir:orderedSectionHasSection](https://faqir.org/datamodel/orderedSectionHasSection)
Alias: orderedSectionHasSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedSection](OrderedSection.md) | Section's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Section](Section.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:orderedSectionHasSection |
| native | https://w3id.org/faqir/datamodel/orderedSectionHasSection |




## LinkML Source

<details>
```yaml
name: orderedSectionHasSection
description: Section indexed in this OrderedSection.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: OrderedSection
slot_uri: faqir:orderedSectionHasSection
alias: orderedSectionHasSection
domain_of:
- OrderedSection
inverse: sectionInOrderedSection
range: Section
required: true
multivalued: false

```
</details>