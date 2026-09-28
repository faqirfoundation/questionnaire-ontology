
# Class: ValueCoding

A coded value with a unique code for each display text, typically used for standardized questionnaires.

URI: [qo:ValueCoding](https://ns.faqir.org/q-o#ValueCoding)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QoQuestion]++-%20qo_codingParams%200..*>[ValueCoding&#124;code:string;display:string],[SarefPropertyValue]++-%20fhir_valueCodeableConcept%200..1>[ValueCoding],[SarefPropertyValue],[QoQuestion])](https://yuml.me/diagram/nofunky;dir:TB/class/[QoQuestion]++-%20qo_codingParams%200..*>[ValueCoding&#124;code:string;display:string],[SarefPropertyValue]++-%20fhir_valueCodeableConcept%200..1>[ValueCoding],[SarefPropertyValue],[QoQuestion])

## Referenced by Class

 *  **None** *[➞qo_codingParams](qoQuestion__qo_codingParams.md)*  <sub>0..\*</sub>  **[ValueCoding](ValueCoding.md)**
 *  **None** *[➞fhir_valueCodeableConcept](sarefPropertyValue__fhir_valueCodeableConcept.md)*  <sub>0..1</sub>  **[ValueCoding](ValueCoding.md)**

## Attributes


### Own

 * [➞code](valueCoding__code.md)  <sub>1..1</sub>
     * Description: The code representing the value (e.g. code '1' for value 'Yes').
     * Range: [String](types/String.md)
 * [➞display](valueCoding__display.md)  <sub>1..1</sub>
     * Description: The human-readable display text for the code (e.g. code '1' for value 'Yes').
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | fhir:Coding |