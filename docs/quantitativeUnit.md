

# Slot: quantitativeUnit 


_The unit of measure for the quantitative value, from UCUM standard._





URI: [ucum:units](https://unitsofmeasure.org/units)
Alias: quantitativeUnit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Weight](Weight.md) | Weight |  no  |
| [ValueNumberInInterval](ValueNumberInInterval.md) | A number that falls within a specified interval, with a coding for the value |  no  |
| [QuantitativeValue](QuantitativeValue.md) | Base class for quantitative values with units |  no  |







## Properties

* Range: [UnitOfMeasure](UnitOfMeasure.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ucum:units |
| native | https://w3id.org/faqir/datamodel/quantitativeUnit |




## LinkML Source

<details>
```yaml
name: quantitativeUnit
description: The unit of measure for the quantitative value, from UCUM standard.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
slot_uri: ucum:units
alias: quantitativeUnit
owner: QuantitativeValue
domain_of:
- QuantitativeValue
range: UnitOfMeasure
required: true

```
</details>