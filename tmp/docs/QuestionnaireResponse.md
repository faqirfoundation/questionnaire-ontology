
# Class: QuestionnaireResponse

A response to a questionnaire (collection of answers).

URI: [datamodel:QuestionnaireResponse](https://w3id.org/faqir/datamodel/QuestionnaireResponse)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vault],[ScoreValue],[ScoreValue]<questionnaireResponseHasDerivedScoreValue%200..*-%20[QuestionnaireResponse&#124;questionnaireResponseId:uriorcurie;questionnaireResponseStatus:QuestionnaireResponseStatus;questionnaireResponseTimeStamp:datetime;questionnaireResponseLastUpdated:datetime],[Answer]<questionnaireResponseHasAnswer%201..*-%20[QuestionnaireResponse],[Questionnaire]<questionnaireResponseToQuestionnaire%201..1-%20[QuestionnaireResponse],[Vault]<questionnaireResponseBySubject%201..1-%20[QuestionnaireResponse],[Answer]-%20answerInQuestionnaireResponse%201..1>[QuestionnaireResponse],[Vault]-%20hasQuestionnaireResponse%200..*>[QuestionnaireResponse],[Questionnaire]-%20questionnaireHasQuestionnaireResponse%200..*>[QuestionnaireResponse],[ScoreValue]-%20scoreValueDerivedFromQuestionnaireResponse%201..*>[QuestionnaireResponse],[Questionnaire],[Answer])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vault],[ScoreValue],[ScoreValue]<questionnaireResponseHasDerivedScoreValue%200..*-%20[QuestionnaireResponse&#124;questionnaireResponseId:uriorcurie;questionnaireResponseStatus:QuestionnaireResponseStatus;questionnaireResponseTimeStamp:datetime;questionnaireResponseLastUpdated:datetime],[Answer]<questionnaireResponseHasAnswer%201..*-%20[QuestionnaireResponse],[Questionnaire]<questionnaireResponseToQuestionnaire%201..1-%20[QuestionnaireResponse],[Vault]<questionnaireResponseBySubject%201..1-%20[QuestionnaireResponse],[Answer]-%20answerInQuestionnaireResponse%201..1>[QuestionnaireResponse],[Vault]-%20hasQuestionnaireResponse%200..*>[QuestionnaireResponse],[Questionnaire]-%20questionnaireHasQuestionnaireResponse%200..*>[QuestionnaireResponse],[ScoreValue]-%20scoreValueDerivedFromQuestionnaireResponse%201..*>[QuestionnaireResponse],[Questionnaire],[Answer])

## Referenced by Class

 *  **[Answer](Answer.md)** *[answerInQuestionnaireResponse](answerInQuestionnaireResponse.md)*  <sub>1..1</sub>  **[QuestionnaireResponse](QuestionnaireResponse.md)**
 *  **[Vault](Vault.md)** *[hasQuestionnaireResponse](hasQuestionnaireResponse.md)*  <sub>0..\*</sub>  **[QuestionnaireResponse](QuestionnaireResponse.md)**
 *  **[Questionnaire](Questionnaire.md)** *[questionnaireHasQuestionnaireResponse](questionnaireHasQuestionnaireResponse.md)*  <sub>0..\*</sub>  **[QuestionnaireResponse](QuestionnaireResponse.md)**
 *  **[ScoreValue](ScoreValue.md)** *[scoreValueDerivedFromQuestionnaireResponse](scoreValueDerivedFromQuestionnaireResponse.md)*  <sub>1..\*</sub>  **[QuestionnaireResponse](QuestionnaireResponse.md)**

## Attributes


### Own

 * [questionnaireResponseBySubject](questionnaireResponseBySubject.md)  <sub>1..1</sub>
     * Description: The subject that has authored this QuestionnaireResponse.
     * Range: [Vault](Vault.md)
 * [questionnaireResponseToQuestionnaire](questionnaireResponseToQuestionnaire.md)  <sub>1..1</sub>
     * Description: The Questionnaire that this QuestionnaireResponse is for.
     * Range: [Questionnaire](Questionnaire.md)
 * [questionnaireResponseHasAnswer](questionnaireResponseHasAnswer.md)  <sub>1..\*</sub>
     * Description: The Answer that is part of this QuestionnaireResponse.
     * Range: [Answer](Answer.md)
 * [questionnaireResponseHasDerivedScoreValue](questionnaireResponseHasDerivedScoreValue.md)  <sub>0..\*</sub>
     * Description: The ScoreValue that is calculated from this QuestionnaireResponse's answers.
     * Range: [ScoreValue](ScoreValue.md)
 * [➞questionnaireResponseId](questionnaireResponse__questionnaireResponseId.md)  <sub>1..1</sub>
     * Description: The unique identifier for a specific questionnaire response.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞questionnaireResponseStatus](questionnaireResponse__questionnaireResponseStatus.md)  <sub>1..1</sub>
     * Description: The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
     * Range: [QuestionnaireResponseStatus](QuestionnaireResponseStatus.md)
 * [➞questionnaireResponseTimeStamp](questionnaireResponse__questionnaireResponseTimeStamp.md)  <sub>1..1</sub>
     * Description: The date and time when the questionnaire response was created (when the questionnaire starts to be answered, not when it's finished).
     * Range: [Datetime](types/Datetime.md)
 * [➞questionnaireResponseLastUpdated](questionnaireResponse__questionnaireResponseLastUpdated.md)  <sub>1..1</sub>
     * Description: The date and time when the questionnaire response was last updated.
     * Range: [Datetime](types/Datetime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:QuestionnaireResponse |