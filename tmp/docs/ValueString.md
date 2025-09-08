
# Class: ValueString

A string value, typically used for text or identifiers.

URI: [datamodel:ValueString](https://w3id.org/faqir/datamodel/ValueString)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Answer]++-%20answerValueString%200..*>[ValueString&#124;stringValue:string],[ScoreValue]++-%20scoreValueString%200..1>[ValueString],[ScoreValue],[Answer])](https://yuml.me/diagram/nofunky;dir:TB/class/[Answer]++-%20answerValueString%200..*>[ValueString&#124;stringValue:string],[ScoreValue]++-%20scoreValueString%200..1>[ValueString],[ScoreValue],[Answer])

## Referenced by Class

 *  **None** *[➞answerValueString](answer__answerValueString.md)*  <sub>0..\*</sub>  **[ValueString](ValueString.md)**
 *  **None** *[➞scoreValueString](scoreValue__scoreValueString.md)*  <sub>0..1</sub>  **[ValueString](ValueString.md)**

## Attributes


### Own

 * [➞stringValue](valueString__stringValue.md)  <sub>1..1</sub>
     * Description: The string value, which can be any text.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ValueString |
|  | | xsd:string |