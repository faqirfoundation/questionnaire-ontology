

# Slot: questionRequired 


_Indicates whether answering this question is mandatory (true) or it's optional (false)._





URI: [https://w3id.org/faqir/datamodel/questionRequired](https://w3id.org/faqir/datamodel/questionRequired)
Alias: questionRequired

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/questionRequired |
| native | https://w3id.org/faqir/datamodel/questionRequired |
| undefined | fhir:Questionnaire.item.required |




## LinkML Source

<details>
```yaml
name: questionRequired
description: Indicates whether answering this question is mandatory (true) or it's
  optional (false).
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.required
rank: 1000
ifabsent: 'False'
alias: questionRequired
owner: Question
domain_of:
- Question
range: boolean

```
</details>