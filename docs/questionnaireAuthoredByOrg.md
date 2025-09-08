

# Slot: questionnaireAuthoredByOrg 


_The Organization that has created this Questionnaire._





URI: [faqir:questionnaireAuthoredByOrg](https://faqir.org/datamodel/questionnaireAuthoredByOrg)
Alias: questionnaireAuthoredByOrg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnaireAuthoredByOrg |
| native | https://w3id.org/faqir/datamodel/questionnaireAuthoredByOrg |
| undefined | fhir:Questionnaire.author |




## LinkML Source

<details>
```yaml
name: questionnaireAuthoredByOrg
description: The Organization that has created this Questionnaire.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.author
rank: 1000
domain: Questionnaire
slot_uri: faqir:questionnaireAuthoredByOrg
alias: questionnaireAuthoredByOrg
domain_of:
- Questionnaire
inverse: organizationAuthorsQuestionnaire
range: Organization
required: false
multivalued: true

```
</details>