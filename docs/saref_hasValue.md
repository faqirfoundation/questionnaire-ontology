

# Slot: saref_hasValue 


_Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes._





URI: [saref:hasValue](https://saref.etsi.org/core/hasValue)
Alias: saref_hasValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |  yes  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | The status of the questionnaire, indicating whether it is 	draft, active, ret... |  yes  |
| [QuantityValue](QuantityValue.md) | A measured amount (or an amount that can potentially be measured) |  no  |
| [TimeDuration](TimeDuration.md) | Duration of a temporal extent expressed as a decimal number scaled by a tempo... |  no  |







## Properties

* Range: [String](String.md)&nbsp;or&nbsp;<br />[Integer](Integer.md)&nbsp;or&nbsp;<br />[Float](Float.md)&nbsp;or&nbsp;<br />[Double](Double.md)&nbsp;or&nbsp;<br />[Decimal](Decimal.md)&nbsp;or&nbsp;<br />[Date](Date.md)&nbsp;or&nbsp;<br />[Datetime](Datetime.md)&nbsp;or&nbsp;<br />[Uriorcurie](Uriorcurie.md)&nbsp;or&nbsp;<br />[String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | saref:hasValue |
| native | qo:saref_hasValue |




## LinkML Source

<details>
```yaml
name: saref_hasValue
description: Value of a property value expressed as an RDF literal. Note that, even
  if decimal values are expected, values could use other datatypes.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: saref:hasValue
alias: saref_hasValue
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

```
</details>