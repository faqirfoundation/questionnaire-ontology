

# Slot: prov_wasAttributedTo 


_Attribution is the ascribing of an entity to an agent._





URI: [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo)
Alias: prov_wasAttributedTo

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |
| [QoQuestion](QoQuestion.md) | A question |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A questionnaire that can be answered (collection of questions) |  no  |
| [QoAnswer](QoAnswer.md) | Answer in the questionnaire response |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  yes  |
| [QoOrderedSection](QoOrderedSection.md) | Section's position within a specific questionnaire or section |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | The status of the questionnaire, indicating whether it is 	draft, active, ret... |  no  |







## Properties

* Range: [FoafAgent](FoafAgent.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasAttributedTo |
| native | qo:prov_wasAttributedTo |




## LinkML Source

<details>
```yaml
name: prov_wasAttributedTo
description: Attribution is the ascribing of an entity to an agent.
from_schema: https://ns.faqir.org/q-o
rank: 1000
domain: prov_Entity
slot_uri: prov:wasAttributedTo
alias: prov_wasAttributedTo
domain_of:
- prov_Entity
range: foaf_Agent
required: false
multivalued: true

```
</details>