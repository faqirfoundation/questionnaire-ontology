
# Class: FlexibleDateTime

The Extended Date/Time Format (EDTF / ISO 8601-2). It is natively typed as a string literal but explicitly structured to support partial dates (2026, 2026-06), uncertain dates (2026?), or intervals. Level 0 and Level 1

URI: [qo:FlexibleDateTime](https://ns.faqir.org/q-o#FlexibleDateTime)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[QoAnswer],[OwlThing],[SarefPropertyValue]++-%20prov_atTime%200..1>[FlexibleDateTime&#124;datetime:string%20%3F],[TimeInterval]++-%20prov_endedAtTime%200..1>[FlexibleDateTime],[OwlThing]++-%20prov_generatedAtTime%200..*>[FlexibleDateTime],[TimeInterval]++-%20prov_startedAtTime%200..1>[FlexibleDateTime],[QoAnswer]++-%20prov_generatedAtTime%201..*>[FlexibleDateTime],[TimeInterval],[SarefPropertyValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[QoAnswer],[OwlThing],[SarefPropertyValue]++-%20prov_atTime%200..1>[FlexibleDateTime&#124;datetime:string%20%3F],[TimeInterval]++-%20prov_endedAtTime%200..1>[FlexibleDateTime],[OwlThing]++-%20prov_generatedAtTime%200..*>[FlexibleDateTime],[TimeInterval]++-%20prov_startedAtTime%200..1>[FlexibleDateTime],[QoAnswer]++-%20prov_generatedAtTime%201..*>[FlexibleDateTime],[TimeInterval],[SarefPropertyValue])

## Referenced by Class

 *  **[SuloProcess](SuloProcess.md)** *[prov_atTime](prov_atTime.md)*  <sub>0..1</sub>  **[FlexibleDateTime](FlexibleDateTime.md)**
 *  **[SuloProcess](SuloProcess.md)** *[prov_endedAtTime](prov_endedAtTime.md)*  <sub>0..1</sub>  **[FlexibleDateTime](FlexibleDateTime.md)**
 *  **[OwlThing](OwlThing.md)** *[prov_generatedAtTime](prov_generatedAtTime.md)*  <sub>0..\*</sub>  **[FlexibleDateTime](FlexibleDateTime.md)**
 *  **[SuloProcess](SuloProcess.md)** *[prov_startedAtTime](prov_startedAtTime.md)*  <sub>0..1</sub>  **[FlexibleDateTime](FlexibleDateTime.md)**
 *  **[QoAnswer](QoAnswer.md)** *[qo_Answer➞prov_generatedAtTime](qo_Answer_prov_generatedAtTime.md)*  <sub>1..\*</sub>  **[FlexibleDateTime](FlexibleDateTime.md)**

## Attributes


### Own

 * [➞datetime](flexibleDateTime__datetime.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | phro:EDTF |