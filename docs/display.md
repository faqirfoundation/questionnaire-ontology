

# Slot: display 


_The human-readable display text for the code (e.g. code '1' for value 'Yes')._





URI: [fhir:display](http://hl7.org/fhir/display)
Alias: display

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ValueCoding](ValueCoding.md) | A coded value with a unique code for each display text, typically used for st... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:display |
| native | qo:display |




## LinkML Source

<details>
```yaml
name: display
description: The human-readable display text for the code (e.g. code '1' for value
  'Yes').
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:display
alias: display
owner: ValueCoding
domain_of:
- ValueCoding
range: string
required: true

```
</details>