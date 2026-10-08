

# Slot: qo_hasOrderedSection 


_Associates a survey container or group with a sequence-indexed wrapper holding a nested thematic subgroup._





URI: [qo:hasOrderedSection](https://ns.faqir.org/q-o#hasOrderedSection)
Alias: qo_hasOrderedSection


## Inheritance

* [dcterms_hasPart](dcterms_hasPart.md)
    * **qo_hasOrderedSection**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  yes  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  yes  |







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
description: Associates a survey container or group with a sequence-indexed wrapper
  holding a nested thematic subgroup.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire.item.where(type='group')
rank: 1000
is_a: dcterms_hasPart
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