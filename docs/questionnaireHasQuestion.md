

# Slot: questionnaireHasQuestion 


_The Question that is part of this Questionnaire._





URI: [datamodel:questionnaireHasQuestion](https://w3id.org/faqir/datamodel/questionnaireHasQuestion)
Alias: questionnaireHasQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [Question](Question.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:questionnaireHasQuestion |
| native | https://w3id.org/faqir/datamodel/questionnaireHasQuestion |
| undefined | fhir:Questionnaire.item.where(type='question') |




## LinkML Source

<details>
```yaml
name: questionnaireHasQuestion
description: The Question that is part of this Questionnaire.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='question')
rank: 1000
domain: Questionnaire
slot_uri: datamodel:questionnaireHasQuestion
alias: questionnaireHasQuestion
domain_of:
- Questionnaire
inverse: questionPartOfQuestionnaire
range: Question
required: false
multivalued: true

```
</details>