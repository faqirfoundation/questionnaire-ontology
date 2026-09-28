
# Class: time_Interval

A temporal entity with an extent or duration

URI: [qo:TimeInterval](https://ns.faqir.org/q-o#TimeInterval)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SarefPropertyValue]++-%20fhir_valuePeriod%200..1>[TimeInterval&#124;prov_startedAtTime:datetime%20%3F;prov_endedAtTime:datetime%20%3F],[SarefPropertyValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[SarefPropertyValue]++-%20fhir_valuePeriod%200..1>[TimeInterval&#124;prov_startedAtTime:datetime%20%3F;prov_endedAtTime:datetime%20%3F],[SarefPropertyValue])

## Referenced by Class

 *  **None** *[➞fhir_valuePeriod](sarefPropertyValue__fhir_valuePeriod.md)*  <sub>0..1</sub>  **[TimeInterval](TimeInterval.md)**

## Attributes


### Own

 * [prov_startedAtTime](prov_startedAtTime.md)  <sub>0..1</sub>
     * Description: The time at which an activity started.
     * Range: [Datetime](types/Datetime.md)
 * [prov_endedAtTime](prov_endedAtTime.md)  <sub>0..1</sub>
     * Description: The time at which an activity ended.
     * Range: [Datetime](types/Datetime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | time:Interval |