

# Slot: questionOrder 


_Question position in the questionnaire or section (1-based index)._





URI: [https://w3id.org/faqir/datamodel/questionOrder](https://w3id.org/faqir/datamodel/questionOrder)
Alias: questionOrder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrderedQuestion](OrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True

* Minimum Value: 1





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/questionOrder |
| native | https://w3id.org/faqir/datamodel/questionOrder |




## LinkML Source

<details>
```yaml
name: questionOrder
description: Question position in the questionnaire or section (1-based index).
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: questionOrder
owner: OrderedQuestion
domain_of:
- OrderedQuestion
range: integer
required: true
minimum_value: 1

```
</details>