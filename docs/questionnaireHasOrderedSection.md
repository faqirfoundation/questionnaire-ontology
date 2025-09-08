

# Slot: questionnaireHasOrderedSection 


_The Section that is part of this Questionnaire, with their display order._





URI: [faqir:questionnaireHasOrderedSection](https://faqir.org/datamodel/questionnaireHasOrderedSection)
Alias: questionnaireHasOrderedSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [OrderedSection](OrderedSection.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnaireHasOrderedSection |
| native | https://w3id.org/faqir/datamodel/questionnaireHasOrderedSection |
| undefined | fhir:Questionnaire.item.where(type='group') |




## LinkML Source

<details>
```yaml
name: questionnaireHasOrderedSection
description: The Section that is part of this Questionnaire, with their display order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='group')
rank: 1000
domain: Questionnaire
slot_uri: faqir:questionnaireHasOrderedSection
alias: questionnaireHasOrderedSection
domain_of:
- Questionnaire
inverse: orderedSectionPartOfQuestionnaire
range: OrderedSection
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>