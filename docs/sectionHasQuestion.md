

# Slot: sectionHasQuestion 


_The Question that is part of this Section._





URI: [datamodel:sectionHasQuestion](https://w3id.org/faqir/datamodel/sectionHasQuestion)
Alias: sectionHasQuestion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A section of questions in the questionnaire |  no  |







## Properties

* Range: [Question](Question.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | datamodel:sectionHasQuestion |
| native | https://w3id.org/faqir/datamodel/sectionHasQuestion |
| undefined | fhir:Questionnaire.item.where(type='question') |




## LinkML Source

<details>
```yaml
name: sectionHasQuestion
description: The Question that is part of this Section.
from_schema: https://w3id.org/faqir/datamodel
mappings:
- fhir:Questionnaire.item.where(type='question')
rank: 1000
domain: Section
slot_uri: datamodel:sectionHasQuestion
alias: sectionHasQuestion
domain_of:
- Section
inverse: questionPartOfSection
range: Question
required: false
multivalued: true

```
</details>