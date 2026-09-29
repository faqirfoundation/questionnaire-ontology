

# Slot: saref_hasPropertyValue 


_Links a feature kind, a feature of interest, or a property of interest, to a property value._





URI: [saref:hasPropertyValue](https://saref.etsi.org/core/hasPropertyValue)
Alias: saref_hasPropertyValue


## Inheritance

* **saref_hasPropertyValue**
    * [fhir_status](fhir_status.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  no  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |







## Properties

* Range: [SarefPropertyValue](SarefPropertyValue.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | saref:hasPropertyValue |
| native | qo:saref_hasPropertyValue |




## LinkML Source

<details>
```yaml
name: saref_hasPropertyValue
description: Links a feature kind, a feature of interest, or a property of interest,
  to a property value.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: saref:hasPropertyValue
alias: saref_hasPropertyValue
domain_of:
- foaf_Agent
- sulo_Process
- prov_Entity
range: saref_PropertyValue
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>