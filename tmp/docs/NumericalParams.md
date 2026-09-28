
# Class: NumericalParams

Parameters for quantitative values, including unit and precision.

URI: [qo:NumericalParams](https://ns.faqir.org/q-o#NumericalParams)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QoQuestion]++-%20qo_numericalParams%200..1>[NumericalParams&#124;numericalUnit:uriorcurie%20%3F;numericalPrecision:integer%20%3F],[QoQuestion])](https://yuml.me/diagram/nofunky;dir:TB/class/[QoQuestion]++-%20qo_numericalParams%200..1>[NumericalParams&#124;numericalUnit:uriorcurie%20%3F;numericalPrecision:integer%20%3F],[QoQuestion])

## Referenced by Class

 *  **None** *[➞qo_numericalParams](qoQuestion__qo_numericalParams.md)*  <sub>0..1</sub>  **[NumericalParams](NumericalParams.md)**

## Attributes


### Own

 * [➞numericalUnit](numericalParams__numericalUnit.md)  <sub>0..1</sub>
     * Description: The unit of measure for the quantitative value, from UCUM standard.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞numericalPrecision](numericalParams__numericalPrecision.md)  <sub>0..1</sub>
     * Description: The precision of the quantitative value, e.g. number of decimal places.
     * Range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | phro:NumericalParams |