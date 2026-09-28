

# Slot: qo_answers 


_The Question that this Answer is for._





URI: [qo:answers](https://ns.faqir.org/q-o#answers)
Alias: qo_answers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoAnswer](QoAnswer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [QoQuestion](QoQuestion.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:answers |
| native | qo:qo_answers |
| undefined | fhir:QuestionnaireResponse.item.answer.question |




## LinkML Source

<details>
```yaml
name: qo_answers
description: The Question that this Answer is for.
from_schema: https://ns.faqir.org/q-o
mappings:
- fhir:QuestionnaireResponse.item.answer.question
rank: 1000
domain: qo_Answer
slot_uri: qo:answers
alias: qo_answers
domain_of:
- qo_Answer
range: qo_Question
required: true
multivalued: false

```
</details>