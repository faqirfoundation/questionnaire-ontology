

# Slot: rdfs_label 


_human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals._





URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)
Alias: rdfs_label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedSection](QoOrderedSection.md) | Section's position within a specific questionnaire or section |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | The status of the questionnaire, indicating whether it is 	draft, active, ret... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |
| [QoQuestion](QoQuestion.md) | A question |  no  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |
| [S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |  no  |
| [QoAnswer](QoAnswer.md) | Answer in the questionnaire response |  no  |
| [FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [OwlThing](OwlThing.md) | This defines IOT as the set of OWL individuals |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | qo:rdfs_label |




## LinkML Source

<details>
```yaml
name: rdfs_label
description: human-readable version of a resource's name. Multilingual labels are
  supported using the language tagging facility of RDF literals.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: owl_Thing
slot_uri: rdfs:label
alias: rdfs_label
domain_of:
- owl_Thing
range: string
required: true
multivalued: true

```
</details>