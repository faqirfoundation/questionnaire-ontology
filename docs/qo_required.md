

# Slot: qo_required 


_Whether the question can be left un-answered (false) or an answer is mandatory (true)._





URI: [qo:required](https://ns.faqir.org/q-o#required)
Alias: qo_required

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:required |
| native | qo:qo_required |
| narrow | fhir:Questionnaire.item.required |




## LinkML Source

<details>
```yaml
name: qo_required
description: Whether the question can be left un-answered (false) or an answer is
  mandatory (true).
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire.item.required
rank: 1000
slot_uri: qo:required
alias: qo_required
owner: qo_OrderedQuestion
domain_of:
- qo_OrderedQuestion
range: boolean
required: true

```
</details>