

# Slot: sectionPartOfSection 


_The Section that this Section is part of._





URI: [datamodel:sectionPartOfSection](https://w3id.org/faqir/datamodel/sectionPartOfSection)
Alias: sectionPartOfSection

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
| self | datamodel:sectionPartOfSection |
| native | https://w3id.org/faqir/datamodel/sectionPartOfSection |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: sectionPartOfSection
description: The Section that this Section is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: Section
slot_uri: datamodel:sectionPartOfSection
alias: sectionPartOfSection
domain_of:
- Section
inverse: sectionHasSection
range: Section
required: false
multivalued: true

```
</details>