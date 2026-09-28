

# Slot: prov_type 


_The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs._





URI: [prov:type](http://www.w3.org/ns/prov#type)
Alias: prov_type

<!-- no inheritance hierarchy -->





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
| [QoQuestion](QoQuestion.md) | A question |  yes  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |







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
domain: owl_Thing
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