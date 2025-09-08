
# Class: QuantitativeParams

Parameters for quantitative values, including unit and precision.

URI: [datamodel:QuantitativeParams](https://w3id.org/faqir/datamodel/QuantitativeParams)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20quantitativeQuestionParams%200..*>[QuantitativeParams&#124;quantitativeUnit:UnitOfMeasure;quantitativePrecision:integer%20%3F],[Question])](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20quantitativeQuestionParams%200..*>[QuantitativeParams&#124;quantitativeUnit:UnitOfMeasure;quantitativePrecision:integer%20%3F],[Question])

## Referenced by Class

 *  **None** *[quantitativeQuestionParams](quantitativeQuestionParams.md)*  <sub>0..\*</sub>  **[QuantitativeParams](QuantitativeParams.md)**

## Attributes


### Own

 * [➞quantitativeUnit](quantitativeParams__quantitativeUnit.md)  <sub>1..1</sub>
     * Description: The unit of measure for the quantitative value, from UCUM standard.
     * Range: [UnitOfMeasure](UnitOfMeasure.md)
 * [➞quantitativePrecision](quantitativeParams__quantitativePrecision.md)  <sub>0..1</sub>
     * Description: The precision of the quantitative value, e.g. number of decimal places.
     * Range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | datamodel:QuantitativeParams |