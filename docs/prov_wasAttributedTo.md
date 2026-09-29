

# Slot: prov_wasAttributedTo 


_Attribution is the ascribing of an entity to an agent._





URI: [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo)
Alias: prov_wasAttributedTo

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  yes  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |







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