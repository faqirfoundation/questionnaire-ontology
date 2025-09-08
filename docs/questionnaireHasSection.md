

# Slot: questionnaireHasSection 


_The Section that is part of this Questionnaire._





URI: [datamodel:questionnaireHasSection](https://w3id.org/faqir/datamodel/questionnaireHasSection)
Alias: questionnaireHasSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [Section](Section.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:questionnaireHasSection |
| native | https://w3id.org/faqir/datamodel/questionnaireHasSection |
| undefined | fhir:Questionnaire.item.where(type='group') |




## LinkML Source

<details>
```yaml
name: questionnaireHasSection
description: The Section that is part of this Questionnaire.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='group')
rank: 1000
domain: Questionnaire
slot_uri: datamodel:questionnaireHasSection
alias: questionnaireHasSection
domain_of:
- Questionnaire
inverse: sectionPartOfQuestionnaire
range: Section
required: false
multivalued: true

```
</details>