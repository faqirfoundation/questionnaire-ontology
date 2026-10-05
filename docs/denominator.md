

# Slot: denominator 



URI: [fhir:denominator](http://hl7.org/fhir/denominator)
Alias: denominator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FhirValueRatio](FhirValueRatio.md) | A ratio of two Quantity values - a numerator and a denominator |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:denominator |
| native | qo:denominator |




## LinkML Source

<details>
```yaml
name: denominator
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:denominator
alias: denominator
owner: fhir_ValueRatio
domain_of:
- fhir_ValueRatio
range: QuantityValue
required: true
multivalued: false

```
</details>