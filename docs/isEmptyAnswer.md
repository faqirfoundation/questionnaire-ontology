

# Slot: isEmptyAnswer 


_True if the answer is intentionally empty._





URI: [datamodel:isEmptyAnswer](https://w3id.org/faqir/datamodel/isEmptyAnswer)
Alias: isEmptyAnswer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:isEmptyAnswer |
| native | https://w3id.org/faqir/datamodel/isEmptyAnswer |




## LinkML Source

<details>
```yaml
name: isEmptyAnswer
description: True if the answer is intentionally empty.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
slot_uri: datamodel:isEmptyAnswer
ifabsent: 'False'
alias: isEmptyAnswer
domain_of:
- Answer
range: boolean
required: true

```
</details>