

# Slot: fhir_valueReference 


_The Reference type contains at least one of a reference (literal reference), an identifier (logical reference), and a display (text description of target). In addition, it may contain a target type._





URI: [fhir:valueReference](http://hl7.org/fhir/valueReference)
Alias: fhir_valueReference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valueReference |
| native | qo:fhir_valueReference |




## LinkML Source

<details>
```yaml
name: fhir_valueReference
description: The Reference type contains at least one of a reference (literal reference),
  an identifier (logical reference), and a display (text description of target). In
  addition, it may contain a target type.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valueReference
alias: fhir_valueReference
domain_of:
- saref_PropertyValue
range: uriorcurie
required: false
multivalued: false

```
</details>