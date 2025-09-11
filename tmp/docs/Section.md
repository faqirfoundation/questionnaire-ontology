
# Class: Section

A section of questions in the questionnaire.

URI: [datamodel:Section](https://w3id.org/faqir/datamodel/Section)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization]<sectionAuthoredByOrg%200..*-%20[Section&#124;sectionId:uriorcurie;sectionLabel:string],[ScoreDefinition]<sectionUsesScoreDefinition%200..*-%20[Section],[OrderedSection]<sectionInOrderedSection%200..*-%20[Section],[OrderedSection]<sectionHasOrderedSection%200..*-++[Section],[OrderedQuestion]<sectionHasOrderedQuestion%200..*-++[Section],[OrderedQuestion]-%20orderedQuestionPartOfSection%200..1>[Section],[OrderedSection]-%20orderedSectionHasSection%201..1>[Section],[OrderedSection]-%20orderedSectionPartOfSection%200..1>[Section],[Organization]-%20organizationAuthorsSection%200..*>[Section],[ScoreDefinition]-%20scoreDefinitionUsedBySection%200..*>[Section],[ScoreDefinition],[Organization],[OrderedSection],[OrderedQuestion])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization]<sectionAuthoredByOrg%200..*-%20[Section&#124;sectionId:uriorcurie;sectionLabel:string],[ScoreDefinition]<sectionUsesScoreDefinition%200..*-%20[Section],[OrderedSection]<sectionInOrderedSection%200..*-%20[Section],[OrderedSection]<sectionHasOrderedSection%200..*-++[Section],[OrderedQuestion]<sectionHasOrderedQuestion%200..*-++[Section],[OrderedQuestion]-%20orderedQuestionPartOfSection%200..1>[Section],[OrderedSection]-%20orderedSectionHasSection%201..1>[Section],[OrderedSection]-%20orderedSectionPartOfSection%200..1>[Section],[Organization]-%20organizationAuthorsSection%200..*>[Section],[ScoreDefinition]-%20scoreDefinitionUsedBySection%200..*>[Section],[ScoreDefinition],[Organization],[OrderedSection],[OrderedQuestion])

## Referenced by Class

 *  **[OrderedQuestion](OrderedQuestion.md)** *[orderedQuestionPartOfSection](orderedQuestionPartOfSection.md)*  <sub>0..1</sub>  **[Section](Section.md)**
 *  **[OrderedSection](OrderedSection.md)** *[orderedSectionHasSection](orderedSectionHasSection.md)*  <sub>1..1</sub>  **[Section](Section.md)**
 *  **[OrderedSection](OrderedSection.md)** *[orderedSectionPartOfSection](orderedSectionPartOfSection.md)*  <sub>0..1</sub>  **[Section](Section.md)**
 *  **[Organization](Organization.md)** *[organizationAuthorsSection](organizationAuthorsSection.md)*  <sub>0..\*</sub>  **[Section](Section.md)**
 *  **[ScoreDefinition](ScoreDefinition.md)** *[scoreDefinitionUsedBySection](scoreDefinitionUsedBySection.md)*  <sub>0..\*</sub>  **[Section](Section.md)**

## Attributes


### Own

 * [sectionHasOrderedQuestion](sectionHasOrderedQuestion.md)  <sub>0..\*</sub>
     * Description: The Question that is part of this Section, with their display order.
     * Range: [OrderedQuestion](OrderedQuestion.md)
 * [sectionHasOrderedSection](sectionHasOrderedSection.md)  <sub>0..\*</sub>
     * Description: The Section that is part of this Section.
     * Range: [OrderedSection](OrderedSection.md)
 * [sectionInOrderedSection](sectionInOrderedSection.md)  <sub>0..\*</sub>
     * Description: OrderedSections that this Section is indexed in.
     * Range: [OrderedSection](OrderedSection.md)
 * [sectionUsesScoreDefinition](sectionUsesScoreDefinition.md)  <sub>0..\*</sub>
     * Description: The ScoreDefinition that is applied in this Section.
     * Range: [ScoreDefinition](ScoreDefinition.md)
 * [sectionAuthoredByOrg](sectionAuthoredByOrg.md)  <sub>0..\*</sub>
     * Description: The Organization that has created this Section.
     * Range: [Organization](Organization.md)
 * [➞sectionId](section__sectionId.md)  <sub>1..1</sub>
     * Description: The unique identifier for a section in the questionnaire.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞sectionLabel](section__sectionLabel.md)  <sub>1..1</sub>
     * Description: The label or title of the section, which is displayed to the user.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:Section |
|  | | fhir:Questionnaire.item.where(type='group') |