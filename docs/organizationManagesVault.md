

# Slot: organizationManagesVault 


_Vault managed by this organization._





URI: [faqir:organizationManagesVault](https://faqir.org/datamodel/organizationManagesVault)
Alias: organizationManagesVault

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An entity acting in a healthcare context |  no  |







## Properties

* Range: [Vault](Vault.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:organizationManagesVault |
| native | https://w3id.org/faqir/datamodel/organizationManagesVault |




## LinkML Source

<details>
```yaml
name: organizationManagesVault
description: Vault managed by this organization.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Organization
slot_uri: faqir:organizationManagesVault
alias: organizationManagesVault
domain_of:
- Organization
inverse: vaultManagedByOrg
range: Vault
required: false
multivalued: true

```
</details>