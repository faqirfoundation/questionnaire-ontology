

# Slot: qo_hasAnswer 


_Associates a recorded instance with its constituent individual response values._





URI: [qo:hasAnswer](https://ns.faqir.org/q-o#hasAnswer)
Alias: qo_hasAnswer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  no  |







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
| narrow | fhir:QuestionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: qo_hasAnswer
description: Associates a recorded instance with its constituent individual response
  values.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:QuestionnaireResponse.item.answer
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