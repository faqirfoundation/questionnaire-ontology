

# Slot: answerValueNumerical 


_The value of the answer to a decimal or numberInterval type of question, which is a numeric value._





URI: [https://w3id.org/faqir/datamodel/answerValueNumerical](https://w3id.org/faqir/datamodel/answerValueNumerical)
Alias: answerValueNumerical

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [ValueNumerical](ValueNumerical.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/answerValueNumerical |
| native | https://w3id.org/faqir/datamodel/answerValueNumerical |
| undefined | fhir:QuestionnaireResponse.item.answer.valueDecimal |




## LinkML Source

<details>
```yaml
name: answerValueNumerical
description: The value of the answer to a decimal or numberInterval type of question,
  which is a numeric value.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer.valueDecimal
rank: 1000
alias: answerValueNumerical
owner: Answer
domain_of:
- Answer
range: ValueNumerical
required: false
multivalued: false

```
</details>