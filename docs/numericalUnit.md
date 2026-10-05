

# Slot: numericalUnit 


_The unit of measure for the quantitative value, from UCUM standard._





URI: [ucum:units](https://unitsofmeasure.org/units)
Alias: numericalUnit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NumericalParams](NumericalParams.md) | Parameters for quantitative values, including unit and precision |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^ucum:`




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ucum:units |
| native | qo:numericalUnit |




## LinkML Source

<details>
```yaml
name: numericalUnit
description: The unit of measure for the quantitative value, from UCUM standard.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: ucum:units
alias: numericalUnit
owner: NumericalParams
domain_of:
- NumericalParams
range: uriorcurie
required: false
pattern: '^ucum:'

```
</details>