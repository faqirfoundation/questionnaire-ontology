
# Class: ValueCoding

A coded value with a unique code for each display text, typically used for standardized questionnaires.

URI: [datamodel:ValueCoding](https://w3id.org/faqir/datamodel/ValueCoding)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20questionCodingParams%200..*>[ValueCoding&#124;code:string;display:string],[Question])](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20questionCodingParams%200..*>[ValueCoding&#124;code:string;display:string],[Question])

## Referenced by Class

 *  **None** *[➞questionCodingParams](question__questionCodingParams.md)*  <sub>0..\*</sub>  **[ValueCoding](ValueCoding.md)**

## Attributes


### Own

 * [➞code](valueCoding__code.md)  <sub>1..1</sub>
     * Description: The code representing the value (e.g. code '1' for display 'Yes').
     * Range: [String](types/String.md)
 * [➞display](valueCoding__display.md)  <sub>1..1</sub>
     * Description: The human-readable display text for the code (e.g. code '1' for display 'Yes').
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ValueCoding |
|  | | fhir:Coding |