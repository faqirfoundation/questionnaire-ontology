
# Class: fhir_ReferenceRange

Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange elements would be used.

URI: [qo:FhirReferenceRange](https://ns.faqir.org/q-o#FhirReferenceRange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<normalValue%200..*-++[FhirReferenceRange],[QuantityValue]<highRange%200..1-++[FhirReferenceRange],[QuantityValue]<lowRange%200..1-++[FhirReferenceRange],[SarefPropertyValue]++-%20fhir_valueRange%200..1>[FhirReferenceRange],[SarefProperty]++-%20fhir_referenceRange%200..1>[FhirReferenceRange],[SarefPropertyValue],[SarefProperty],[QuantityValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<normalValue%200..*-++[FhirReferenceRange],[QuantityValue]<highRange%200..1-++[FhirReferenceRange],[QuantityValue]<lowRange%200..1-++[FhirReferenceRange],[SarefPropertyValue]++-%20fhir_valueRange%200..1>[FhirReferenceRange],[SarefProperty]++-%20fhir_referenceRange%200..1>[FhirReferenceRange],[SarefPropertyValue],[SarefProperty],[QuantityValue])

## Referenced by Class

 *  **None** *[➞fhir_valueRange](sarefPropertyValue__fhir_valueRange.md)*  <sub>0..1</sub>  **[FhirReferenceRange](FhirReferenceRange.md)**
 *  **None** *[➞fhir_referenceRange](sarefProperty__fhir_referenceRange.md)*  <sub>0..1</sub>  **[FhirReferenceRange](FhirReferenceRange.md)**

## Attributes


### Own

 * [➞lowRange](fhirReferenceRange__lowRange.md)  <sub>0..1</sub>
     * Description: Low range, if relevant.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞highRange](fhirReferenceRange__highRange.md)  <sub>0..1</sub>
     * Description: High range, if relevant.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞normalValue](fhirReferenceRange__normalValue.md)  <sub>0..\*</sub>
     * Description: Normal value, if relevant.
     * Range: [QuantityValue](QuantityValue.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | fhir:Observation.referenceRange |