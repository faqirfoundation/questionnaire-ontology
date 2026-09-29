

# Slot: qo_section 


_Identifies the specific thematic grouping referenced at a given positional index._





URI: [qo:section](https://ns.faqir.org/q-o#section)
Alias: qo_section


## Inheritance

* [dcterms_hasPart](dcterms_hasPart.md)
    * **qo_section**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |







## Properties

* Range: [QoSection](QoSection.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:section |
| native | qo:qo_section |




## LinkML Source

<details>
```yaml
name: qo_section
description: Identifies the specific thematic grouping referenced at a given positional
  index.
from_schema: https://ns.faqir.org/q-o
rank: 1000
is_a: dcterms_hasPart
domain: qo_OrderedSection
slot_uri: qo:section
alias: qo_section
domain_of:
- qo_OrderedSection
range: qo_Section
required: true
multivalued: true

```
</details>