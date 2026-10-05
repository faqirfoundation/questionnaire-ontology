

# Slot: fhir_valueCodeableConcept 


_A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the provision of text. This is a common pattern in healthcare data._





URI: [fhir:valueCodeableConcept](http://hl7.org/fhir/valueCodeableConcept)
Alias: fhir_valueCodeableConcept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |






## Properties

* Range: [ValueCoding](ValueCoding.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valueCodeableConcept |
| native | qo:fhir_valueCodeableConcept |




## LinkML Source

<details>
```yaml
name: fhir_valueCodeableConcept
description: A CodeableConcept represents a value that is usually supplied by providing
  a reference to one or more terminologies or ontologies but may also be defined by
  the provision of text. This is a common pattern in healthcare data.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valueCodeableConcept
alias: fhir_valueCodeableConcept
owner: saref_PropertyValue
domain_of:
- saref_PropertyValue
range: ValueCoding
required: false
multivalued: false

```
</details>