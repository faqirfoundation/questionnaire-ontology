
# Class: ValueDateTime

A date and time value, typically in ISO 8601 format.

URI: [datamodel:ValueDateTime](https://w3id.org/faqir/datamodel/ValueDateTime)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Answer]++-%20answerValueDateTime%200..1>[ValueDateTime&#124;dateTimeValue:datetime%20%3F],[ScoreParameter]++-%20scoreParameterValueDateTime%200..1>[ValueDateTime],[ScoreParameter],[Answer])](https://yuml.me/diagram/nofunky;dir:TB/class/[Answer]++-%20answerValueDateTime%200..1>[ValueDateTime&#124;dateTimeValue:datetime%20%3F],[ScoreParameter]++-%20scoreParameterValueDateTime%200..1>[ValueDateTime],[ScoreParameter],[Answer])

## Referenced by Class

 *  **None** *[➞answerValueDateTime](answer__answerValueDateTime.md)*  <sub>0..1</sub>  **[ValueDateTime](ValueDateTime.md)**
 *  **None** *[➞scoreParameterValueDateTime](scoreParameter__scoreParameterValueDateTime.md)*  <sub>0..1</sub>  **[ValueDateTime](ValueDateTime.md)**

## Attributes


### Own

 * [➞dateTimeValue](valueDateTime__dateTimeValue.md)  <sub>0..1</sub>
     * Description: The date and time value in ISO 8601 format.
     * Range: [Datetime](types/Datetime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ValueDateTime |
|  | | xsd:dateTime |