

# Slot: procedurePerformedByOrg 


_Organization that manages and perfomes this procedure._





URI: [faqir:procedurePerformedByOrg](https://faqir.org/datamodel/procedurePerformedByOrg)
Alias: procedurePerformedByOrg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Procedure](Procedure.md) | A clinical or administrative process that uses resources like questionnaires |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:procedurePerformedByOrg |
| native | https://w3id.org/faqir/datamodel/procedurePerformedByOrg |




## LinkML Source

<details>
```yaml
name: procedurePerformedByOrg
description: Organization that manages and perfomes this procedure.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Procedure
slot_uri: faqir:procedurePerformedByOrg
alias: procedurePerformedByOrg
domain_of:
- Procedure
inverse: organizationPerformsProcedure
range: Organization
required: false
multivalued: true

```
</details>