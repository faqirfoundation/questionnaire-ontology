

# Slot: intervalQuestionParams 


_Minimum and Maximum limiting the range the answer must be in for the question._





URI: [datamodel:intervalQuestionParams](https://w3id.org/faqir/datamodel/intervalQuestionParams)
Alias: intervalQuestionParams

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [IntervalParams](IntervalParams.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:intervalQuestionParams |
| native | https://w3id.org/faqir/datamodel/intervalQuestionParams |




## LinkML Source

<details>
```yaml
name: intervalQuestionParams
description: Minimum and Maximum limiting the range the answer must be in for the
  question.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
slot_uri: datamodel:intervalQuestionParams
alias: intervalQuestionParams
domain_of:
- Question
range: IntervalParams
required: false
multivalued: true
inlined: false

```
</details>