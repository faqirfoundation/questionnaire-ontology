
# Class: OrderedSection

Section's position within a specific questionnaire or section.

URI: [datamodel:OrderedSection](https://w3id.org/faqir/datamodel/OrderedSection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Section],[Questionnaire],[Section]<orderedSectionPartOfSection%200..1-%20[OrderedSection&#124;orderedSectionId:uriorcurie;sectionOrder:integer],[Questionnaire]<orderedSectionPartOfQuestionnaire%200..1-%20[OrderedSection],[Section]<orderedSectionHasSection%201..1-%20[OrderedSection],[Questionnaire]++-%20questionnaireHasOrderedSection%200..*>[OrderedSection],[Section]++-%20sectionHasOrderedSection%200..*>[OrderedSection],[Section]-%20sectionInOrderedSection%200..*>[OrderedSection])](https://yuml.me/diagram/nofunky;dir:TB/class/[Section],[Questionnaire],[Section]<orderedSectionPartOfSection%200..1-%20[OrderedSection&#124;orderedSectionId:uriorcurie;sectionOrder:integer],[Questionnaire]<orderedSectionPartOfQuestionnaire%200..1-%20[OrderedSection],[Section]<orderedSectionHasSection%201..1-%20[OrderedSection],[Questionnaire]++-%20questionnaireHasOrderedSection%200..*>[OrderedSection],[Section]++-%20sectionHasOrderedSection%200..*>[OrderedSection],[Section]-%20sectionInOrderedSection%200..*>[OrderedSection])

## Referenced by Class

 *  **[Questionnaire](Questionnaire.md)** *[questionnaireHasOrderedSection](questionnaireHasOrderedSection.md)*  <sub>0..\*</sub>  **[OrderedSection](OrderedSection.md)**
 *  **[Section](Section.md)** *[sectionHasOrderedSection](sectionHasOrderedSection.md)*  <sub>0..\*</sub>  **[OrderedSection](OrderedSection.md)**
 *  **[Section](Section.md)** *[sectionInOrderedSection](sectionInOrderedSection.md)*  <sub>0..\*</sub>  **[OrderedSection](OrderedSection.md)**

## Attributes


### Own

 * [orderedSectionHasSection](orderedSectionHasSection.md)  <sub>1..1</sub>
     * Description: Section indexed in this OrderedSection.
     * Range: [Section](Section.md)
 * [orderedSectionPartOfQuestionnaire](orderedSectionPartOfQuestionnaire.md)  <sub>0..1</sub>
     * Description: The Questionnaire that this Section is part of in the specified order.
     * Range: [Questionnaire](Questionnaire.md)
 * [orderedSectionPartOfSection](orderedSectionPartOfSection.md)  <sub>0..1</sub>
     * Description: The Section that this Section is part of in the specified order.
     * Range: [Section](Section.md)
 * [➞orderedSectionId](orderedSection__orderedSectionId.md)  <sub>1..1</sub>
     * Description: The unique identifier for the ordered Section.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞sectionOrder](orderedSection__sectionOrder.md)  <sub>1..1</sub>
     * Description: Section position in the questionnaire or section (1-based index).
     * Range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:OrderedSection |