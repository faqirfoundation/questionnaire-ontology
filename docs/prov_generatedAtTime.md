

# Slot: prov_generatedAtTime 


_The time at which an entity was completely created and is available for use._





URI: [prov:generatedAtTime](http://www.w3.org/ns/prov#generatedAtTime)
Alias: prov_generatedAtTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |  no  |
| [FoafAgent](FoafAgent.md) | An agent (eg |  no  |
| [QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |  no  |
| [QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  yes  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |  no  |
| [ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |  no  |
| [FoafPerson](FoafPerson.md) | A person |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:generatedAtTime |
| native | qo:prov_generatedAtTime |




## LinkML Source

<details>
```yaml
name: prov_generatedAtTime
description: The time at which an entity was completely created and is available for
  use.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: prov:generatedAtTime
alias: prov_generatedAtTime
domain_of:
- foaf_Agent
- prov_Entity
range: datetime
required: false
multivalued: true

```
</details>