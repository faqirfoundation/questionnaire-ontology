

# Slot: responseToQuestionnaire 


_The Questionnaire that this QuestionnaireResponse is for._





URI: [datamodel:responseToQuestionnaire](https://w3id.org/faqir/datamodel/responseToQuestionnaire)
Alias: responseToQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:responseToQuestionnaire |
| native | https://w3id.org/faqir/datamodel/responseToQuestionnaire |
| undefined | fhir:QuestionnaireResponse.questionnaire |




## LinkML Source

<details>
```yaml
name: responseToQuestionnaire
description: The Questionnaire that this QuestionnaireResponse is for.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.questionnaire
rank: 1000
domain: QuestionnaireResponse
slot_uri: datamodel:responseToQuestionnaire
alias: responseToQuestionnaire
domain_of:
- QuestionnaireResponse
inverse: questionnaireHasResponse
range: Questionnaire
required: true
multivalued: false

```
</details>