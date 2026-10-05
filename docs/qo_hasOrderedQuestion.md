

# Slot: qo_hasOrderedQuestion 


_Associates a survey container or group with a sequence-indexed wrapper holding an individual inquiry item._





URI: [qo:hasOrderedQuestion](https://ns.faqir.org/q-o#hasOrderedQuestion)
Alias: qo_hasOrderedQuestion


## Inheritance

* [dcterms_hasPart](dcterms_hasPart.md)
    * **qo_hasOrderedQuestion**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  yes  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  yes  |






## Properties

* Range: [QoOrderedQuestion](QoOrderedQuestion.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:hasOrderedQuestion |
| native | qo:qo_hasOrderedQuestion |
| narrow | fhir:Questionnaire.item.where(type='question') |




## LinkML Source

<details>
```yaml
name: qo_hasOrderedQuestion
description: Associates a survey container or group with a sequence-indexed wrapper
  holding an individual inquiry item.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire.item.where(type='question')
rank: 1000
is_a: dcterms_hasPart
slot_uri: qo:hasOrderedQuestion
alias: qo_hasOrderedQuestion
domain_of:
- qo_Questionnaire
- qo_Section
range: qo_OrderedQuestion
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>