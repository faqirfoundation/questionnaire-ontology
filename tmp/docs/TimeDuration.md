
# Class: time_Duration

Duration of a temporal extent expressed as a decimal number scaled by a temporal unit

URI: [qo:TimeDuration](https://ns.faqir.org/q-o#TimeDuration)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QoOrderedQuestion]++-%20qo_temporalValidity%201..1>[TimeDuration&#124;saref_hasValue:string%20%3F;saref_isMeasuredIn:uriorcurie%20%3F],[QoOrderedQuestion])](https://yuml.me/diagram/nofunky;dir:TB/class/[QoOrderedQuestion]++-%20qo_temporalValidity%201..1>[TimeDuration&#124;saref_hasValue:string%20%3F;saref_isMeasuredIn:uriorcurie%20%3F],[QoOrderedQuestion])

## Referenced by Class

 *  **None** *[qo_temporalValidity](qo_temporalValidity.md)*  <sub>1..1</sub>  **[TimeDuration](TimeDuration.md)**
 *  **None** *[time_hasDuration](time_hasDuration.md)*  <sub>0..1</sub>  **[TimeDuration](TimeDuration.md)**

## Attributes


### Own

 * [saref_hasValue](saref_hasValue.md)  <sub>0..1</sub>
     * Description: Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes.
     * Range: [String](types/String.md)
 * [saref_isMeasuredIn](saref_isMeasuredIn.md)  <sub>0..1</sub>
     * Description: A relationship identifying the unit of measure used for a certain entity.
     * Range: [Uriorcurie](types/Uriorcurie.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | time:Duration |