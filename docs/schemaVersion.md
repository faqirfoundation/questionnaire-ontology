

# Slot: schemaVersion 


_The version of the schema._





URI: [https://w3id.org/faqir/datamodel/schemaVersion](https://w3id.org/faqir/datamodel/schemaVersion)
Alias: schemaVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [Vault](Vault.md) | The FAQIR healthdata vault |  no  |
| [Metadata](Metadata.md) | Base class for metadata tracking (e |  no  |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^\d+\.\d+\.\d+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/schemaVersion |
| native | https://w3id.org/faqir/datamodel/schemaVersion |




## LinkML Source

<details>
```yaml
name: schemaVersion
description: The version of the schema.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: schemaVersion
domain_of:
- Metadata
range: string
recommended: true
pattern: ^\d+\.\d+\.\d+$

```
</details>