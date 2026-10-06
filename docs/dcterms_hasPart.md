

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
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |







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