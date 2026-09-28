

# Slot: dcterms_hasPart 


_A related resource that is included either physically or logically in the described resource._





URI: [dcterms:hasPart](http://purl.org/dc/terms/hasPart)
Alias: dcterms_hasPart


## Inheritance

* **dcterms_hasPart**
    * [qo_question](qo_question.md)
    * [qo_hasOrderedQuestion](qo_hasOrderedQuestion.md)
    * [qo_hasOrderedSection](qo_hasOrderedSection.md)
    * [qo_section](qo_section.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoOrderedSection](QoOrderedSection.md) | Section's position within a specific questionnaire or section |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | The status of the questionnaire, indicating whether it is 	draft, active, ret... |  no  |
| [QoAnswer](QoAnswer.md) | Answer in the questionnaire response |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [QoQuestion](QoQuestion.md) | A question |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |







## Properties

* Range: [OwlThing](OwlThing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:hasPart |
| native | qo:dcterms_hasPart |




## LinkML Source

<details>
```yaml
name: dcterms_hasPart
description: A related resource that is included either physically or logically in
  the described resource.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: owl_Thing
slot_uri: dcterms:hasPart
alias: dcterms_hasPart
domain_of:
- foaf_Agent
- sulo_Process
- prov_Entity
inverse: dcterms_isPartOf
range: owl_Thing
required: false
multivalued: true

```
</details>