

# Slot: sectionPartOfQuestionnaire 


_The Questionnaire that this Section is part of._





URI: [datamodel:sectionPartOfQuestionnaire](https://w3id.org/faqir/datamodel/sectionPartOfQuestionnaire)
Alias: sectionPartOfQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A section of questions in the questionnaire |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:sectionPartOfQuestionnaire |
| native | https://w3id.org/faqir/datamodel/sectionPartOfQuestionnaire |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: sectionPartOfQuestionnaire
description: The Questionnaire that this Section is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: Section
slot_uri: datamodel:sectionPartOfQuestionnaire
alias: sectionPartOfQuestionnaire
domain_of:
- Section
inverse: questionnaireHasSection
range: Questionnaire
required: false
multivalued: true

```
</details>