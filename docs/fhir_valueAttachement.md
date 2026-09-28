

# Slot: fhir_valueAttachement 


_This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type._





URI: [fhir:valueAttachement](http://hl7.org/fhir/valueAttachement)
Alias: fhir_valueAttachement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | The status of the questionnaire, indicating whether it is 	draft, active, ret... |  no  |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valueAttachement |
| native | qo:fhir_valueAttachement |




## LinkML Source

<details>
```yaml
name: fhir_valueAttachement
description: This type is for containing or referencing attachments - additional data
  content defined in other formats. The most common use of this type is to include
  images or reports in some report format such as PDF. However, it can be used for
  any data that has a MIME type.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valueAttachement
alias: fhir_valueAttachement
owner: saref_PropertyValue
domain_of:
- saref_PropertyValue
range: uriorcurie
required: false
multivalued: false

```
</details>