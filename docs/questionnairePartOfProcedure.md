

# Slot: questionnairePartOfProcedure 


_Procedure this questionnaire is part of._





URI: [faqir:questionnairePartOfProcedure](https://faqir.org/datamodel/questionnairePartOfProcedure)
Alias: questionnairePartOfProcedure

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |







## Properties

* Range: [Procedure](Procedure.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faqir:questionnairePartOfProcedure |
| native | https://w3id.org/faqir/datamodel/questionnairePartOfProcedure |




## LinkML Source

<details>
```yaml
name: questionnairePartOfProcedure
description: Procedure this questionnaire is part of.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
domain: Questionnaire
slot_uri: faqir:questionnairePartOfProcedure
alias: questionnairePartOfProcedure
domain_of:
- Questionnaire
inverse: procedureHasQuestionnaire
range: Procedure
required: false
multivalued: true

```
</details>