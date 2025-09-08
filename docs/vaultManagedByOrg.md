

# Slot: vaultManagedByOrg 


_Organization managing this vault._





URI: [https://w3id.org/faqir/datamodel/vaultManagedByOrg](https://w3id.org/faqir/datamodel/vaultManagedByOrg)
Alias: vaultManagedByOrg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vault](Vault.md) | The FAQIR healthdata vault |  no  |







## Properties

* Range: [Organization](Organization.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/faqir/datamodel/vaultManagedByOrg |
| native | https://w3id.org/faqir/datamodel/vaultManagedByOrg |




## LinkML Source

<details>
```yaml
name: vaultManagedByOrg
description: Organization managing this vault.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Vault
alias: vaultManagedByOrg
domain_of:
- Vault
inverse: organizationManagesVault
range: Organization
required: true
multivalued: false

```
</details>