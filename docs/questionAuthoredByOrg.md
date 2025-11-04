

# Slot: questionAuthoredByOrg 


_The organization that has designed this Question._





URI: [faqir:questionAuthoredByOrg](https://faqir.org/datamodel/questionAuthoredByOrg)
Alias: questionAuthoredByOrg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionAuthoredByOrg |
| native | https://w3id.org/faqir/datamodel/questionAuthoredByOrg |




## LinkML Source

<details>
```yaml
name: questionAuthoredByOrg
description: The organization that has designed this Question.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Question
slot_uri: faqir:questionAuthoredByOrg
alias: questionAuthoredByOrg
domain_of:
- Question
inverse: organizationAuthorsQuestion
range: Organization
required: false
multivalued: true

```
</details>