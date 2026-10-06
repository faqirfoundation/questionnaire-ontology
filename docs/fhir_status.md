

# Slot: fhir_status 


_A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state._





URI: [fhir:resource-status](http://hl7.org/fhir/resource-status)
Alias: fhir_status


## Inheritance

* [saref_hasPropertyValue](saref_hasPropertyValue.md)
    * **fhir_status**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  yes  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  yes  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
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
| self | fhir:resource-status |
| native | qo:fhir_status |




## LinkML Source

<details>
```yaml
name: fhir_status
description: A code specifying the state of the observation/procedure/questionnaire...
  Generally, this will be the in-progress or completed state.
from_schema: https://ns.faqir.org/q-o
rank: 1000
is_a: saref_hasPropertyValue
slot_uri: fhir:resource-status
alias: fhir_status
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