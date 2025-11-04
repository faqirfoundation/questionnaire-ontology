

# Slot: hasQuestionnaireResponse 


_QuestionnaireResponse authored by this vault's user._





URI: [https://w3id.org/faqir/datamodel/hasQuestionnaireResponse](https://w3id.org/faqir/datamodel/hasQuestionnaireResponse)
Alias: hasQuestionnaireResponse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vault](Vault.md) | The FAQIR healthdata vault |  no  |







## Properties

* Range: [QuestionnaireResponse](QuestionnaireResponse.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/hasQuestionnaireResponse |
| native | https://w3id.org/faqir/datamodel/hasQuestionnaireResponse |




## LinkML Source

<details>
```yaml
name: hasQuestionnaireResponse
description: QuestionnaireResponse authored by this vault's user.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Vault
alias: hasQuestionnaireResponse
domain_of:
- Vault
inverse: questionnaireResponseBySubject
range: QuestionnaireResponse
required: false
multivalued: true

```
</details>