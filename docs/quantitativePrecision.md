

# Slot: quantitativePrecision 


_The precision of the quantitative value, e.g. number of decimal places._





URI: [https://w3id.org/faqir/datamodel/quantitativePrecision](https://w3id.org/faqir/datamodel/quantitativePrecision)
Alias: quantitativePrecision

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Weight](Weight.md) | Weight |  no  |
| [ValueNumberInInterval](ValueNumberInInterval.md) | A number that falls within a specified interval, with a coding for the value |  no  |
| [QuantitativeValue](QuantitativeValue.md) | Base class for quantitative values with units |  no  |







## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 0





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/quantitativePrecision |
| native | https://w3id.org/faqir/datamodel/quantitativePrecision |




## LinkML Source

<details>
```yaml
name: quantitativePrecision
description: The precision of the quantitative value, e.g. number of decimal places.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: quantitativePrecision
owner: QuantitativeValue
domain_of:
- QuantitativeValue
range: integer
minimum_value: 0

```
</details>