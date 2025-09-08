

# Slot: isResponseFor 


_The Questionnaire that this QuestionnaireResponse is for._





URI: [datamodel:isResponseFor](https://w3id.org/faqir/datamodel/isResponseFor)
Alias: isResponseFor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:isResponseFor |
| native | https://w3id.org/faqir/datamodel/isResponseFor |
| undefined | fhir:QuestionnaireResponse.questionnaire |




## LinkML Source

<details>
```yaml
name: isResponseFor
description: The Questionnaire that this QuestionnaireResponse is for.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:QuestionnaireResponse.questionnaire
rank: 1000
domain: QuestionnaireResponse
slot_uri: datamodel:isResponseFor
alias: isResponseFor
domain_of:
- QuestionnaireResponse
inverse: hasResponse
range: Questionnaire
required: true
multivalued: false

```
</details>