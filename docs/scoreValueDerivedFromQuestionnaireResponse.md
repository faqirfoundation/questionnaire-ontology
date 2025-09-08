

# Slot: scoreValueDerivedFromQuestionnaireResponse 


_The QuestionnaireResponse that contains the answers this ScoreValue is calculated from._





URI: [faqir:scoreValueDerivedFromQuestionnaireResponse](https://faqir.org/datamodel/scoreValueDerivedFromQuestionnaireResponse)
Alias: scoreValueDerivedFromQuestionnaireResponse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScoreValue](ScoreValue.md) | The score value calculated from a QuestionnaireResponse following a ScoreDefi... |  no  |







## Properties

* Range: [QuestionnaireResponse](QuestionnaireResponse.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:scoreValueDerivedFromQuestionnaireResponse |
| native | https://w3id.org/faqir/datamodel/scoreValueDerivedFromQuestionnaireResponse |




## LinkML Source

<details>
```yaml
name: scoreValueDerivedFromQuestionnaireResponse
description: The QuestionnaireResponse that contains the answers this ScoreValue is
  calculated from.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: ScoreValue
slot_uri: faqir:scoreValueDerivedFromQuestionnaireResponse
alias: scoreValueDerivedFromQuestionnaireResponse
domain_of:
- ScoreValue
inverse: questionnaireResponseHasDerivedScoreValue
range: QuestionnaireResponse
required: true
multivalued: true

```
</details>