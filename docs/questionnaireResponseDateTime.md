

# Slot: questionnaireResponseDateTime 


_The date and time when the questionnaire response was created or last updated._





URI: [datamodel:questionnaireResponseDateTime](https://w3id.org/faqir/datamodel/questionnaireResponseDateTime)
Alias: questionnaireResponseDateTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:questionnaireResponseDateTime |
| native | https://w3id.org/faqir/datamodel/questionnaireResponseDateTime |
| undefined | fhir:QuestionnaireResponse.authored |




## LinkML Source

<details>
```yaml
name: questionnaireResponseDateTime
description: The date and time when the questionnaire response was created or last
  updated.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.authored
rank: 1000
slot_uri: datamodel:questionnaireResponseDateTime
alias: questionnaireResponseDateTime
domain_of:
- QuestionnaireResponse
range: datetime
required: true

```
</details>