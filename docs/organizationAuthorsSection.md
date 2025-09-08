

# Slot: organizationAuthorsSection 


_Section created by this organization._





URI: [faqir:organizationAuthorsSection](https://faqir.org/datamodel/organizationAuthorsSection)
Alias: organizationAuthorsSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An entity acting in a healthcare context |  no  |







## Properties

* Range: [Section](Section.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:organizationAuthorsSection |
| native | https://w3id.org/faqir/datamodel/organizationAuthorsSection |
| undefined | prov:wasAssociatedWith |




## LinkML Source

<details>
```yaml
name: organizationAuthorsSection
description: Section created by this organization.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- prov:wasAssociatedWith
rank: 1000
domain: Organization
slot_uri: faqir:organizationAuthorsSection
alias: organizationAuthorsSection
domain_of:
- Organization
inverse: sectionAuthoredByOrg
range: Section
required: false
multivalued: true

```
</details>