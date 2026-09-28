
# Enum: qo_QuestionType

The type of question asked in the questionnaire. It defines the expected answer format.

URI: [qo:qo_QuestionType](https://ns.faqir.org/q-o#qo_QuestionType)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| choice | A question with predefined options to choose from. Multiple choices may be allowed. | http://hl7.org/fhir/item-type#coding | {'mappings': ['fhir:QuestionnaireResponse.item.answer.valueCoding']} |
| openChoice | A question with predefined options to choose from plus a last valueCoding: {'code': '-1', 'display': 'Other'} that allows text input. Multiple choices may be allowed. | qo:open-choice | {'narrow_mappings': ['fhir:QuestionnaireResponse.item.answer.valueCoding']} |
| numberInterval | A question that expects a numeric answer in between a minimum and maximum value. | qo:numberInterval | {'narrow_mappings': ['fhir:QuestionnaireResponse.item.answer.valueInteger', 'xsd:decimal', 'xsd:integer', 'xsd:float']} |
| decimal | A question that expects a numerical answer, either integer or float. | http://hl7.org/fhir/item-type#decimal | {'narrow_mappings': ['xsd:decimal', 'xsd:integer', 'xsd:float']} |
| time | Question with a time (hour:minute:second) answer independent of date. (valueTime). | http://hl7.org/fhir/item-type#time | {'mappings': ['xsd:time']} |
| dateTime | A question that expects a dateTime answer, formatted as YYYY-MM-DDThh:mm:ss+zz:zz. | http://hl7.org/fhir/item-type#dateTime | {'mappings': ['xsd:dateTime']} |
| text | A question that expects a free text answer. | http://hl7.org/fhir/item-type#string | {'mappings': ['xsd:string', 'xsd2:text']} |

