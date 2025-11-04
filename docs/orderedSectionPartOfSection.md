

# Slot: orderedSectionPartOfSection 


_The Section that this Section is part of in the specified order._





URI: [faqir:orderedSectionPartOfSection](https://faqir.org/datamodel/orderedSectionPartOfSection)
Alias: orderedSectionPartOfSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedSection](OrderedSection.md) | Section's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Section](Section.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:orderedSectionPartOfSection |
| native | https://w3id.org/faqir/datamodel/orderedSectionPartOfSection |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: orderedSectionPartOfSection
description: The Section that this Section is part of in the specified order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: OrderedSection
slot_uri: faqir:orderedSectionPartOfSection
alias: orderedSectionPartOfSection
domain_of:
- OrderedSection
inverse: sectionHasOrderedSection
range: Section
required: false
multivalued: false

```
</details>