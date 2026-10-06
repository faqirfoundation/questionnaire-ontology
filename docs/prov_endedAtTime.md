

# Slot: prov_endedAtTime 


_The time at which an activity ended._





URI: [prov:endedAtTime](http://www.w3.org/ns/prov#endedAtTime)
Alias: prov_endedAtTime

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
| self | prov:endedAtTime |
| native | qo:prov_endedAtTime |




## LinkML Source

<details>
```yaml
name: prov_endedAtTime
description: The time at which an activity ended.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: sulo_Process
slot_uri: prov:endedAtTime
alias: prov_endedAtTime
domain_of:
- sulo_Process
- time_Interval
range: datetime
required: false
multivalued: false

```
</details>