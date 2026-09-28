

# Slot: prov_hadPrimarySource 


_A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain._





URI: [prov:hadPrimarySource](http://www.w3.org/ns/prov#hadPrimarySource)
Alias: prov_hadPrimarySource

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

* Range: [ProvEntity](ProvEntity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:hadPrimarySource |
| native | qo:prov_hadPrimarySource |




## LinkML Source

<details>
```yaml
name: prov_hadPrimarySource
description: A primary source for a topic refers to something produced by some agent
  with direct experience and knowledge about the topic, at the time of the topic's
  study, without benefit from hindsight. Because of the directness of primary sources,
  they 'speak for themselves' in ways that cannot be captured through the filter of
  secondary sources. As such, it is important for secondary sources to reference those
  primary sources from which they were derived, so that their reliability can be investigated.
  A primary source relation is a particular case of derivation of secondary materials
  from their primary sources. It is recognized that the determination of primary sources
  can be up to interpretation, and should be done according to conventions accepted
  within the application's domain.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: owl_Thing
slot_uri: prov:hadPrimarySource
alias: prov_hadPrimarySource
domain_of:
- owl_Thing
range: prov_Entity
required: false
multivalued: true

```
</details>