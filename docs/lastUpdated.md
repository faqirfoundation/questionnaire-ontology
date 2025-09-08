

# Slot: lastUpdated 


_The date and time when the entity was last updated._





URI: [https://w3id.org/faqir/datamodel/lastUpdated](https://w3id.org/faqir/datamodel/lastUpdated)
Alias: lastUpdated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Metadata](Metadata.md) | Base class for metadata tracking (e |  no  |
| [Vault](Vault.md) | The FAQIR healthdata vault |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/lastUpdated |
| native | https://w3id.org/faqir/datamodel/lastUpdated |




## LinkML Source

<details>
```yaml
name: lastUpdated
description: The date and time when the entity was last updated.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
alias: lastUpdated
owner: Metadata
domain_of:
- Metadata
range: datetime
required: true

```
</details>