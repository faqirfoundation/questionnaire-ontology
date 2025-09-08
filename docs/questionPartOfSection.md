

# Slot: questionPartOfSection 


_The Section that this Question is part of._





URI: [datamodel:questionPartOfSection](https://w3id.org/faqir/datamodel/questionPartOfSection)
Alias: questionPartOfSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Question](Question.md) | A question in the questionnaire |  no  |







## Properties

* Range: [Section](Section.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:questionPartOfSection |
| native | https://w3id.org/faqir/datamodel/questionPartOfSection |
| undefined | fhir:Questionnaire.item |




## LinkML Source

<details>
```yaml
name: questionPartOfSection
description: The Section that this Question is part of.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item
rank: 1000
domain: Question
slot_uri: datamodel:questionPartOfSection
alias: questionPartOfSection
domain_of:
- Question
inverse: sectionHasQuestion
range: Section
required: false
multivalued: true

```
</details>