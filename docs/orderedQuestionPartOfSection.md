

# Slot: orderedQuestionPartOfSection 


_The Section that this Question is part of in the specified order._





URI: [faqir:orderedQuestionPartOfSection](https://faqir.org/datamodel/orderedQuestionPartOfSection)
Alias: orderedQuestionPartOfSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedQuestion](OrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Section](Section.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:orderedQuestionPartOfSection |
| native | https://w3id.org/faqir/datamodel/orderedQuestionPartOfSection |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: orderedQuestionPartOfSection
description: The Section that this Question is part of in the specified order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: OrderedQuestion
slot_uri: faqir:orderedQuestionPartOfSection
alias: orderedQuestionPartOfSection
domain_of:
- OrderedQuestion
inverse: sectionHasOrderedQuestion
range: Section
required: false
multivalued: false

```
</details>