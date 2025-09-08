
# Enum: QuestionnaireStatus

Questionnaires must have one of the following status (FHIR inspired):

URI: [datamodel:QuestionnaireStatus](https://w3id.org/faqir/datamodel/QuestionnaireStatus)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| draft | This resource is still under development and is not yet considered to be ready for normal use. | fhir:resource-status-draft | {'mappings': ['fhir:codesystem-resource-status.html#resource-status-draft']} |
| active | This resource is ready for normal use. | fhir:resource-status-active | {'mappings': ['fhir:codesystem-resource-status.html#resource-status-active']} |
| retired | This resource has been withdrawn or superseded and should no longer be used. | fhir:resource-status-retired | {'mappings': ['fhir:codesystem-resource-status.html#resource-status-inactive']} |
| unknown | The authoring system does not know which of the status values currently applies for this resource. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, it's just not known which one. | fhir:resource-status-unknown | {'mappings': ['fhir:codesystem-resource-status.html#resource-status-unknown']} |

