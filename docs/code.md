

# Slot: code 


_The code representing the value (e.g. code '1' for value 'Yes')._





URI: [fhir:code](http://hl7.org/fhir/code)
Alias: code

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
| self | fhir:code |
| native | qo:code |




## LinkML Source

<details>
```yaml
name: code
description: The code representing the value (e.g. code '1' for value 'Yes').
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:code
alias: code
owner: ValueCoding
domain_of:
- ValueCoding
range: string
required: true

```
</details>