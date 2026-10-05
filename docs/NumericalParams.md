

# Class: NumericalParams 


_Parameters for quantitative values, including unit and precision._





URI: [phro:NumericalParams](https://ns.faqir.org/phr-o#NumericalParams)





```mermaid
 classDiagram
    class NumericalParams
    click NumericalParams href "../NumericalParams/"
      NumericalParams : numericalPrecision
        
      NumericalParams : numericalUnit
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [numericalUnit](numericalUnit.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The unit of measure for the quantitative value, from UCUM standard | direct |
| [numericalPrecision](numericalPrecision.md) | 0..1 <br/> [Integer](Integer.md) | The precision of the quantitative value, e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoQuestion](QoQuestion.md) | [qo_numericalParams](qo_numericalParams.md) | range | [NumericalParams](NumericalParams.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:NumericalParams |
| native | qo:NumericalParams |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NumericalParams
description: Parameters for quantitative values, including unit and precision.
from_schema: https://ns.faqir.org/q-o
attributes:
  numericalUnit:
    name: numericalUnit
    description: The unit of measure for the quantitative value, from UCUM standard.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: ucum:units
    domain_of:
    - NumericalParams
    range: uriorcurie
    required: false
    pattern: '^ucum:'
  numericalPrecision:
    name: numericalPrecision
    description: The precision of the quantitative value, e.g. number of decimal places.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:precision
    domain_of:
    - NumericalParams
    range: integer
    required: false
    minimum_value: 0
class_uri: phro:NumericalParams

```
</details>

### Induced

<details>
```yaml
name: NumericalParams
description: Parameters for quantitative values, including unit and precision.
from_schema: https://ns.faqir.org/q-o
attributes:
  numericalUnit:
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
  numericalPrecision:
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
class_uri: phro:NumericalParams

```
</details>