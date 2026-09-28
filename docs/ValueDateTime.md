

# Class: ValueDateTime 


_A date and time value, typically in ISO 8601 format._





URI: [phro:ValueDateTime](https://ns.faqir.org/phr-o#ValueDateTime)






```mermaid
 classDiagram
    class ValueDateTime
    click ValueDateTime href "../ValueDateTime"
      ValueDateTime : dateTimeValue
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [dateTimeValue](dateTimeValue.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time value in ISO 8601 format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoAnswer](QoAnswer.md) | [qo_answerValue](qo_answerValue.md) | any_of[range] | [ValueDateTime](ValueDateTime.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:ValueDateTime |
| native | qo:ValueDateTime |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValueDateTime
description: A date and time value, typically in ISO 8601 format.
from_schema: https://ns.faqir.org/q-o
attributes:
  dateTimeValue:
    name: dateTimeValue
    description: The date and time value in ISO 8601 format.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: xsd:dateTime
    domain_of:
    - ValueDateTime
    range: datetime
class_uri: phro:ValueDateTime

```
</details>

### Induced

<details>
```yaml
name: ValueDateTime
description: A date and time value, typically in ISO 8601 format.
from_schema: https://ns.faqir.org/q-o
attributes:
  dateTimeValue:
    name: dateTimeValue
    description: The date and time value in ISO 8601 format.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: xsd:dateTime
    alias: dateTimeValue
    owner: ValueDateTime
    domain_of:
    - ValueDateTime
    range: datetime
class_uri: phro:ValueDateTime

```
</details>