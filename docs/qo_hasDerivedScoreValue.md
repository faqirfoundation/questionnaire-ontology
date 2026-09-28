

# Slot: qo_hasDerivedScoreValue 


_The ScoreValue that is calculated from this QuestionnaireResponse's answers._





URI: [qo:hasDerivedScoreValue](https://ns.faqir.org/q-o#hasDerivedScoreValue)
Alias: qo_hasDerivedScoreValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [QoScoreValue](QoScoreValue.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:hasDerivedScoreValue |
| native | qo:qo_hasDerivedScoreValue |




## LinkML Source

<details>
```yaml
name: qo_hasDerivedScoreValue
description: The ScoreValue that is calculated from this QuestionnaireResponse's answers.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: qo_QuestionnaireResponse
slot_uri: qo:hasDerivedScoreValue
alias: qo_hasDerivedScoreValue
domain_of:
- qo_QuestionnaireResponse
range: qo_ScoreValue
required: false
multivalued: true

```
</details>