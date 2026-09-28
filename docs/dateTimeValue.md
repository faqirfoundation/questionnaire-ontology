

# Slot: dateTimeValue 


_The date and time value in ISO 8601 format._





URI: [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime)
Alias: dateTimeValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ValueDateTime](ValueDateTime.md) | A date and time value, typically in ISO 8601 format |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | xsd:dateTime |
| native | qo:dateTimeValue |




## LinkML Source

<details>
```yaml
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

```
</details>