# Enum: QoQuestionnaireStatusEnum 




_Questionnaires must have one of the following status (FHIR inspired): _



URI: [QoQuestionnaireStatusEnum](QoQuestionnaireStatusEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| draft | http://hl7.org/fhir/resource-status-draft | This resource is still under development and is not yet considered to be read... |
| active | http://hl7.org/fhir/resource-status-active | This resource is ready for normal use |
| retired | http://hl7.org/fhir/resource-status-retired | This resource has been withdrawn or superseded and should no longer be used |
| unknown | http://hl7.org/fhir/resource-status-unknown | The authoring system does not know which of the status values currently appli... |




## Slots

| Name | Description |
| ---  | --- |
| [saref_hasValue](saref_hasValue.md) | The status of the questionnaire, indicating whether it is	draft active, retir... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o






## LinkML Source

<details>
```yaml
name: qo_QuestionnaireStatusEnum
description: 'Questionnaires must have one of the following status (FHIR inspired): '
from_schema: https://ns.faqir.org/q-o
rank: 1000
enum_uri: qo:QuestionnaireStatusEnum
permissible_values:
  draft:
    text: draft
    description: This resource is still under development and is not yet considered
      to be ready for normal use.
    meaning: http://hl7.org/fhir/resource-status-draft
    mappings:
    - fhir:codesystem-resource-status.html#resource-status-draft
  active:
    text: active
    description: This resource is ready for normal use.
    meaning: http://hl7.org/fhir/resource-status-active
    mappings:
    - fhir:codesystem-resource-status.html#resource-status-active
  retired:
    text: retired
    description: This resource has been withdrawn or superseded and should no longer
      be used.
    meaning: http://hl7.org/fhir/resource-status-retired
    mappings:
    - fhir:codesystem-resource-status.html#resource-status-inactive
  unknown:
    text: unknown
    description: 'The authoring system does not know which of the status values currently
      applies for this resource. Note: This concept is not to be used for ''other''
      - one of the listed statuses is presumed to apply, it''s just not known which
      one.'
    meaning: http://hl7.org/fhir/resource-status-unknown
    mappings:
    - fhir:codesystem-resource-status.html#resource-status-unknown

```
</details>
