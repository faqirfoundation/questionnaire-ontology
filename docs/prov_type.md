

# Slot: prov_type 


_The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs._





URI: [prov:type](http://www.w3.org/ns/prov#type)
Alias: prov_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  yes  |
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

* Range: [Uriorcurie](Uriorcurie.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:type |
| native | qo:prov_type |
| exact | rdf:type, sphn:hasTypeCode |
| narrow | schema:procedureType |




## LinkML Source

<details>
```yaml
name: prov_type
description: The attribute prov:type provides further typing information for any construct
  with an optional set of attribute-value pairs.
from_schema: https://ns.faqir.org/q-o
exact_mappings:
- rdf:type
- sphn:hasTypeCode
narrow_mappings:
- schema:procedureType
rank: 1000
slot_uri: prov:type
alias: prov_type
domain_of:
- foaf_Agent
- sulo_Process
- prov_Entity
range: uriorcurie
required: false
multivalued: true

```
</details>