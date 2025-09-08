

# Slot: questionnaireHasOrderedQuestion 


_The Question that is part of this Questionnaire, with their display order._





URI: [faqir:questionnaireHasOrderedQuestion](https://faqir.org/datamodel/questionnaireHasOrderedQuestion)
Alias: questionnaireHasOrderedQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [OrderedQuestion](OrderedQuestion.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnaireHasOrderedQuestion |
| native | https://w3id.org/faqir/datamodel/questionnaireHasOrderedQuestion |
| undefined | fhir:Questionnaire.item.where(type='question') |




## LinkML Source

<details>
```yaml
name: questionnaireHasOrderedQuestion
description: The Question that is part of this Questionnaire, with their display order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='question')
rank: 1000
domain: Questionnaire
slot_uri: faqir:questionnaireHasOrderedQuestion
alias: questionnaireHasOrderedQuestion
domain_of:
- Questionnaire
inverse: orderedQuestionPartOfQuestionnaire
range: OrderedQuestion
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>