

# Slot: fhir_valueAttachment 


_This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type._





URI: [fhir:valueAttachment](http://hl7.org/fhir/valueAttachment)
Alias: fhir_valueAttachment

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |
| [SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |  no  |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fhir:valueAttachment |
| native | qo:fhir_valueAttachment |




## LinkML Source

<details>
```yaml
name: fhir_valueAttachment
description: This type is for containing or referencing attachments - additional data
  content defined in other formats. The most common use of this type is to include
  images or reports in some report format such as PDF. However, it can be used for
  any data that has a MIME type.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: fhir:valueAttachment
alias: fhir_valueAttachment
owner: saref_PropertyValue
domain_of:
- saref_PropertyValue
range: uriorcurie
required: false
multivalued: false

```
</details>