

# Slot: fhir_referenceRange 


_Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange elements would be used._





URI: [http://hl7.org/fhir/Observation.referenceRange](http://hl7.org/fhir/Observation.referenceRange)
Alias: fhir_referenceRange

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |







## Properties

* Range: [FhirReferenceRange](FhirReferenceRange.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | http://hl7.org/fhir/Observation.referenceRange |
| native | qo:fhir_referenceRange |




## LinkML Source

<details>
```yaml
name: fhir_referenceRange
description: Guidance on how to interpret the value by comparison to a normal or recommended
  range. Multiple reference ranges are interpreted as an 'OR'. In other words, to
  represent two distinct target populations, two referenceRange elements would be
  used.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: http://hl7.org/fhir/Observation.referenceRange
alias: fhir_referenceRange
owner: saref_Property
domain_of:
- saref_Property
range: fhir_ReferenceRange
required: false
multivalued: false

```
</details>