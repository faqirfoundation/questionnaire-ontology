

# Slot: questionnaireLastUpdated 


_The date and time when the questionnaire was last updated._





URI: [https://w3id.org/faqir/datamodel/questionnaireLastUpdated](https://w3id.org/faqir/datamodel/questionnaireLastUpdated)
Alias: questionnaireLastUpdated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/questionnaireLastUpdated |
| native | https://w3id.org/faqir/datamodel/questionnaireLastUpdated |
| undefined | fhir:Questionnaire.date |




## LinkML Source

<details>
```yaml
name: questionnaireLastUpdated
description: The date and time when the questionnaire was last updated.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.date
rank: 1000
alias: questionnaireLastUpdated
owner: Questionnaire
domain_of:
- Questionnaire
range: datetime
required: true

```
</details>