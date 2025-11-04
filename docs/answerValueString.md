

# Slot: answerValueString 


_The value of the answer to a choice, openChoice or text type of question, which is a stringValue._





URI: [https://w3id.org/faqir/datamodel/answerValueString](https://w3id.org/faqir/datamodel/answerValueString)
Alias: answerValueString

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [ValueString](ValueString.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/answerValueString |
| native | https://w3id.org/faqir/datamodel/answerValueString |
| undefined | fhir:QuestionnaireResponse.item.answer.valueString |




## LinkML Source

<details>
```yaml
name: answerValueString
description: The value of the answer to a choice, openChoice or text type of question,
  which is a stringValue.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer.valueString
rank: 1000
alias: answerValueString
owner: Answer
domain_of:
- Answer
range: ValueString
required: false
multivalued: true

```
</details>