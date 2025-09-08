

# Slot: orderedSectionPartOfQuestionnaire 


_The Questionnaire that this Section is part of in the specified order._





URI: [faqir:orderedSectionPartOfQuestionnaire](https://faqir.org/datamodel/orderedSectionPartOfQuestionnaire)
Alias: orderedSectionPartOfQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedSection](OrderedSection.md) | Section's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:orderedSectionPartOfQuestionnaire |
| native | https://w3id.org/faqir/datamodel/orderedSectionPartOfQuestionnaire |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: orderedSectionPartOfQuestionnaire
description: The Questionnaire that this Section is part of in the specified order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: OrderedSection
slot_uri: faqir:orderedSectionPartOfQuestionnaire
alias: orderedSectionPartOfQuestionnaire
domain_of:
- OrderedSection
inverse: questionnaireHasOrderedSection
range: Questionnaire
required: false
multivalued: false

```
</details>