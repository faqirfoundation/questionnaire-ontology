

# Slot: sectionHasOrderedSection 


_The Section that is part of this Section._





URI: [faqir:sectionHasOrderedSection](https://faqir.org/datamodel/sectionHasOrderedSection)
Alias: sectionHasOrderedSection

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
| self | faqir:sectionHasOrderedSection |
| native | https://w3id.org/faqir/datamodel/sectionHasOrderedSection |
| undefined | fhir:Questionnaire.item.where(type='group') |




## LinkML Source

<details>
```yaml
name: sectionHasOrderedSection
description: The Section that is part of this Section.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='group')
rank: 1000
domain: Section
slot_uri: faqir:sectionHasOrderedSection
alias: sectionHasOrderedSection
domain_of:
- Section
inverse: orderedSectionPartOfSection
range: OrderedSection
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>