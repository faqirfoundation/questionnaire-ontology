
# Class: QuantityValue

A measured amount (or an amount that can potentially be measured).

URI: [qo:QuantityValue](https://ns.faqir.org/q-o#QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[FhirReferenceRange]++-%20highRange%200..1>[QuantityValue&#124;saref_isMeasuredIn:uriorcurie%20%3F;saref_hasValue:string%20%3F],[FhirReferenceRange]++-%20lowRange%200..1>[QuantityValue],[FhirReferenceRange]++-%20normalValue%200..*>[QuantityValue],[FhirValueRatio]++-%20denominator%201..1>[QuantityValue],[FhirValueRatio]++-%20numerator%201..1>[QuantityValue],[FhirValueRatio],[FhirReferenceRange])](https://yuml.me/diagram/nofunky;dir:TB/class/[FhirReferenceRange]++-%20highRange%200..1>[QuantityValue&#124;saref_isMeasuredIn:uriorcurie%20%3F;saref_hasValue:string%20%3F],[FhirReferenceRange]++-%20lowRange%200..1>[QuantityValue],[FhirReferenceRange]++-%20normalValue%200..*>[QuantityValue],[FhirValueRatio]++-%20denominator%201..1>[QuantityValue],[FhirValueRatio]++-%20numerator%201..1>[QuantityValue],[FhirValueRatio],[FhirReferenceRange])

## Referenced by Class

 *  **None** *[➞highRange](fhirReferenceRange__highRange.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞lowRange](fhirReferenceRange__lowRange.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞normalValue](fhirReferenceRange__normalValue.md)*  <sub>0..\*</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞denominator](fhirValueRatio__denominator.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞numerator](fhirValueRatio__numerator.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [saref_isMeasuredIn](saref_isMeasuredIn.md)  <sub>0..1</sub>
     * Description: A relationship identifying the unit of measure used for a certain entity.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [saref_hasValue](saref_hasValue.md)  <sub>0..1</sub>
     * Description: Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | fhir:datatypes.Quantity |