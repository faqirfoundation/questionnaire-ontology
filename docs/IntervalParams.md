

# Class: IntervalParams 


_Parameters for interval values, including minimum and maximum values._





URI: [phro:IntervalParams](https://ns.faqir.org/phr-o#IntervalParams)





```mermaid
 classDiagram
    class IntervalParams
    click IntervalParams href "../IntervalParams/"
      IntervalParams : maxLabel
        
      IntervalParams : maxValue
        
      IntervalParams : minLabel
        
      IntervalParams : minValue
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [minValue](minValue.md) | 0..1 <br/> [Float](Float.md) | The minimum value of the interval | direct |
| [minLabel](minLabel.md) | 0..1 <br/> [String](String.md) | The label for the minimum value of the interval | direct |
| [maxValue](maxValue.md) | 0..1 <br/> [Float](Float.md) | The maximum value of the interval | direct |
| [maxLabel](maxLabel.md) | 0..1 <br/> [String](String.md) | The label for the maximum value of the interval | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoQuestion](QoQuestion.md) | [qo_intervalParams](qo_intervalParams.md) | range | [IntervalParams](IntervalParams.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:IntervalParams |
| native | qo:IntervalParams |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntervalParams
description: Parameters for interval values, including minimum and maximum values.
from_schema: https://ns.faqir.org/q-o
attributes:
  minValue:
    name: minValue
    description: The minimum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:minValue
    domain_of:
    - IntervalParams
    range: float
    required: false
  minLabel:
    name: minLabel
    description: The label for the minimum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:minLabel
    domain_of:
    - IntervalParams
    range: string
    required: false
  maxValue:
    name: maxValue
    description: The maximum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:maxValue
    domain_of:
    - IntervalParams
    range: float
    required: false
  maxLabel:
    name: maxLabel
    description: The label for the maximum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:maxLabel
    domain_of:
    - IntervalParams
    range: string
    required: false
class_uri: phro:IntervalParams

```
</details>

### Induced

<details>
```yaml
name: IntervalParams
description: Parameters for interval values, including minimum and maximum values.
from_schema: https://ns.faqir.org/q-o
attributes:
  minValue:
    name: minValue
    description: The minimum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:minValue
    alias: minValue
    owner: IntervalParams
    domain_of:
    - IntervalParams
    range: float
    required: false
  minLabel:
    name: minLabel
    description: The label for the minimum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:minLabel
    alias: minLabel
    owner: IntervalParams
    domain_of:
    - IntervalParams
    range: string
    required: false
  maxValue:
    name: maxValue
    description: The maximum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:maxValue
    alias: maxValue
    owner: IntervalParams
    domain_of:
    - IntervalParams
    range: float
    required: false
  maxLabel:
    name: maxLabel
    description: The label for the maximum value of the interval.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: phro:maxLabel
    alias: maxLabel
    owner: IntervalParams
    domain_of:
    - IntervalParams
    range: string
    required: false
class_uri: phro:IntervalParams

```
</details>