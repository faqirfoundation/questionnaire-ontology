
# Class: fhir_ValueRatio

A ratio of two Quantity values - a numerator and a denominator

URI: [qo:FhirValueRatio](https://ns.faqir.org/q-o#FhirValueRatio)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<denominator%201..1-++[FhirValueRatio],[QuantityValue]<numerator%201..1-++[FhirValueRatio],[SarefPropertyValue]++-%20fhir_valueRatio%200..1>[FhirValueRatio],[SarefPropertyValue],[QuantityValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<denominator%201..1-++[FhirValueRatio],[QuantityValue]<numerator%201..1-++[FhirValueRatio],[SarefPropertyValue]++-%20fhir_valueRatio%200..1>[FhirValueRatio],[SarefPropertyValue],[QuantityValue])

## Referenced by Class

 *  **None** *[➞fhir_valueRatio](sarefPropertyValue__fhir_valueRatio.md)*  <sub>0..1</sub>  **[FhirValueRatio](FhirValueRatio.md)**

## Attributes


### Own

 * [➞numerator](fhirValueRatio__numerator.md)  <sub>1..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [➞denominator](fhirValueRatio__denominator.md)  <sub>1..1</sub>
     * Range: [QuantityValue](QuantityValue.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | fhir:datatype.Ratio |