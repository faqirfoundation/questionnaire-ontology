
# Enum: qo_QuestionnaireResponseStatusEnum

The quesionnaire response status must be one of the following: 'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.

URI: [qo:qo_QuestionnaireResponseStatusEnum](https://ns.faqir.org/q-o#qo_QuestionnaireResponseStatusEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| in_progress | This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it. | fhir:questionnaire-answers-status-in-progress | {'mappings': ['fhir:valueset-resource-status.html']} |
| completed | This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive. | fhir:questionnaire-answers-status-completed | {'mappings': ['fhir:valueset-resource-status.html']} |
| amended | This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards. | fhir:questionnaire-answers-status-amended | {'mappings': ['fhir:valueset-resource-status.html']} |
| entered_in_error | This QuestionnaireResponse was entered in error and voided. | fhir:questionnaire-answers-status-entered-in-error | {'mappings': ['fhir:valueset-resource-status.html']} |
| stopped | This QuestionnaireResponse has been partially filled out with answers but has been abandoned. No subsequent changes can be made. | fhir:questionnaire-answers-status-stopped | {'mappings': ['fhir:valueset-resource-status.html']} |

