

# Class: ValueCoding 


_A coded value with a unique code for each display text, typically used for standardized questionnaires._





URI: [fhir:Coding](http://hl7.org/fhir/Coding)






```mermaid
 classDiagram
    class ValueCoding
    click ValueCoding href "../ValueCoding"
      ValueCoding : code
        
      ValueCoding : display
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [code](code.md) | 1 <br/> [String](String.md) | The code representing the value (e | direct |
| [display](display.md) | 1 <br/> [String](String.md) | The human-readable display text for the code (e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SarefPropertyValue](SarefPropertyValue.md) | [fhir_valueCodeableConcept](fhir_valueCodeableConcept.md) | range | [ValueCoding](ValueCoding.md) |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | [fhir_valueCodeableConcept](fhir_valueCodeableConcept.md) | range | [ValueCoding](ValueCoding.md) |
| [QoQuestion](QoQuestion.md) | [qo_codingParams](qo_codingParams.md) | range | [ValueCoding](ValueCoding.md) |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | [fhir_valueCodeableConcept](fhir_valueCodeableConcept.md) | range | [ValueCoding](ValueCoding.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:Coding |
| native | qo:ValueCoding |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValueCoding
description: A coded value with a unique code for each display text, typically used
  for standardized questionnaires.
from_schema: https://ns.faqir.org/q-o
attributes:
  code:
    name: code
    description: The code representing the value (e.g. code '1' for value 'Yes').
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: fhir:code
    domain_of:
    - ValueCoding
    range: string
    required: true
  display:
    name: display
    description: The human-readable display text for the code (e.g. code '1' for value
      'Yes').
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: fhir:display
    domain_of:
    - ValueCoding
    range: string
    required: true
class_uri: fhir:Coding

```
</details>

### Induced

<details>
```yaml
name: ValueCoding
description: A coded value with a unique code for each display text, typically used
  for standardized questionnaires.
from_schema: https://ns.faqir.org/q-o
attributes:
  code:
    name: code
    description: The code representing the value (e.g. code '1' for value 'Yes').
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: fhir:code
    alias: code
    owner: ValueCoding
    domain_of:
    - ValueCoding
    range: string
    required: true
  display:
    name: display
    description: The human-readable display text for the code (e.g. code '1' for value
      'Yes').
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: fhir:display
    alias: display
    owner: ValueCoding
    domain_of:
    - ValueCoding
    range: string
    required: true
class_uri: fhir:Coding

```
</details>