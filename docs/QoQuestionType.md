# Enum: QoQuestionType 




_Specifies the structural classification and data-type constraints governing acceptable inputs for an inquiry item._



URI: [QoQuestionType](QoQuestionType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| choice | http://hl7.org/fhir/item-type#coding | An inquiry format offering a fixed set of standardized coded options for sele... |
| openChoice | https://ns.faqir.org/q-o#open-choice | A question with predefined options to select from plus a last valueCoding: {'... |
| numberInterval | https://ns.faqir.org/q-o#numberInterval | A question that expects a numeric answer in between a minimum and maximum val... |
| decimal | http://hl7.org/fhir/item-type#decimal | A question that expects a numerical answer, either integer or float |
| time | http://hl7.org/fhir/item-type#time | An inquiry item constraining acceptable input strictly to a clock time (hour,... |
| dateTime | http://hl7.org/fhir/item-type#dateTime | An inquiry item constraining acceptable input strictly to a date and time, fo... |
| text | http://hl7.org/fhir/item-type#string | An inquiry item that expects a free string answer |




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
description: Specifies the structural classification and data-type constraints governing
  acceptable inputs for an inquiry item.
from_schema: https://ns.faqir.org/q-o
rank: 1000
enum_uri: qo:QuestionType
permissible_values:
  choice:
    text: choice
    description: An inquiry format offering a fixed set of standardized coded options
      for selection.
    meaning: http://hl7.org/fhir/item-type#coding
    mappings:
    - fhir:QuestionnaireResponse.item.answer.valueCoding
  openChoice:
    text: openChoice
    description: 'A question with predefined options to select from plus a last valueCoding:
      {''code'': ''-1'', ''display'': ''Other''} that allows text input. Multiple
      selection may be allowed.'
    meaning: https://ns.faqir.org/q-o#open-choice
    narrow_mappings:
    - fhir:QuestionnaireResponse.item.answer.valueCoding
  numberInterval:
    text: numberInterval
    description: A question that expects a numeric answer in between a minimum and
      maximum value.
    meaning: https://ns.faqir.org/q-o#numberInterval
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
    description: An inquiry item constraining acceptable input strictly to a clock
      time (hour, minute, second) without a date component.
    meaning: http://hl7.org/fhir/item-type#time
    mappings:
    - xsd:time
  dateTime:
    text: dateTime
    description: An inquiry item constraining acceptable input strictly to a date
      and time, formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
    meaning: http://hl7.org/fhir/item-type#dateTime
    mappings:
    - xsd:dateTime
  text:
    text: text
    description: An inquiry item that expects a free string answer.
    meaning: http://hl7.org/fhir/item-type#string
    mappings:
    - xsd:string

```
</details>
