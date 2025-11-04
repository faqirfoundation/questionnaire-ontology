

# Slot: numericalValue 


_The quantitative value, which can be an integer or a float._





URI: [https://w3id.org/faqir/datamodel/numericalValue](https://w3id.org/faqir/datamodel/numericalValue)
Alias: numericalValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Weight](Weight.md) | Weight |  no  |
| [ValueNumerical](ValueNumerical.md) | Base class for quantitative values, they may have units and precision |  no  |







## Properties

* Range: [Decimal](Decimal.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/numericalValue |
| native | https://w3id.org/faqir/datamodel/numericalValue |




## LinkML Source

<details>
```yaml
name: numericalValue
description: The quantitative value, which can be an integer or a float.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: numericalValue
owner: ValueNumerical
domain_of:
- ValueNumerical
range: decimal
required: true

```
</details>