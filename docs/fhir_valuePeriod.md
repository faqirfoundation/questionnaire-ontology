

# Slot: fhir_valuePeriod 


_A time period defined by a start and end date/time. A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. 'the patient was an inpatient of the hospital for this time range') or one value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun 2013')._





URI: [fhir:valuePeriod](http://hl7.org/fhir/valuePeriod)
Alias: fhir_valuePeriod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |






## Properties

* Range: [TimeInterval](TimeInterval.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valuePeriod |
| native | qo:fhir_valuePeriod |




## LinkML Source

<details>
```yaml
name: fhir_valuePeriod
description: A time period defined by a start and end date/time. A period specifies
  a range of times. The context of use will specify whether the entire range applies
  (e.g. 'the patient was an inpatient of the hospital for this time range') or one
  value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun
  2013').
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valuePeriod
alias: fhir_valuePeriod
owner: saref_PropertyValue
domain_of:
- saref_PropertyValue
range: time_Interval
required: false
multivalued: false

```
</details>