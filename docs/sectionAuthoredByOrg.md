

# Slot: sectionAuthoredByOrg 


_The Organization that has created this Section._





URI: [faqir:sectionAuthoredByOrg](https://faqir.org/datamodel/sectionAuthoredByOrg)
Alias: sectionAuthoredByOrg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A section of questions in the questionnaire |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:sectionAuthoredByOrg |
| native | https://w3id.org/faqir/datamodel/sectionAuthoredByOrg |
| undefined | fhir:Questionnaire.author |




## LinkML Source

<details>
```yaml
name: sectionAuthoredByOrg
description: The Organization that has created this Section.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.author
rank: 1000
domain: Section
slot_uri: faqir:sectionAuthoredByOrg
alias: sectionAuthoredByOrg
domain_of:
- Section
inverse: organizationAuthorsSection
range: Organization
required: false
multivalued: true

```
</details>