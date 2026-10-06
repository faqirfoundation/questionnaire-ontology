

# Slot: prov_startedAtTime 


_The time at which an activity started._





URI: [prov:startedAtTime](http://www.w3.org/ns/prov#startedAtTime)
Alias: prov_startedAtTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [TimeInterval](TimeInterval.md) | A temporal entity with an extent or duration |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:startedAtTime |
| native | qo:prov_startedAtTime |




## LinkML Source

<details>
```yaml
name: prov_startedAtTime
description: The time at which an activity started.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: sulo_Process
slot_uri: prov:startedAtTime
alias: prov_startedAtTime
domain_of:
- sulo_Process
- time_Interval
range: datetime
required: false
multivalued: false

```
</details>