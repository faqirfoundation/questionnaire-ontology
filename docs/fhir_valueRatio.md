

# Slot: fhir_valueRatio 


_A relationship between two Quantity values expressed as a numerator and a denominator. The Ratio datatype should only be used to express a relationship of two numbers if the relationship cannot be suitably expressed using a Quantity and a common unit. Where the denominator value is known to be fixed to '1', Quantity should be used instead of Ratio._





URI: [fhir:valueRatio](http://hl7.org/fhir/valueRatio)
Alias: fhir_valueRatio

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |







## Properties

* Range: [FhirValueRatio](FhirValueRatio.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valueRatio |
| native | qo:fhir_valueRatio |




## LinkML Source

<details>
```yaml
name: fhir_valueRatio
description: A relationship between two Quantity values expressed as a numerator and
  a denominator. The Ratio datatype should only be used to express a relationship
  of two numbers if the relationship cannot be suitably expressed using a Quantity
  and a common unit. Where the denominator value is known to be fixed to '1', Quantity
  should be used instead of Ratio.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valueRatio
alias: fhir_valueRatio
owner: saref_PropertyValue
domain_of:
- saref_PropertyValue
range: fhir_ValueRatio
required: false
multivalued: false

```
</details>