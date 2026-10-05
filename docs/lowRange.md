

# Slot: lowRange 


_Low range, if relevant._





URI: [phro:lowRange](https://ns.faqir.org/phr-o#lowRange)
Alias: lowRange

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FhirReferenceRange](FhirReferenceRange.md) | Guidance on how to interpret the value by comparison to a normal or recommend... |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:lowRange |
| native | qo:lowRange |




## LinkML Source

<details>
```yaml
name: lowRange
description: Low range, if relevant.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: phro:lowRange
alias: lowRange
owner: fhir_ReferenceRange
domain_of:
- fhir_ReferenceRange
range: QuantityValue
required: false
multivalued: false

```
</details>