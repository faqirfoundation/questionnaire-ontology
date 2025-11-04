
# Class: ValueNumerical

Base class for quantitative values, they may have units and precision.

URI: [datamodel:ValueNumerical](https://w3id.org/faqir/datamodel/ValueNumerical)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Weight],[Answer]++-%20answerValueNumerical%200..1>[ValueNumerical&#124;numericalValue:decimal],[ScoreParameter]++-%20scoreParameterValueNumerical%200..1>[ValueNumerical],[ScoreValue]++-%20scoreValueNumerical%200..1>[ValueNumerical],[ValueNumerical]^-[Weight],[ScoreValue],[ScoreParameter],[Answer])](https://yuml.me/diagram/nofunky;dir:TB/class/[Weight],[Answer]++-%20answerValueNumerical%200..1>[ValueNumerical&#124;numericalValue:decimal],[ScoreParameter]++-%20scoreParameterValueNumerical%200..1>[ValueNumerical],[ScoreValue]++-%20scoreValueNumerical%200..1>[ValueNumerical],[ValueNumerical]^-[Weight],[ScoreValue],[ScoreParameter],[Answer])

## Children

 * [Weight](Weight.md) - Weight.

## Referenced by Class

 *  **None** *[➞answerValueNumerical](answer__answerValueNumerical.md)*  <sub>0..1</sub>  **[ValueNumerical](ValueNumerical.md)**
 *  **None** *[➞scoreParameterValueNumerical](scoreParameter__scoreParameterValueNumerical.md)*  <sub>0..1</sub>  **[ValueNumerical](ValueNumerical.md)**
 *  **None** *[➞scoreValueNumerical](scoreValue__scoreValueNumerical.md)*  <sub>0..1</sub>  **[ValueNumerical](ValueNumerical.md)**

## Attributes


### Own

 * [➞numericalValue](valueNumerical__numericalValue.md)  <sub>1..1</sub>
     * Description: The quantitative value, which can be an integer or a float.
     * Range: [Decimal](types/Decimal.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ValueNumerical |