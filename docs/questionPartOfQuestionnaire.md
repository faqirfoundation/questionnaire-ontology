

# Slot: questionPartOfQuestionnaire 


_The Questionnaire that this Question is part of._





URI: [datamodel:questionPartOfQuestionnaire](https://w3id.org/faqir/datamodel/questionPartOfQuestionnaire)
Alias: questionPartOfQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:questionPartOfQuestionnaire |
| native | https://w3id.org/faqir/datamodel/questionPartOfQuestionnaire |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: questionPartOfQuestionnaire
description: The Questionnaire that this Question is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: Question
slot_uri: datamodel:questionPartOfQuestionnaire
alias: questionPartOfQuestionnaire
domain_of:
- Question
inverse: questionnaireHasQuestion
range: Questionnaire
required: true
multivalued: true

```
</details>