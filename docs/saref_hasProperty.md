

# Slot: saref_hasProperty 


_Links a feature kind or a feature of interest to one of its properties._





URI: [saref:hasProperty](https://saref.etsi.org/core/hasProperty)
Alias: saref_hasProperty

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
| [QoQuestion](QoQuestion.md) | A question |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |







## Properties

* Range: [SarefProperty](SarefProperty.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | saref:hasProperty |
| native | qo:saref_hasProperty |
| undefined | ssn:hasProperty |




## LinkML Source

<details>
```yaml
name: saref_hasProperty
description: Links a feature kind or a feature of interest to one of its properties.
from_schema: https://ns.faqir.org/q-o
mappings:
- ssn:hasProperty
rank: 1000
domain: owl_Thing
slot_uri: saref:hasProperty
alias: saref_hasProperty
domain_of:
- foaf_Agent
- sulo_Process
- prov_Entity
range: saref_Property
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>