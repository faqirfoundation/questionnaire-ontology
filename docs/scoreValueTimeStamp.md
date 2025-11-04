

# Slot: scoreValueTimeStamp 


_Timestamp when the score value was calculated._





URI: [https://w3id.org/faqir/datamodel/scoreValueTimeStamp](https://w3id.org/faqir/datamodel/scoreValueTimeStamp)
Alias: scoreValueTimeStamp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreValue](ScoreValue.md) | The score value calculated from a QuestionnaireResponse following a ScoreDefi... |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/scoreValueTimeStamp |
| native | https://w3id.org/faqir/datamodel/scoreValueTimeStamp |




## LinkML Source

<details>
```yaml
name: scoreValueTimeStamp
description: Timestamp when the score value was calculated.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: scoreValueTimeStamp
owner: ScoreValue
domain_of:
- ScoreValue
range: datetime
required: true

```
</details>