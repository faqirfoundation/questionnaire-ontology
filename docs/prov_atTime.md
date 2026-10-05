

# Slot: prov_atTime 


_The time at which an InstantaneousEvent occurred._





URI: [prov:atTime](http://www.w3.org/ns/prov#atTime)
Alias: prov_atTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:atTime |
| native | qo:prov_atTime |
| undefined | saref:hasTimestamp, fhir:DeviceMetric.calibration.time, sosa:phenomenonTime |




## LinkML Source

<details>
```yaml
name: prov_atTime
description: The time at which an InstantaneousEvent occurred.
from_schema: https://ns.faqir.org/q-o
mappings:
- saref:hasTimestamp
- fhir:DeviceMetric.calibration.time
- sosa:phenomenonTime
rank: 1000
domain: sulo_Process
slot_uri: prov:atTime
alias: prov_atTime
domain_of:
- saref_PropertyValue
range: datetime
required: false
multivalued: false

```
</details>