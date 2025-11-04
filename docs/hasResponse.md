

# Slot: hasResponse 


_The QuestionnaireResponse that is associated with this Questionnaire._





URI: [datamodel:hasResponse](https://w3id.org/faqir/datamodel/hasResponse)
Alias: hasResponse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [QuestionnaireResponse](QuestionnaireResponse.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:hasResponse |
| native | https://w3id.org/faqir/datamodel/hasResponse |
| undefined | fhir:QuestionnaireResponse |




## LinkML Source

<details>
```yaml
name: hasResponse
description: The QuestionnaireResponse that is associated with this Questionnaire.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse
rank: 1000
domain: Questionnaire
slot_uri: datamodel:hasResponse
alias: hasResponse
domain_of:
- Questionnaire
inverse: isResponseFor
range: QuestionnaireResponse
multivalued: true

```
</details>