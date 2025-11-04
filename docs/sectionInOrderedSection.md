

# Slot: sectionInOrderedSection 


_OrderedSections that this Section is indexed in._





URI: [faqir:sectionInOrderedSection](https://faqir.org/datamodel/sectionInOrderedSection)
Alias: sectionInOrderedSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A section of questions in the questionnaire |  no  |







## Properties

* Range: [OrderedSection](OrderedSection.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:sectionInOrderedSection |
| native | https://w3id.org/faqir/datamodel/sectionInOrderedSection |




## LinkML Source

<details>
```yaml
name: sectionInOrderedSection
description: OrderedSections that this Section is indexed in.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Section
slot_uri: faqir:sectionInOrderedSection
alias: sectionInOrderedSection
domain_of:
- Section
inverse: orderedSectionHasSection
range: OrderedSection
required: false
multivalued: true

```
</details>