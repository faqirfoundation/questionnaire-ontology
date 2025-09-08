
# Class: QuantitativeValue

Base class for quantitative values with units.

URI: [datamodel:QuantitativeValue](https://w3id.org/faqir/datamodel/QuantitativeValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Weight],[ValueNumberInInterval],[Question]++-%20intervalQuestionParams%200..*>[QuantitativeValue&#124;quantitativeValue:decimal],[QuantitativeValue]^-[Weight],[QuantitativeValue]^-[ValueNumberInInterval],[Question])](https://yuml.me/diagram/nofunky;dir:TB/class/[Weight],[ValueNumberInInterval],[Question]++-%20intervalQuestionParams%200..*>[QuantitativeValue&#124;quantitativeValue:decimal],[QuantitativeValue]^-[Weight],[QuantitativeValue]^-[ValueNumberInInterval],[Question])

## Children

 * [ValueNumberInInterval](ValueNumberInInterval.md) - A number that falls within a specified interval, with a coding for the value.
 * [Weight](Weight.md) - Weight.

## Referenced by Class

 *  **None** *[intervalQuestionParams](intervalQuestionParams.md)*  <sub>0..\*</sub>  **[QuantitativeValue](QuantitativeValue.md)**

## Attributes


### Own

 * [➞quantitativeValue](quantitativeValue__quantitativeValue.md)  <sub>1..1</sub>
     * Description: The quantitative value, which can be an integer or a float.
     * Range: [Decimal](types/Decimal.md)
