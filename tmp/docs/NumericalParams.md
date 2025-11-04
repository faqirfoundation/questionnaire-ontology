
# Class: NumericalParams

Parameters for quantitative values, including unit and precision.

URI: [datamodel:NumericalParams](https://w3id.org/faqir/datamodel/NumericalParams)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20questionNumericalParams%200..1>[NumericalParams&#124;numericalUnit:UnitOfMeasure%20%3F;numericalPrecision:integer%20%3F],[Question])](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20questionNumericalParams%200..1>[NumericalParams&#124;numericalUnit:UnitOfMeasure%20%3F;numericalPrecision:integer%20%3F],[Question])

## Referenced by Class

 *  **None** *[➞questionNumericalParams](question__questionNumericalParams.md)*  <sub>0..1</sub>  **[NumericalParams](NumericalParams.md)**

## Attributes


### Own

 * [➞numericalUnit](numericalParams__numericalUnit.md)  <sub>0..1</sub>
     * Description: The unit of measure for the quantitative value, from UCUM standard.
     * Range: [UnitOfMeasure](UnitOfMeasure.md)
 * [➞numericalPrecision](numericalParams__numericalPrecision.md)  <sub>0..1</sub>
     * Description: The precision of the quantitative value, e.g. number of decimal places.
     * Range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:NumericalParams |