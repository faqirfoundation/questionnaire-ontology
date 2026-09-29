

# Slot: dcterms_isPartOf 


_A related resource in which the described resource is physically or logically included._





URI: [dcterms:isPartOf](http://purl.org/dc/terms/isPartOf)
Alias: dcterms_isPartOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  yes  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  yes  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |







## Properties

* Range: [OwlThing](OwlThing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:isPartOf |
| native | qo:dcterms_isPartOf |




## LinkML Source

<details>
```yaml
name: dcterms_isPartOf
description: A related resource in which the described resource is physically or logically
  included.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: dcterms:isPartOf
alias: dcterms_isPartOf
domain_of:
- foaf_Agent
- sulo_Process
- prov_Entity
inverse: dcterms_hasPart
range: owl_Thing
required: false
multivalued: true

```
</details>