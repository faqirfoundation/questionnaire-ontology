

# Slot: orderedQuestionPartOfQuestionnaire 


_The Questionnaire that this Question is part of in the specified order._





URI: [faqir:orderedQuestionPartOfQuestionnaire](https://faqir.org/datamodel/orderedQuestionPartOfQuestionnaire)
Alias: orderedQuestionPartOfQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedQuestion](OrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:orderedQuestionPartOfQuestionnaire |
| native | https://w3id.org/faqir/datamodel/orderedQuestionPartOfQuestionnaire |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: orderedQuestionPartOfQuestionnaire
description: The Questionnaire that this Question is part of in the specified order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: OrderedQuestion
slot_uri: faqir:orderedQuestionPartOfQuestionnaire
alias: orderedQuestionPartOfQuestionnaire
domain_of:
- OrderedQuestion
inverse: questionnaireHasOrderedQuestion
range: Questionnaire
required: false
multivalued: false

```
</details>