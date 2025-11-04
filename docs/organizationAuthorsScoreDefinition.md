

# Slot: organizationAuthorsScoreDefinition 


_Score definition created by this organization._





URI: [faqir:organizationAuthorsScoreDefinition](https://faqir.org/datamodel/organizationAuthorsScoreDefinition)
Alias: organizationAuthorsScoreDefinition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An entity acting in a healthcare context |  no  |







## Properties

* Range: [ScoreDefinition](ScoreDefinition.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:organizationAuthorsScoreDefinition |
| native | https://w3id.org/faqir/datamodel/organizationAuthorsScoreDefinition |
| undefined | prov:wasAssociatedWith |




## LinkML Source

<details>
```yaml
name: organizationAuthorsScoreDefinition
description: Score definition created by this organization.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- prov:wasAssociatedWith
rank: 1000
domain: Organization
slot_uri: faqir:organizationAuthorsScoreDefinition
alias: organizationAuthorsScoreDefinition
domain_of:
- Organization
inverse: scoreDefinitionAuthoredByOrg
range: ScoreDefinition
required: false
multivalued: true

```
</details>