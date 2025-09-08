

# Slot: procedureHasQuestionnaire 


_Questionnaires part of this procedure._





URI: [faqir:procedureHasQuestionnaire](https://faqir.org/datamodel/procedureHasQuestionnaire)
Alias: procedureHasQuestionnaire

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Procedure](Procedure.md) | A clinical or administrative process that uses resources like questionnaires |  no  |







## Properties

* Range: [Questionnaire](Questionnaire.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:procedureHasQuestionnaire |
| native | https://w3id.org/faqir/datamodel/procedureHasQuestionnaire |




## LinkML Source

<details>
```yaml
name: procedureHasQuestionnaire
description: Questionnaires part of this procedure.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Procedure
slot_uri: faqir:procedureHasQuestionnaire
alias: procedureHasQuestionnaire
domain_of:
- Procedure
inverse: questionnairePartOfProcedure
range: Questionnaire
required: false
multivalued: true

```
</details>