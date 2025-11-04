

# Slot: hasAnswer 


_The Answer to this Question._





URI: [datamodel:hasAnswer](https://w3id.org/faqir/datamodel/hasAnswer)
Alias: hasAnswer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [Answer](Answer.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:hasAnswer |
| native | https://w3id.org/faqir/datamodel/hasAnswer |
| undefined | fhir:Questionnaire.item.answer |




## LinkML Source

<details>
```yaml
name: hasAnswer
description: The Answer to this Question.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.answer
rank: 1000
domain: Question
slot_uri: datamodel:hasAnswer
alias: hasAnswer
domain_of:
- Question
inverse: toQuestion
range: Answer
required: false
multivalued: true

```
</details>