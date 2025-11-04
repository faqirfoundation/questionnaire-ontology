

# Slot: questionnaireResponseHasAnswer 


_The Answer that is part of this QuestionnaireResponse._





URI: [faqir:questionnaireResponseHasAnswer](https://faqir.org/datamodel/questionnaireResponseHasAnswer)
Alias: questionnaireResponseHasAnswer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [Answer](Answer.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnaireResponseHasAnswer |
| native | https://w3id.org/faqir/datamodel/questionnaireResponseHasAnswer |
| undefined | fhir:questionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: questionnaireResponseHasAnswer
description: The Answer that is part of this QuestionnaireResponse.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:questionnaireResponse.item.answer
rank: 1000
domain: QuestionnaireResponse
slot_uri: faqir:questionnaireResponseHasAnswer
alias: questionnaireResponseHasAnswer
domain_of:
- QuestionnaireResponse
inverse: answerInQuestionnaireResponse
range: Answer
required: true
multivalued: true

```
</details>