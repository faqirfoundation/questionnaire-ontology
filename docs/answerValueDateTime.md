

# Slot: answerValueDateTime 


_The value of the answer to a dateTime type of question, which is a datetime value._





URI: [https://w3id.org/faqir/datamodel/answerValueDateTime](https://w3id.org/faqir/datamodel/answerValueDateTime)
Alias: answerValueDateTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [ValueDateTime](ValueDateTime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/answerValueDateTime |
| native | https://w3id.org/faqir/datamodel/answerValueDateTime |
| undefined | fhir:QuestionnaireResponse.item.answer.valueDateTime |




## LinkML Source

<details>
```yaml
name: answerValueDateTime
description: The value of the answer to a dateTime type of question, which is a datetime
  value.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer.valueDateTime
rank: 1000
alias: answerValueDateTime
owner: Answer
domain_of:
- Answer
range: ValueDateTime
required: false
multivalued: false

```
</details>