

# Slot: dcterms_creator 


_An entity responsible for making the resource._





URI: [dcterms:creator](http://purl.org/dc/terms/creator)
Alias: dcterms_creator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  yes  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  yes  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  yes  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |






## Properties

* Range: [FoafAgent](FoafAgent.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:creator |
| native | qo:dcterms_creator |




## LinkML Source

<details>
```yaml
name: dcterms_creator
description: An entity responsible for making the resource.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: dcterms:creator
alias: dcterms_creator
domain_of:
- foaf_Agent
- sulo_Process
- prov_Entity
range: foaf_Agent
required: false
multivalued: true

```
</details>