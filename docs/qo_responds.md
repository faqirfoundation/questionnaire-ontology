

# Slot: qo_responds 


_The Questionnaire that this QuestionnaireResponse is for._





URI: [qo:responds](https://ns.faqir.org/q-o#responds)
Alias: qo_responds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [QoQuestionnaire](QoQuestionnaire.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:responds |
| native | qo:qo_responds |
| narrow | fhir:questionnaireResponse.questionnaire |




## LinkML Source

<details>
```yaml
name: qo_responds
description: The Questionnaire that this QuestionnaireResponse is for.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:questionnaireResponse.questionnaire
rank: 1000
domain: qo_QuestionnaireResponse
slot_uri: qo:responds
alias: qo_responds
domain_of:
- qo_QuestionnaireResponse
range: qo_Questionnaire
required: true
multivalued: false

```
</details>