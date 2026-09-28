

# Slot: qo_answerValue 


_The value of the answer to: a decimal or numberInterval type of question, which is a numeric value; a choice, openChoice or text type of question, which is a stringValue; dateTime type of question, which is a datetime value._





URI: [qo:answerValue](https://ns.faqir.org/q-o#answerValue)
Alias: qo_answerValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoAnswer](QoAnswer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [String](String.md)&nbsp;or&nbsp;<br />[Float](Float.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:answerValue |
| native | qo:qo_answerValue |
| narrow | fhir:QuestionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: qo_answerValue
description: 'The value of the answer to: a decimal or numberInterval type of question,
  which is a numeric value; a choice, openChoice or text type of question, which is
  a stringValue; dateTime type of question, which is a datetime value.'
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:QuestionnaireResponse.item.answer
rank: 1000
slot_uri: qo:answerValue
alias: qo_answerValue
owner: qo_Answer
domain_of:
- qo_Answer
range: string
required: false
multivalued: false
any_of:
- range: float
- range: string
- range: datetime

```
</details>