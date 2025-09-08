

# Slot: answerInResponse 


_The QuestionnaireResponse that this Answer is part of._





URI: [datamodel:answerInResponse](https://w3id.org/faqir/datamodel/answerInResponse)
Alias: answerInResponse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [QuestionnaireResponse](QuestionnaireResponse.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:answerInResponse |
| native | https://w3id.org/faqir/datamodel/answerInResponse |
| undefined | fhir:QuestionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: answerInResponse
description: The QuestionnaireResponse that this Answer is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer
rank: 1000
domain: Answer
slot_uri: datamodel:answerInResponse
alias: answerInResponse
domain_of:
- Answer
inverse: responseHasAnswer
range: QuestionnaireResponse
required: true
multivalued: false

```
</details>