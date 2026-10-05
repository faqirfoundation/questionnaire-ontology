

# Slot: qo_toQuestion 


_Links a recorded response value back to its originating inquiry item definition._





URI: [qo:toQuestion](https://ns.faqir.org/q-o#toQuestion)
Alias: qo_toQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |






## Properties

* Range: [QoQuestion](QoQuestion.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:toQuestion |
| native | qo:qo_toQuestion |
| narrow | fhir:QuestionnaireResponse.item.answer.question |




## LinkML Source

<details>
```yaml
name: qo_toQuestion
description: Links a recorded response value back to its originating inquiry item
  definition.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:QuestionnaireResponse.item.answer.question
rank: 1000
domain: qo_Answer
slot_uri: qo:toQuestion
alias: qo_toQuestion
domain_of:
- qo_Answer
range: qo_Question
required: true
multivalued: false

```
</details>