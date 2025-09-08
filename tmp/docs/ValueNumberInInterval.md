
# Class: ValueNumberInInterval

A number that falls within a specified interval, with a coding for the value.

URI: [datamodel:ValueNumberInInterval](https://w3id.org/faqir/datamodel/ValueNumberInInterval)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueNumerical],[ValueCoding]<numberInIntervalValue%201..1-++[ValueNumberInInterval&#124;numericalValue(i):decimal],[ValueNumerical]^-[ValueNumberInInterval],[ValueCoding])](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueNumerical],[ValueCoding]<numberInIntervalValue%201..1-++[ValueNumberInInterval&#124;numericalValue(i):decimal],[ValueNumerical]^-[ValueNumberInInterval],[ValueCoding])

## Parents

 *  is_a: [ValueNumerical](ValueNumerical.md) - Base class for quantitative values, they may have units and precision.

## Attributes


### Own

 * [➞numberInIntervalValue](valueNumberInInterval__numberInIntervalValue.md)  <sub>1..1</sub>
     * Description: The actual number that falls within the specified interval.
     * Range: [ValueCoding](ValueCoding.md)

### Inherited from ValueNumerical:

 * [➞numericalValue](valueNumerical__numericalValue.md)  <sub>1..1</sub>
     * Description: The quantitative value, which can be an integer or a float.
     * Range: [Decimal](types/Decimal.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | datamodel:ValueNumberInInterval |