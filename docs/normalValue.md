

# Slot: normalValue 


_Normal value, if relevant._





URI: [phro:normalValue](https://ns.faqir.org/phr-o#normalValue)
Alias: normalValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FhirReferenceRange](FhirReferenceRange.md) | Guidance on how to interpret the value by comparison to a normal or recommend... |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:normalValue |
| native | qo:normalValue |




## LinkML Source

<details>
```yaml
name: normalValue
description: Normal value, if relevant.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: phro:normalValue
alias: normalValue
owner: fhir_ReferenceRange
domain_of:
- fhir_ReferenceRange
range: QuantityValue
required: false
multivalued: true

```
</details>