
# Class: Question

A question in the questionnaire.

URI: [datamodel:Question](https://w3id.org/faqir/datamodel/Question)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueCoding],[ScoreDefinition],[QuestionRepresentation],[IntervalParams]<questionIntervalParams%200..1-++[Question&#124;questionType:QuestionType;questionId:uriorcurie;questionTag:string;questionRequired:boolean%20%3F],[ValueCoding]<questionCodingParams%200..*-++[Question],[NumericalParams]<questionNumericalParams%200..1-++[Question],[ScoreDefinition]<questionUsedInScoreDefinition%200..*-%20[Question],[Answer]<questionHasAnswer%200..*-%20[Question],[OrderedQuestion]<questionInOrderedQuestion%200..*-%20[Question],[Organization]<questionAuthoredByOrg%200..*-%20[Question],[QuestionRepresentation]<questionHasQuestionRepresentation%201..*-++[Question],[Answer]-%20answerToQuestion%201..1>[Question],[OrderedQuestion]-%20orderedQuestionHasQuestion%201..1>[Question],[Organization]-%20organizationAuthorsQuestion%200..*>[Question],[QuestionRepresentation]-%20questionRepresentationOfQuestion%201..1>[Question],[ScoreDefinition]-%20scoreDefinitionUsesQuestion%201..*>[Question],[Organization],[OrderedQuestion],[NumericalParams],[IntervalParams],[Answer])](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueCoding],[ScoreDefinition],[QuestionRepresentation],[IntervalParams]<questionIntervalParams%200..1-++[Question&#124;questionType:QuestionType;questionId:uriorcurie;questionTag:string;questionRequired:boolean%20%3F],[ValueCoding]<questionCodingParams%200..*-++[Question],[NumericalParams]<questionNumericalParams%200..1-++[Question],[ScoreDefinition]<questionUsedInScoreDefinition%200..*-%20[Question],[Answer]<questionHasAnswer%200..*-%20[Question],[OrderedQuestion]<questionInOrderedQuestion%200..*-%20[Question],[Organization]<questionAuthoredByOrg%200..*-%20[Question],[QuestionRepresentation]<questionHasQuestionRepresentation%201..*-++[Question],[Answer]-%20answerToQuestion%201..1>[Question],[OrderedQuestion]-%20orderedQuestionHasQuestion%201..1>[Question],[Organization]-%20organizationAuthorsQuestion%200..*>[Question],[QuestionRepresentation]-%20questionRepresentationOfQuestion%201..1>[Question],[ScoreDefinition]-%20scoreDefinitionUsesQuestion%201..*>[Question],[Organization],[OrderedQuestion],[NumericalParams],[IntervalParams],[Answer])

## Referenced by Class

 *  **[Answer](Answer.md)** *[answerToQuestion](answerToQuestion.md)*  <sub>1..1</sub>  **[Question](Question.md)**
 *  **[OrderedQuestion](OrderedQuestion.md)** *[orderedQuestionHasQuestion](orderedQuestionHasQuestion.md)*  <sub>1..1</sub>  **[Question](Question.md)**
 *  **[Organization](Organization.md)** *[organizationAuthorsQuestion](organizationAuthorsQuestion.md)*  <sub>0..\*</sub>  **[Question](Question.md)**
 *  **[QuestionRepresentation](QuestionRepresentation.md)** *[questionRepresentationOfQuestion](questionRepresentationOfQuestion.md)*  <sub>1..1</sub>  **[Question](Question.md)**
 *  **[ScoreDefinition](ScoreDefinition.md)** *[scoreDefinitionUsesQuestion](scoreDefinitionUsesQuestion.md)*  <sub>1..\*</sub>  **[Question](Question.md)**

## Attributes


### Own

 * [questionType](questionType.md)  <sub>1..1</sub>
     * Description: Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
     * Range: [QuestionType](QuestionType.md)
 * [questionHasQuestionRepresentation](questionHasQuestionRepresentation.md)  <sub>1..\*</sub>
     * Description: QuestionRepresentations that describe the question in each language.
     * Range: [QuestionRepresentation](QuestionRepresentation.md)
 * [questionAuthoredByOrg](questionAuthoredByOrg.md)  <sub>0..\*</sub>
     * Description: The organization that has designed this Question.
     * Range: [Organization](Organization.md)
 * [questionInOrderedQuestion](questionInOrderedQuestion.md)  <sub>0..\*</sub>
     * Description: OrderedQuestions that this Question is indexed in.
     * Range: [OrderedQuestion](OrderedQuestion.md)
 * [questionHasAnswer](questionHasAnswer.md)  <sub>0..\*</sub>
     * Description: The Answer to this Question.
     * Range: [Answer](Answer.md)
 * [questionUsedInScoreDefinition](questionUsedInScoreDefinition.md)  <sub>0..\*</sub>
     * Description: The ScoreDefinition that this Question is used in.
     * Range: [ScoreDefinition](ScoreDefinition.md)
 * [➞questionId](question__questionId.md)  <sub>1..1</sub>
     * Description: The unique identifier for a question in the questionnaire.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞questionTag](question__questionTag.md)  <sub>1..1</sub>
     * Description: Internal English identifier, e.g., 'q_pain_level'.
     * Range: [String](types/String.md)
 * [➞questionNumericalParams](question__questionNumericalParams.md)  <sub>0..1</sub>
     * Description: Unit and Precision limiting the quantitative answer for the question.
     * Range: [NumericalParams](NumericalParams.md)
 * [➞questionCodingParams](question__questionCodingParams.md)  <sub>0..\*</sub>
     * Description: Code and Display of each option offered as answer to the choice or open-choice question.
     * Range: [ValueCoding](ValueCoding.md)
 * [➞questionIntervalParams](question__questionIntervalParams.md)  <sub>0..1</sub>
     * Description: Minimum and Maximum limiting the range the answer must be in for the question.
     * Range: [IntervalParams](IntervalParams.md)
 * [➞questionRequired](question__questionRequired.md)  <sub>0..1</sub>
     * Description: Indicates whether answering this question is mandatory (true) or it's optional (false).
     * Range: [Boolean](types/Boolean.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:Question |
|  | | fhir:Questionnaire.item.where(type='question') |
|  | | skos:Concept |