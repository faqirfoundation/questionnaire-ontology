

# Slot: prov_wasGeneratedBy 


_Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation._





URI: [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy)
Alias: prov_wasGeneratedBy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [OwlThing](OwlThing.md) | This defines IOT as the set of OWL individuals |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |







## Properties

* Range: [SuloProcess](SuloProcess.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasGeneratedBy |
| native | qo:prov_wasGeneratedBy |




## LinkML Source

<details>
```yaml
name: prov_wasGeneratedBy
description: Generation is the completion of production of a new entity by an activity.
  This entity did not exist before generation and becomes available for usage after
  this generation.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: owl_Thing
slot_uri: prov:wasGeneratedBy
alias: prov_wasGeneratedBy
domain_of:
- owl_Thing
range: sulo_Process
required: false
multivalued: true

```
</details>