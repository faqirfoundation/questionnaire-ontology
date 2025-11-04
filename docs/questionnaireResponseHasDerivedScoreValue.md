

# Slot: questionnaireResponseHasDerivedScoreValue 


_The ScoreValue that is calculated from this QuestionnaireResponse's answers._





URI: [faqir:questionnaireResponseHasDerivedScoreValue](https://faqir.org/datamodel/questionnaireResponseHasDerivedScoreValue)
Alias: questionnaireResponseHasDerivedScoreValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [ScoreValue](ScoreValue.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnaireResponseHasDerivedScoreValue |
| native | https://w3id.org/faqir/datamodel/questionnaireResponseHasDerivedScoreValue |




## LinkML Source

<details>
```yaml
name: questionnaireResponseHasDerivedScoreValue
description: The ScoreValue that is calculated from this QuestionnaireResponse's answers.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: QuestionnaireResponse
slot_uri: faqir:questionnaireResponseHasDerivedScoreValue
alias: questionnaireResponseHasDerivedScoreValue
domain_of:
- QuestionnaireResponse
inverse: scoreValueDerivedFromQuestionnaireResponse
range: ScoreValue
required: false
multivalued: true

```
</details>