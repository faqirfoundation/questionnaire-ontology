

# Slot: sectionHasOrderedQuestion 


_The Question that is part of this Section, with their display order._





URI: [faqir:sectionHasOrderedQuestion](https://faqir.org/datamodel/sectionHasOrderedQuestion)
Alias: sectionHasOrderedQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A section of questions in the questionnaire |  no  |







## Properties

* Range: [OrderedQuestion](OrderedQuestion.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:sectionHasOrderedQuestion |
| native | https://w3id.org/faqir/datamodel/sectionHasOrderedQuestion |
| undefined | fhir:Questionnaire.item.where(type='question') |




## LinkML Source

<details>
```yaml
name: sectionHasOrderedQuestion
description: The Question that is part of this Section, with their display order.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='question')
rank: 1000
domain: Section
slot_uri: faqir:sectionHasOrderedQuestion
alias: sectionHasOrderedQuestion
domain_of:
- Section
inverse: orderedQuestionPartOfSection
range: OrderedQuestion
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>