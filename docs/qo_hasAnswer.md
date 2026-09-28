

# Slot: qo_hasAnswer 


_The Answer that is part of this QuestionnaireResponse._





URI: [qo:hasAnswer](https://ns.faqir.org/q-o#hasAnswer)
Alias: qo_hasAnswer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [QoAnswer](QoAnswer.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:hasAnswer |
| native | qo:qo_hasAnswer |
| narrow | fhir:questionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: qo_hasAnswer
description: The Answer that is part of this QuestionnaireResponse.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:questionnaireResponse.item.answer
rank: 1000
domain: qo_QuestionnaireResponse
slot_uri: qo:hasAnswer
alias: qo_hasAnswer
domain_of:
- qo_QuestionnaireResponse
range: qo_Answer
required: true
multivalued: true

```
</details>