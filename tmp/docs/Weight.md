
# Class: Weight

Weight.

URI: [datamodel:Weight](https://w3id.org/faqir/datamodel/Weight)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vault]++-%20weight%200..1>[Weight&#124;weightType:WeightType;numericalValue(i):decimal],[ValueNumerical]^-[Weight],[Vault],[ValueNumerical])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vault]++-%20weight%200..1>[Weight&#124;weightType:WeightType;numericalValue(i):decimal],[ValueNumerical]^-[Weight],[Vault],[ValueNumerical])

## Parents

 *  is_a: [ValueNumerical](ValueNumerical.md) - Base class for quantitative values, they may have units and precision.

## Referenced by Class

 *  **None** *[➞weight](vault__weight.md)*  <sub>0..1</sub>  **[Weight](Weight.md)**

## Attributes


### Own

 * [➞weightType](weight__weightType.md)  <sub>1..1</sub>
     * Description: The type of weight measurement, e.g. measured or stated.
     * Range: [WeightType](WeightType.md)

### Inherited from ValueNumerical:

 * [➞numericalValue](valueNumerical__numericalValue.md)  <sub>1..1</sub>
     * Description: The quantitative value, which can be an integer or a float.
     * Range: [Decimal](types/Decimal.md)
