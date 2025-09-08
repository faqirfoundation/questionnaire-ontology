

# Slot: organizationAuthorsQuestion 


_Question created by this organization._





URI: [faqir:organizationAuthorsQuestion](https://faqir.org/datamodel/organizationAuthorsQuestion)
Alias: organizationAuthorsQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An entity acting in a healthcare context |  no  |







## Properties

* Range: [Question](Question.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:organizationAuthorsQuestion |
| native | https://w3id.org/faqir/datamodel/organizationAuthorsQuestion |
| undefined | prov:wasAssociatedWith |




## LinkML Source

<details>
```yaml
name: organizationAuthorsQuestion
description: Question created by this organization.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- prov:wasAssociatedWith
rank: 1000
domain: Organization
slot_uri: faqir:organizationAuthorsQuestion
alias: organizationAuthorsQuestion
domain_of:
- Organization
inverse: questionAuthoredByOrg
range: Question
required: false
multivalued: true

```
</details>