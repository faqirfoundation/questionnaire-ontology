

# Class: QuantityValue 


_A measured amount (or an amount that can potentially be measured)._





URI: [fhir:Quantity](http://hl7.org/fhir/Quantity)






```mermaid
 classDiagram
    class QuantityValue
    click QuantityValue href "../QuantityValue"
      QuantityValue : saref_hasValue
        
      QuantityValue : saref_isMeasuredIn
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [saref_isMeasuredIn](saref_isMeasuredIn.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A relationship identifying the unit of measure used for a certain entity | direct |
| [saref_hasValue](saref_hasValue.md) | 0..1 <br/> [String](String.md)&nbsp;or&nbsp;<br />[Integer](Integer.md)&nbsp;or&nbsp;<br />[Float](Float.md)&nbsp;or&nbsp;<br />[Double](Double.md)&nbsp;or&nbsp;<br />[Decimal](Decimal.md)&nbsp;or&nbsp;<br />[Date](Date.md)&nbsp;or&nbsp;<br />[Datetime](Datetime.md)&nbsp;or&nbsp;<br />[Uriorcurie](Uriorcurie.md)&nbsp;or&nbsp;<br />[String](String.md) | Value of a property value expressed as an RDF literal | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FhirValueRatio](FhirValueRatio.md) | [numerator](numerator.md) | range | [QuantityValue](QuantityValue.md) |
| [FhirValueRatio](FhirValueRatio.md) | [denominator](denominator.md) | range | [QuantityValue](QuantityValue.md) |
| [FhirReferenceRange](FhirReferenceRange.md) | [lowRange](lowRange.md) | range | [QuantityValue](QuantityValue.md) |
| [FhirReferenceRange](FhirReferenceRange.md) | [highRange](highRange.md) | range | [QuantityValue](QuantityValue.md) |
| [FhirReferenceRange](FhirReferenceRange.md) | [normalValue](normalValue.md) | range | [QuantityValue](QuantityValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:Quantity |
| native | qo:QuantityValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QuantityValue
description: A measured amount (or an amount that can potentially be measured).
from_schema: https://ns.faqir.org/q-o
slots:
- saref_isMeasuredIn
- saref_hasValue
class_uri: fhir:Quantity

```
</details>

### Induced

<details>
```yaml
name: QuantityValue
description: A measured amount (or an amount that can potentially be measured).
from_schema: https://ns.faqir.org/q-o
attributes:
  saref_isMeasuredIn:
    name: saref_isMeasuredIn
    description: A relationship identifying the unit of measure used for a certain
      entity.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: saref:isMeasuredIn
    alias: saref_isMeasuredIn
    owner: QuantityValue
    domain_of:
    - QuantityValue
    - time_Duration
    range: uriorcurie
    required: false
    multivalued: false
    pattern: '^ucum:'
  saref_hasValue:
    name: saref_hasValue
    description: Value of a property value expressed as an RDF literal. Note that,
      even if decimal values are expected, values could use other datatypes.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: saref:hasValue
    alias: saref_hasValue
    owner: QuantityValue
    domain_of:
    - saref_PropertyValue
    - QuantityValue
    - time_Duration
    range: string
    required: false
    multivalued: false
    any_of:
    - range: integer
    - range: float
    - range: double
    - range: decimal
    - range: date
    - range: datetime
    - range: uriorcurie
    - range: string
class_uri: fhir:Quantity

```
</details>