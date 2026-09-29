

# Slot: saref_isValueOfProperty 


_Links a property value to the property or property of interest it is a value of._





URI: [saref:isValueOfProperty](https://saref.etsi.org/core/isValueOfProperty)
Alias: saref_isValueOfProperty

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |







## Properties

* Range: [SarefProperty](SarefProperty.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | saref:isValueOfProperty |
| native | qo:saref_isValueOfProperty |




## LinkML Source

<details>
```yaml
name: saref_isValueOfProperty
description: Links a property value to the property or property of interest it is
  a value of.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: saref_PropertyValue
slot_uri: saref:isValueOfProperty
alias: saref_isValueOfProperty
domain_of:
- saref_PropertyValue
range: saref_Property
required: false
multivalued: false

```
</details>