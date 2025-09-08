

# Slot: organizationAuthorsQuestionnaire 


_Questionnaire created by this organization._





URI: [faqir:organizationAuthorsQuestionnaire](https://faqir.org/datamodel/organizationAuthorsQuestionnaire)
Alias: organizationAuthorsQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An entity acting in a healthcare context |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:organizationAuthorsQuestionnaire |
| native | https://w3id.org/faqir/datamodel/organizationAuthorsQuestionnaire |
| undefined | prov:wasAssociatedWith |




## LinkML Source

<details>
```yaml
name: organizationAuthorsQuestionnaire
description: Questionnaire created by this organization.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- prov:wasAssociatedWith
rank: 1000
domain: Organization
slot_uri: faqir:organizationAuthorsQuestionnaire
alias: organizationAuthorsQuestionnaire
domain_of:
- Organization
inverse: questionnaireAuthoredByOrg
range: Questionnaire
required: false
multivalued: true

```
</details>