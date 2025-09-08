

# Slot: questionnaireVersion 


_Version of the questionnaire._





URI: [https://w3id.org/faqir/datamodel/questionnaireVersion](https://w3id.org/faqir/datamodel/questionnaireVersion)
Alias: questionnaireVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^\d+\.\d+\.\d+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/questionnaireVersion |
| native | https://w3id.org/faqir/datamodel/questionnaireVersion |




## LinkML Source

<details>
```yaml
name: questionnaireVersion
description: Version of the questionnaire.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: questionnaireVersion
owner: Questionnaire
domain_of:
- Questionnaire
range: string
required: true
pattern: ^\d+\.\d+\.\d+$

```
</details>