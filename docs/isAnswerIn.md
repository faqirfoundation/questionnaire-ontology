

# Slot: isAnswerIn 


_The QuestionnaireResponse that this Answer is part of._





URI: [datamodel:isAnswerIn](https://w3id.org/faqir/datamodel/isAnswerIn)
Alias: isAnswerIn

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
| self | datamodel:isAnswerIn |
| native | https://w3id.org/faqir/datamodel/isAnswerIn |
| undefined | fhir:QuestionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: isAnswerIn
description: The QuestionnaireResponse that this Answer is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer
rank: 1000
domain: Answer
slot_uri: datamodel:isAnswerIn
alias: isAnswerIn
domain_of:
- Answer
inverse: hasResponseAnswer
range: QuestionnaireResponse
required: true
multivalued: false

```
</details>