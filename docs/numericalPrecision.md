

# Slot: numericalPrecision 


_The precision of the quantitative value, e.g. number of decimal places._





URI: [phro:precision](https://ns.faqir.org/phr-o#precision)
Alias: numericalPrecision

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NumericalParams](NumericalParams.md) | Parameters for quantitative values, including unit and precision |  no  |






## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 0




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:precision |
| native | qo:numericalPrecision |




## LinkML Source

<details>
```yaml
name: numericalPrecision
description: The precision of the quantitative value, e.g. number of decimal places.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: phro:precision
alias: numericalPrecision
owner: NumericalParams
domain_of:
- NumericalParams
range: integer
required: false
minimum_value: 0

```
</details>