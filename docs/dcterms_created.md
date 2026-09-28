

# Slot: dcterms_created 


_The date and time when the entity was created._





URI: [dcterms:created](http://purl.org/dc/terms/created)
Alias: dcterms_created

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoOrderedSection](QoOrderedSection.md) | Section's position within a specific questionnaire or section |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |  no  |
| [QoAnswer](QoAnswer.md) | Answer in the questionnaire response |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaire](QoQuestionnaire.md) | A questionnaire that can be answered (collection of questions) |  yes  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | The status of the questionnaire, indicating whether it is 	draft, active, ret... |  no  |
| [SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |  no  |
| [ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |  no  |
| [QoQuestion](QoQuestion.md) | A question |  no  |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |  yes  |
| [QoSection](QoSection.md) | A section of questions in the questionnaire |  no  |
| [QoOrderedQuestion](QoOrderedQuestion.md) | Question's position within a specific questionnaire or section |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:created |
| native | qo:dcterms_created |




## LinkML Source

<details>
```yaml
name: dcterms_created
description: The date and time when the entity was created.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: dcterms:created
alias: dcterms_created
domain_of:
- prov_Entity
range: datetime
required: false

```
</details>