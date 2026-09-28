

# Slot: numericalValue 


_The quantitative value, which can be an integer or a float._





URI: [phro:numericalValue](https://ns.faqir.org/phr-o#numericalValue)
Alias: numericalValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ValueNumerical](ValueNumerical.md) |  |  no  |







## Properties

* Range: [Decimal](Decimal.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:numericalValue |
| native | qo:numericalValue |




## LinkML Source

<details>
```yaml
name: numericalValue
description: The quantitative value, which can be an integer or a float.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: phro:numericalValue
alias: numericalValue
owner: ValueNumerical
domain_of:
- ValueNumerical
range: decimal
required: true

```
</details>