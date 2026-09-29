

# Slot: fhir_valueRange 


_A set of ordered Quantity values defined by a low and high limit._





URI: [fhir:valueRange](http://hl7.org/fhir/valueRange)
Alias: fhir_valueRange

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |







## Properties

* Range: [FhirReferenceRange](FhirReferenceRange.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valueRange |
| native | qo:fhir_valueRange |




## LinkML Source

<details>
```yaml
name: fhir_valueRange
description: A set of ordered Quantity values defined by a low and high limit.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valueRange
alias: fhir_valueRange
owner: saref_PropertyValue
domain_of:
- saref_PropertyValue
range: fhir_ReferenceRange
required: false
multivalued: false

```
</details>