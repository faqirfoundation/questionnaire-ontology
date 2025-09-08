

# Slot: schema_version 


_The version of the schema._





URI: [https://w3id.org/faqir/datamodel/schema_version](https://w3id.org/faqir/datamodel/schema_version)
Alias: schema_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vault](Vault.md) | The FAQIR healthdata vault |  no  |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [Metadata](Metadata.md) | Base class for metadata tracking (e |  no  |







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
| self | https://w3id.org/faqir/datamodel/schema_version |
| native | https://w3id.org/faqir/datamodel/schema_version |




## LinkML Source

<details>
```yaml
name: schema_version
description: The version of the schema.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: schema_version
domain_of:
- Metadata
range: string
recommended: true
pattern: ^\d+\.\d+\.\d+$

```
</details>