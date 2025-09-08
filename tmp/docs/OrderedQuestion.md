
# Class: OrderedQuestion

Question's position within a specific questionnaire or section.

URI: [datamodel:OrderedQuestion](https://w3id.org/faqir/datamodel/OrderedQuestion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Section],[Questionnaire],[Question],[Section]<orderedQuestionPartOfSection%200..1-%20[OrderedQuestion&#124;orderedQuestionId:uriorcurie;questionOrder:integer],[Questionnaire]<orderedQuestionPartOfQuestionnaire%200..1-%20[OrderedQuestion],[Question]<orderedQuestionHasQuestion%201..1-%20[OrderedQuestion],[Question]-%20questionInOrderedQuestion%200..*>[OrderedQuestion],[Questionnaire]++-%20questionnaireHasOrderedQuestion%200..*>[OrderedQuestion],[Section]++-%20sectionHasOrderedQuestion%200..*>[OrderedQuestion])](https://yuml.me/diagram/nofunky;dir:TB/class/[Section],[Questionnaire],[Question],[Section]<orderedQuestionPartOfSection%200..1-%20[OrderedQuestion&#124;orderedQuestionId:uriorcurie;questionOrder:integer],[Questionnaire]<orderedQuestionPartOfQuestionnaire%200..1-%20[OrderedQuestion],[Question]<orderedQuestionHasQuestion%201..1-%20[OrderedQuestion],[Question]-%20questionInOrderedQuestion%200..*>[OrderedQuestion],[Questionnaire]++-%20questionnaireHasOrderedQuestion%200..*>[OrderedQuestion],[Section]++-%20sectionHasOrderedQuestion%200..*>[OrderedQuestion])

## Referenced by Class

 *  **[Question](Question.md)** *[questionInOrderedQuestion](questionInOrderedQuestion.md)*  <sub>0..\*</sub>  **[OrderedQuestion](OrderedQuestion.md)**
 *  **[Questionnaire](Questionnaire.md)** *[questionnaireHasOrderedQuestion](questionnaireHasOrderedQuestion.md)*  <sub>0..\*</sub>  **[OrderedQuestion](OrderedQuestion.md)**
 *  **[Section](Section.md)** *[sectionHasOrderedQuestion](sectionHasOrderedQuestion.md)*  <sub>0..\*</sub>  **[OrderedQuestion](OrderedQuestion.md)**

## Attributes


### Own

 * [orderedQuestionHasQuestion](orderedQuestionHasQuestion.md)  <sub>1..1</sub>
     * Description: Question indexed in this OrderedQuestion.
     * Range: [Question](Question.md)
 * [orderedQuestionPartOfQuestionnaire](orderedQuestionPartOfQuestionnaire.md)  <sub>0..1</sub>
     * Description: The Questionnaire that this Question is part of in the specified order.
     * Range: [Questionnaire](Questionnaire.md)
 * [orderedQuestionPartOfSection](orderedQuestionPartOfSection.md)  <sub>0..1</sub>
     * Description: The Section that this Question is part of in the specified order.
     * Range: [Section](Section.md)
 * [➞orderedQuestionId](orderedQuestion__orderedQuestionId.md)  <sub>1..1</sub>
     * Description: The unique identifier for the ordered question.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞questionOrder](orderedQuestion__questionOrder.md)  <sub>1..1</sub>
     * Description: Question position in the questionnaire or section (1-based index).
     * Range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:OrderedQuestion |