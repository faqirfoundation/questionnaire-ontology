
# Class: QuestionRepresentation

The text representation of the question, in a specific language.

URI: [datamodel:QuestionRepresentation](https://w3id.org/faqir/datamodel/QuestionRepresentation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]<questionRepresentationOfQuestion%201..1-%20[QuestionRepresentation&#124;questionRepresentationId:uriorcurie;questionRepresentationText:string;questionRepresentationLanguage:string],[Question]++-%20questionHasQuestionRepresentation%201..*>[QuestionRepresentation],[Question])](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]<questionRepresentationOfQuestion%201..1-%20[QuestionRepresentation&#124;questionRepresentationId:uriorcurie;questionRepresentationText:string;questionRepresentationLanguage:string],[Question]++-%20questionHasQuestionRepresentation%201..*>[QuestionRepresentation],[Question])

## Referenced by Class

 *  **[Question](Question.md)** *[questionHasQuestionRepresentation](questionHasQuestionRepresentation.md)*  <sub>1..\*</sub>  **[QuestionRepresentation](QuestionRepresentation.md)**

## Attributes


### Own

 * [questionRepresentationOfQuestion](questionRepresentationOfQuestion.md)  <sub>1..1</sub>
     * Description: The Question that this QuestionRepresentation describes.
     * Range: [Question](Question.md)
 * [➞questionRepresentationId](questionRepresentation__questionRepresentationId.md)  <sub>1..1</sub>
     * Description: The unique identifier for the question representation.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞questionRepresentationText](questionRepresentation__questionRepresentationText.md)  <sub>1..1</sub>
     * Description: The text of the question as presented to the user.
     * Range: [String](types/String.md)
 * [➞questionRepresentationLanguage](questionRepresentation__questionRepresentationLanguage.md)  <sub>1..1</sub>
     * Description: The language of the question text, represented as a BCP 47 language tag (e.g., 'en', 'fr', 'es').
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:QuestionRepresentation |