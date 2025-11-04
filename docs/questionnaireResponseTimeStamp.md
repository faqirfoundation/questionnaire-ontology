

# Slot: questionnaireResponseTimeStamp 


_The date and time when the questionnaire response was created (when the questionnaire starts to be answered, not when it's finished)._





URI: [https://w3id.org/faqir/datamodel/questionnaireResponseTimeStamp](https://w3id.org/faqir/datamodel/questionnaireResponseTimeStamp)
Alias: questionnaireResponseTimeStamp

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
| self | https://w3id.org/faqir/datamodel/questionnaireResponseTimeStamp |
| native | https://w3id.org/faqir/datamodel/questionnaireResponseTimeStamp |
| undefined | fhir:QuestionnaireResponse.authored |




## LinkML Source

<details>
```yaml
name: questionnaireResponseTimeStamp
description: The date and time when the questionnaire response was created (when the
  questionnaire starts to be answered, not when it's finished).
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.authored
rank: 1000
alias: questionnaireResponseTimeStamp
owner: QuestionnaireResponse
domain_of:
- QuestionnaireResponse
range: datetime
required: true

```
</details>