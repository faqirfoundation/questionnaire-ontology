

# Slot: quantitativeValue 


_The quantitative value, which can be an integer or a float._





URI: [https://w3id.org/faqir/datamodel/quantitativeValue](https://w3id.org/faqir/datamodel/quantitativeValue)
Alias: quantitativeValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Weight](Weight.md) | Weight |  no  |
| [ValueNumberInInterval](ValueNumberInInterval.md) | A number that falls within a specified interval, with a coding for the value |  no  |
| [QuantitativeValue](QuantitativeValue.md) | Base class for quantitative values with units |  no  |







## Properties

* Range: [Decimal](Decimal.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/quantitativeValue |
| native | https://w3id.org/faqir/datamodel/quantitativeValue |




## LinkML Source

<details>
```yaml
name: quantitativeValue
description: The quantitative value, which can be an integer or a float.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: quantitativeValue
owner: QuantitativeValue
domain_of:
- QuantitativeValue
range: decimal
required: true

```
</details>