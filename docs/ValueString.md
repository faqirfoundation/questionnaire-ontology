

# Class: ValueString 


_A string value, typically used for text or identifiers._





URI: [phro:ValueString](https://ns.faqir.org/phr-o#ValueString)






```mermaid
 classDiagram
    class ValueString
    click ValueString href "../ValueString"
      ValueString : stringValue
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [stringValue](stringValue.md) | 0..1 <br/> [String](String.md) | The string value, which can be any text | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoAnswer](QoAnswer.md) | [qo_answerValue](qo_answerValue.md) | any_of[range] | [ValueString](ValueString.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phro:ValueString |
| native | qo:ValueString |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValueString
description: A string value, typically used for text or identifiers.
from_schema: https://ns.faqir.org/q-o
attributes:
  stringValue:
    name: stringValue
    description: The string value, which can be any text.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: xsd:string
    domain_of:
    - ValueString
    range: string
class_uri: phro:ValueString

```
</details>

### Induced

<details>
```yaml
name: ValueString
description: A string value, typically used for text or identifiers.
from_schema: https://ns.faqir.org/q-o
attributes:
  stringValue:
    name: stringValue
    description: The string value, which can be any text.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: xsd:string
    alias: stringValue
    owner: ValueString
    domain_of:
    - ValueString
    range: string
class_uri: phro:ValueString

```
</details>