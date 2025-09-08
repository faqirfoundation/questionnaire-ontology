

# Slot: hasResponseAnswer 


_The Answer that is part of this QuestionnaireResponse._





URI: [datamodel:hasResponseAnswer](https://w3id.org/faqir/datamodel/hasResponseAnswer)
Alias: hasResponseAnswer

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
| self | datamodel:hasResponseAnswer |
| native | https://w3id.org/faqir/datamodel/hasResponseAnswer |
| undefined | fhir:QuestionnaireResponse.item.answer |




## LinkML Source

<details>
```yaml
name: hasResponseAnswer
description: The Answer that is part of this QuestionnaireResponse.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.item.answer
rank: 1000
domain: QuestionnaireResponse
slot_uri: datamodel:hasResponseAnswer
alias: hasResponseAnswer
domain_of:
- QuestionnaireResponse
inverse: isAnswerIn
range: Answer
required: true
multivalued: true

```
</details>