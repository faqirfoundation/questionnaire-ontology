

# Slot: last_updated 


_The date and time when the schema was last updated._





URI: [https://w3id.org/faqir/datamodel/last_updated](https://w3id.org/faqir/datamodel/last_updated)
Alias: last_updated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vault](Vault.md) | The FAQIR healthdata vault |  no  |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [Metadata](Metadata.md) | Base class for metadata tracking (e |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/last_updated |
| native | https://w3id.org/faqir/datamodel/last_updated |




## LinkML Source

<details>
```yaml
name: last_updated
description: The date and time when the schema was last updated.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: last_updated
domain_of:
- Metadata
range: datetime
required: true

```
</details>