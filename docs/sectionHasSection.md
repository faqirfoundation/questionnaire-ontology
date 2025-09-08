

# Slot: sectionHasSection 


_The Section that is part of this Section._





URI: [datamodel:sectionHasSection](https://w3id.org/faqir/datamodel/sectionHasSection)
Alias: sectionHasSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A section of questions in the questionnaire |  no  |







## Properties

* Range: [Section](Section.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:sectionHasSection |
| native | https://w3id.org/faqir/datamodel/sectionHasSection |
| undefined | fhir:Questionnaire.item.where(type='group') |




## LinkML Source

<details>
```yaml
name: sectionHasSection
description: The Section that is part of this Section.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='group')
rank: 1000
domain: Section
slot_uri: datamodel:sectionHasSection
alias: sectionHasSection
domain_of:
- Section
inverse: sectionPartOfSection
range: Section
required: false
multivalued: true

```
</details>