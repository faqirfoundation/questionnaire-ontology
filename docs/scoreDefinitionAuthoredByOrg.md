

# Slot: scoreDefinitionAuthoredByOrg 


_The Organization that has created this ScoreDefinition._





URI: [faqir:scoreDefinitionAuthoredByOrg](https://faqir.org/datamodel/scoreDefinitionAuthoredByOrg)
Alias: scoreDefinitionAuthoredByOrg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreDefinition](ScoreDefinition.md) | A score calculated from questions |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreDefinitionAuthoredByOrg |
| native | https://w3id.org/faqir/datamodel/scoreDefinitionAuthoredByOrg |
| undefined | fhir:Questionnaire.author |




## LinkML Source

<details>
```yaml
name: scoreDefinitionAuthoredByOrg
description: The Organization that has created this ScoreDefinition.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.author
rank: 1000
domain: ScoreDefinition
slot_uri: faqir:scoreDefinitionAuthoredByOrg
alias: scoreDefinitionAuthoredByOrg
domain_of:
- ScoreDefinition
inverse: organizationAuthorsScoreDefinition
range: Organization
required: false
multivalued: true

```
</details>