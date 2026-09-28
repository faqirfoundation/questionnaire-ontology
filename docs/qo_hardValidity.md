

# Slot: qo_hardValidity 


_if true, the temporal duration is a strict deadline; if false, it is an orientative guideline._





URI: [qo:hardValidity](https://ns.faqir.org/q-o#hardValidity)
Alias: qo_hardValidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:hardValidity |
| native | qo:qo_hardValidity |




## LinkML Source

<details>
```yaml
name: qo_hardValidity
description: if true, the temporal duration is a strict deadline; if false, it is
  an orientative guideline.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:hardValidity
ifabsent: 'False'
alias: qo_hardValidity
domain_of:
- qo_OrderedQuestion
range: boolean
required: false

```
</details>