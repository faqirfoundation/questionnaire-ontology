

# Slot: toQuestion 


_The Question that this Answer is for._





URI: [datamodel:toQuestion](https://w3id.org/faqir/datamodel/toQuestion)
Alias: toQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [Question](Question.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:toQuestion |
| native | https://w3id.org/faqir/datamodel/toQuestion |
| undefined | fhir:QuestionnaireResponse.item.answer.question |




## LinkML Source

<details>
```yaml
name: toQuestion
description: The Question that this Answer is for.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer.question
rank: 1000
domain: Answer
slot_uri: datamodel:toQuestion
alias: toQuestion
domain_of:
- Answer
inverse: hasAnswer
range: Question
required: true
multivalued: false

```
</details>