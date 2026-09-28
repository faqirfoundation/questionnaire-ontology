# Enum: QoQuestionType 




_The type of question asked in the questionnaire. It defines the expected answer format._



URI: [QoQuestionType](QoQuestionType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| choice | http://hl7.org/fhir/item-type#coding | A question with predefined options to choose from |
| openChoice | qo:open-choice | A question with predefined options to choose from plus a last valueCoding: {'... |
| numberInterval | qo:numberInterval | A question that expects a numeric answer in between a minimum and maximum val... |
| decimal | http://hl7.org/fhir/item-type#decimal | A question that expects a numerical answer, either integer or float |
| time | http://hl7.org/fhir/item-type#time | Question with a time (hour:minute:second) answer independent of date |
| dateTime | http://hl7.org/fhir/item-type#dateTime | A question that expects a dateTime answer, formatted as YYYY-MM-DDThh:mm:ss+z... |
| text | http://hl7.org/fhir/item-type#string | A question that expects a free text answer |




## Slots

| Name | Description |
| ---  | --- |
| [prov_type](prov_type.md) | Type of the question (e |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o






## LinkML Source

<details>
```yaml
name: qo_QuestionType
description: The type of question asked in the questionnaire. It defines the expected
  answer format.
from_schema: https://ns.faqir.org/q-o
rank: 1000
enum_uri: qo:QuestionType
permissible_values:
  choice:
    text: choice
    description: A question with predefined options to choose from. Multiple choices
      may be allowed.
    meaning: http://hl7.org/fhir/item-type#coding
    mappings:
    - fhir:QuestionnaireResponse.item.answer.valueCoding
  openChoice:
    text: openChoice
    description: 'A question with predefined options to choose from plus a last valueCoding:
      {''code'': ''-1'', ''display'': ''Other''} that allows text input. Multiple
      choices may be allowed.'
    meaning: qo:open-choice
    narrow_mappings:
    - fhir:QuestionnaireResponse.item.answer.valueCoding
  numberInterval:
    text: numberInterval
    description: A question that expects a numeric answer in between a minimum and
      maximum value.
    meaning: qo:numberInterval
    narrow_mappings:
    - fhir:QuestionnaireResponse.item.answer.valueInteger
    - xsd:decimal
    - xsd:integer
    - xsd:float
  decimal:
    text: decimal
    description: A question that expects a numerical answer, either integer or float.
    meaning: http://hl7.org/fhir/item-type#decimal
    narrow_mappings:
    - xsd:decimal
    - xsd:integer
    - xsd:float
  time:
    text: time
    description: Question with a time (hour:minute:second) answer independent of date.
      (valueTime).
    meaning: http://hl7.org/fhir/item-type#time
    mappings:
    - xsd:time
  dateTime:
    text: dateTime
    description: A question that expects a dateTime answer, formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
    meaning: http://hl7.org/fhir/item-type#dateTime
    mappings:
    - xsd:dateTime
  text:
    text: text
    description: A question that expects a free text answer.
    meaning: http://hl7.org/fhir/item-type#string
    mappings:
    - xsd:string
    - xsd2:text

```
</details>
