# Enum: QuestionType 




_The type of question asked in the questionnaire. It defines the expected answer format._



URI: [QuestionType](QuestionType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| choice | fhir:choice | A question with predefined options to choose from |
| openChoice | fhir:open-choice | A question with predefined options to choose from plus a last {valueCoding: {... |
| numberInterval | fhir:number | A question that expects a numeric answer in between a minimum and maximum val... |
| decimal | fhir:decimal | A question that expects a numerical answer, either integer or float |
| dateTime | fhir:dateTime | A question that expects a dateTime answer, formatted as YYYY-MM-DDThh:mm:ss+z... |
| text | fhir:string | A question that expects a free text answer |




## Slots

| Name | Description |
| ---  | --- |
| [questionType](questionType.md) | Type of the question (e |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel






## LinkML Source

<details>
```yaml
name: QuestionType
description: The type of question asked in the questionnaire. It defines the expected
  answer format.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
enum_uri: faqir:QuestionType
permissible_values:
  choice:
    text: choice
    description: A question with predefined options to choose from. Multiple choices
      may be allowed.
    meaning: fhir:choice
    mappings:
    - fhir:QuestionnaireResponse.item.answer.valueCoding
  openChoice:
    text: openChoice
    description: 'A question with predefined options to choose from plus a last {valueCoding:
      {''code'': ''-1'', ''display'': ''Other''}} that allows text input. Multiple
      choices may be allowed.'
    meaning: fhir:open-choice
    mappings:
    - fhir:QuestionnaireResponse.item.answer.valueCoding
  numberInterval:
    text: numberInterval
    description: A question that expects a numeric answer in between a minimum and
      maximum value.
    meaning: fhir:number
    mappings:
    - fhir:QuestionnaireResponse.item.answer.valueInteger
    - xsd:decimal
    - xsd:integer
    - xsd:float
  decimal:
    text: decimal
    description: A question that expects a numerical answer, either integer or float.
    meaning: fhir:decimal
    mappings:
    - xsd:decimal
    - xsd:integer
    - xsd:float
  dateTime:
    text: dateTime
    description: A question that expects a dateTime answer, formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
    meaning: fhir:dateTime
    mappings:
    - xsd:dateTime
  text:
    text: text
    description: A question that expects a free text answer.
    meaning: fhir:string
    mappings:
    - xsd:string
    - xsd2:text

```
</details>
