# Enum: QoQuestionnaireResponseStatusEnum 




_The questionnaire response status must be one of the following: 'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'._



URI: [QoQuestionnaireResponseStatusEnum](QoQuestionnaireResponseStatusEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| in_progress | http://hl7.org/fhir/questionnaire-answers-status-in-progress | This QuestionnaireResponse has been partially filled out with answers but cha... |
| completed | http://hl7.org/fhir/questionnaire-answers-status-completed | This QuestionnaireResponse has been filled out with answers and the current c... |
| amended | http://hl7.org/fhir/questionnaire-answers-status-amended | This QuestionnaireResponse has been filled out with answers, then marked as c... |
| entered_in_error | http://hl7.org/fhir/questionnaire-answers-status-entered-in-error | This QuestionnaireResponse was entered in error and voided |
| stopped | http://hl7.org/fhir/questionnaire-answers-status-stopped | This QuestionnaireResponse has been partially filled out with answers but has... |




## Slots

| Name | Description |
| ---  | --- |
| [saref_hasValue](saref_hasValue.md) | The status of the questionnaire response, indicating whether it is 'in-progre... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o






## LinkML Source

<details>
```yaml
name: qo_QuestionnaireResponseStatusEnum
description: 'The questionnaire response status must be one of the following: ''in-progress'',
  ''completed'', ''amended'', ''entered-in-error'' or ''stopped''.'
from_schema: https://ns.faqir.org/q-o
rank: 1000
enum_uri: qo:QuestionnaireResponseStatusEnum
permissible_values:
  in_progress:
    text: in_progress
    description: This QuestionnaireResponse has been partially filled out with answers
      but changes or additions are still expected to be made to it.
    meaning: http://hl7.org/fhir/questionnaire-answers-status-in-progress
    mappings:
    - fhir:valueset-resource-status.html
  completed:
    text: completed
    description: This QuestionnaireResponse has been filled out with answers and the
      current content is regarded as definitive.
    meaning: http://hl7.org/fhir/questionnaire-answers-status-completed
    mappings:
    - fhir:valueset-resource-status.html
  amended:
    text: amended
    description: This QuestionnaireResponse has been filled out with answers, then
      marked as complete, yet changes or additions have been made to it afterwards.
    meaning: http://hl7.org/fhir/questionnaire-answers-status-amended
    mappings:
    - fhir:valueset-resource-status.html
  entered_in_error:
    text: entered_in_error
    description: This QuestionnaireResponse was entered in error and voided.
    meaning: http://hl7.org/fhir/questionnaire-answers-status-entered-in-error
    mappings:
    - fhir:valueset-resource-status.html
  stopped:
    text: stopped
    description: This QuestionnaireResponse has been partially filled out with answers
      but has been abandoned. No subsequent changes can be made.
    meaning: http://hl7.org/fhir/questionnaire-answers-status-stopped
    mappings:
    - fhir:valueset-resource-status.html

```
</details>
