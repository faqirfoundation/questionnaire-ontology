

# Slot: qo_hasOrderedSection 


_The Section that is part of this Questionnaire or Section, with their display order._





URI: [qo:hasOrderedSection](https://ns.faqir.org/q-o#hasOrderedSection)
Alias: qo_hasOrderedSection


## Inheritance

* [dcterms_hasPart](dcterms_hasPart.md)
    * **qo_hasOrderedSection**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaire](QoQuestionnaire.md) | A questionnaire that can be answered (collection of questions) |  yes  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  yes  |







## Properties

* Range: [QoOrderedSection](QoOrderedSection.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:hasOrderedSection |
| native | qo:qo_hasOrderedSection |
| narrow | fhir:Questionnaire.item.where(type='group') |




## LinkML Source

<details>
```yaml
name: qo_hasOrderedSection
description: The Section that is part of this Questionnaire or Section, with their
  display order.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire.item.where(type='group')
rank: 1000
is_a: dcterms_hasPart
domain: owl_Thing
slot_uri: qo:hasOrderedSection
alias: qo_hasOrderedSection
domain_of:
- qo_Questionnaire
- qo_Section
range: qo_OrderedSection
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>