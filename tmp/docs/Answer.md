
# Class: Answer

Answer in the questionnaire response.

URI: [datamodel:Answer](https://w3id.org/faqir/datamodel/Answer)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueString],[ValueNumerical],[ValueDateTime],[QuestionnaireResponse],[Question],[ValueDateTime]<answerValueDateTime%200..1-++[Answer&#124;questionType:QuestionType;questionMultivaluedAnswer:boolean%20%3F;answerId:uriorcurie;answerIsEmpty:boolean%20%3F;answerTimeStamp:datetime],[ValueString]<answerValueString%200..*-++[Answer],[ValueNumerical]<answerValueNumerical%200..1-++[Answer],[Question]<answerToQuestion%201..1-%20[Answer],[QuestionnaireResponse]<answerInQuestionnaireResponse%201..1-%20[Answer],[Question]-%20questionHasAnswer%200..*>[Answer],[QuestionnaireResponse]-%20questionnaireResponseHasAnswer%201..*>[Answer])](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueString],[ValueNumerical],[ValueDateTime],[QuestionnaireResponse],[Question],[ValueDateTime]<answerValueDateTime%200..1-++[Answer&#124;questionType:QuestionType;questionMultivaluedAnswer:boolean%20%3F;answerId:uriorcurie;answerIsEmpty:boolean%20%3F;answerTimeStamp:datetime],[ValueString]<answerValueString%200..*-++[Answer],[ValueNumerical]<answerValueNumerical%200..1-++[Answer],[Question]<answerToQuestion%201..1-%20[Answer],[QuestionnaireResponse]<answerInQuestionnaireResponse%201..1-%20[Answer],[Question]-%20questionHasAnswer%200..*>[Answer],[QuestionnaireResponse]-%20questionnaireResponseHasAnswer%201..*>[Answer])

## Referenced by Class

 *  **[Question](Question.md)** *[questionHasAnswer](questionHasAnswer.md)*  <sub>0..\*</sub>  **[Answer](Answer.md)**
 *  **[QuestionnaireResponse](QuestionnaireResponse.md)** *[questionnaireResponseHasAnswer](questionnaireResponseHasAnswer.md)*  <sub>1..\*</sub>  **[Answer](Answer.md)**

## Attributes


### Own

 * [answerInQuestionnaireResponse](answerInQuestionnaireResponse.md)  <sub>1..1</sub>
     * Description: The QuestionnaireResponse that this Answer is part of.
     * Range: [QuestionnaireResponse](QuestionnaireResponse.md)
 * [answerToQuestion](answerToQuestion.md)  <sub>1..1</sub>
     * Description: The Question that this Answer is for.
     * Range: [Question](Question.md)
 * [questionType](questionType.md)  <sub>1..1</sub>
     * Description: Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
     * Range: [QuestionType](QuestionType.md)
 * [questionMultivaluedAnswer](questionMultivaluedAnswer.md)  <sub>0..1</sub>
     * Description: Indicates whether this question allows multiple answers (true) or it's single answer (false).
     * Range: [Boolean](types/Boolean.md)
 * [➞answerId](answer__answerId.md)  <sub>1..1</sub>
     * Description: The unique identifier for an answer in the questionnaire response.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞answerValueNumerical](answer__answerValueNumerical.md)  <sub>0..1</sub>
     * Description: The value of the answer to a decimal or numberInterval type of question, which is a numeric value.
     * Range: [ValueNumerical](ValueNumerical.md)
 * [➞answerValueString](answer__answerValueString.md)  <sub>0..\*</sub>
     * Description: The value of the answer to a choice, openChoice or text type of question, which is a stringValue.
     * Range: [ValueString](ValueString.md)
 * [➞answerValueDateTime](answer__answerValueDateTime.md)  <sub>0..1</sub>
     * Description: The value of the answer to a dateTime type of question, which is a datetime value.
     * Range: [ValueDateTime](ValueDateTime.md)
 * [➞answerIsEmpty](answer__answerIsEmpty.md)  <sub>0..1</sub>
     * Description: True if the answer is intentionally empty.
     * Range: [Boolean](types/Boolean.md)
 * [➞answerTimeStamp](answer__answerTimeStamp.md)  <sub>1..1</sub>
     * Description: The exact date and time when the answer was provided.
     * Range: [Datetime](types/Datetime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:Answer |
|  | | fhir:QuestionnaireResponse.item.answer |