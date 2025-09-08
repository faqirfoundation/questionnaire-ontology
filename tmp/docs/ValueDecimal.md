
# Class: ValueDecimal

A decimal value, either integer or float.

URI: [datamodel:ValueDecimal](https://w3id.org/faqir/datamodel/ValueDecimal)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IntervalParams]++-%20maxValue%201..1>[ValueDecimal&#124;decimalValue:decimal%20%3F],[IntervalParams]++-%20minValue%201..1>[ValueDecimal],[IntervalParams])](https://yuml.me/diagram/nofunky;dir:TB/class/[IntervalParams]++-%20maxValue%201..1>[ValueDecimal&#124;decimalValue:decimal%20%3F],[IntervalParams]++-%20minValue%201..1>[ValueDecimal],[IntervalParams])

## Referenced by Class

 *  **None** *[➞maxValue](intervalParams__maxValue.md)*  <sub>1..1</sub>  **[ValueDecimal](ValueDecimal.md)**
 *  **None** *[➞minValue](intervalParams__minValue.md)*  <sub>1..1</sub>  **[ValueDecimal](ValueDecimal.md)**

## Attributes


### Own

 * [➞decimalValue](valueDecimal__decimalValue.md)  <sub>0..1</sub>
     * Description: The decimal value, which can be an integer or a float.
     * Range: [Decimal](types/Decimal.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | xsd:decimal |