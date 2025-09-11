# datamodel

The datamodel used in faqir vaults.

URI: https://w3id.org/faqir/datamodel

Name: datamodel



## Classes

| Class | Description |
| --- | --- |
| [Answer](Answer.md) | Answer in the questionnaire response |
| [FullName](FullName.md) | Structured full name |
| [IntervalParams](IntervalParams.md) | Parameters for interval values, including minimum and maximum values |
| [Metadata](Metadata.md) | Base class for metadata tracking (e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vault](Vault.md) | The FAQIR healthdata vault |
| [NumericalParams](NumericalParams.md) | Parameters for quantitative values, including unit and precision |
| [OrderedQuestion](OrderedQuestion.md) | Question's position within a specific questionnaire or section |
| [OrderedSection](OrderedSection.md) | Section's position within a specific questionnaire or section |
| [Organization](Organization.md) | An entity acting in a healthcare context |
| [Procedure](Procedure.md) | A clinical or administrative process that uses resources like questionnaires |
| [Question](Question.md) | A question in the questionnaire |
| [Questionnaire](Questionnaire.md) | A questionnaire that can be answered (collection of questions) |
| [QuestionnaireResponse](QuestionnaireResponse.md) | A response to a questionnaire (collection of answers) |
| [ScoreDefinition](ScoreDefinition.md) | A score calculated from questions |
| [ScoreParameter](ScoreParameter.md) | Parameters for score definitions, such as min/max values, categories or const... |
| [ScoreValue](ScoreValue.md) | The score value calculated from a QuestionnaireResponse following a ScoreDefi... |
| [Section](Section.md) | A section of questions in the questionnaire |
| [ValueCoding](ValueCoding.md) | A coded value with a unique code for each display text, typically used for st... |
| [ValueDateTime](ValueDateTime.md) | A date and time value, typically in ISO 8601 format |
| [ValueNumerical](ValueNumerical.md) | Base class for quantitative values, they may have units and precision |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Weight](Weight.md) | Weight |
| [ValueString](ValueString.md) | A string value, typically used for text or identifiers |



## Slots

| Slot | Description |
| --- | --- |
| [answerId](answerId.md) | The unique identifier for an answer in the questionnaire response |
| [answerInQuestionnaireResponse](answerInQuestionnaireResponse.md) | The QuestionnaireResponse that this Answer is part of |
| [answerIsEmpty](answerIsEmpty.md) | True if the answer is intentionally empty |
| [answerTimeStamp](answerTimeStamp.md) | The exact date and time when the answer was provided |
| [answerToQuestion](answerToQuestion.md) | The Question that this Answer is for |
| [answerValueDateTime](answerValueDateTime.md) | The value of the answer to a dateTime type of question, which is a datetime v... |
| [answerValueNumerical](answerValueNumerical.md) | The value of the answer to a decimal or numberInterval type of question, whic... |
| [answerValueString](answerValueString.md) | The value of the answer to a choice, openChoice or text type of question, whi... |
| [birthdate](birthdate.md) | The date of birth |
| [code](code.md) | The code representing the value (e |
| [dateTimeValue](dateTimeValue.md) | The date and time value in ISO 8601 format |
| [display](display.md) | The human-readable display text for the code (e |
| [family_name](family_name.md) | Family or last name |
| [first_name](first_name.md) | Given or first name |
| [full_name](full_name.md) | The full name of the vault's user |
| [hasQuestionnaireResponse](hasQuestionnaireResponse.md) | QuestionnaireResponse authored by this vault's user |
| [id](id.md) | Unique identifier for all entities |
| [lastUpdated](lastUpdated.md) | The date and time when the entity was last updated |
| [maxLabel](maxLabel.md) | The label for the maximum value of the interval |
| [maxValue](maxValue.md) | The maximum value of the interval |
| [middle_name](middle_name.md) | Middle name |
| [minLabel](minLabel.md) | The label for the minimum value of the interval |
| [minValue](minValue.md) | The minimum value of the interval |
| [numericalPrecision](numericalPrecision.md) | The precision of the quantitative value, e |
| [numericalUnit](numericalUnit.md) | The unit of measure for the quantitative value, from UCUM standard |
| [numericalValue](numericalValue.md) | The quantitative value, which can be an integer or a float |
| [orderedQuestionHasQuestion](orderedQuestionHasQuestion.md) | Question indexed in this OrderedQuestion |
| [orderedQuestionId](orderedQuestionId.md) | The unique identifier for the ordered question |
| [orderedQuestionPartOfQuestionnaire](orderedQuestionPartOfQuestionnaire.md) | The Questionnaire that this Question is part of in the specified order |
| [orderedQuestionPartOfSection](orderedQuestionPartOfSection.md) | The Section that this Question is part of in the specified order |
| [orderedSectionHasSection](orderedSectionHasSection.md) | Section indexed in this OrderedSection |
| [orderedSectionId](orderedSectionId.md) | The unique identifier for the ordered Section |
| [orderedSectionPartOfQuestionnaire](orderedSectionPartOfQuestionnaire.md) | The Questionnaire that this Section is part of in the specified order |
| [orderedSectionPartOfSection](orderedSectionPartOfSection.md) | The Section that this Section is part of in the specified order |
| [organizationAuthorsQuestion](organizationAuthorsQuestion.md) | Question created by this organization |
| [organizationAuthorsQuestionnaire](organizationAuthorsQuestionnaire.md) | Questionnaire created by this organization |
| [organizationAuthorsScoreDefinition](organizationAuthorsScoreDefinition.md) | Score definition created by this organization |
| [organizationAuthorsSection](organizationAuthorsSection.md) | Section created by this organization |
| [organizationId](organizationId.md) | Unique identifier of the organization |
| [organizationLabel](organizationLabel.md) | Name of the organization |
| [organizationManagesVault](organizationManagesVault.md) | Vault managed by this organization |
| [organizationPerformsProcedure](organizationPerformsProcedure.md) | Procedure managed and performed by this organization |
| [organizationType](organizationType.md) | Type of organization |
| [procedureDescription](procedureDescription.md) | Description of the procedure |
| [procedureHasQuestionnaire](procedureHasQuestionnaire.md) | Questionnaires part of this procedure |
| [procedureId](procedureId.md) | unique identifier of the procedure |
| [procedureLabel](procedureLabel.md) | Name of the procedure |
| [procedurePerformedByOrg](procedurePerformedByOrg.md) | Organization that manages and perfomes this procedure |
| [questionAuthoredByOrg](questionAuthoredByOrg.md) | The organization that has designed this Question |
| [questionCodingParams](questionCodingParams.md) | Code and Display of each option offered as answer to the choice or open-choic... |
| [questionHasAnswer](questionHasAnswer.md) | The Answer to this Question |
| [questionId](questionId.md) | The unique identifier for a question in the questionnaire |
| [questionInOrderedQuestion](questionInOrderedQuestion.md) | OrderedQuestions that this Question is indexed in |
| [questionIntervalParams](questionIntervalParams.md) | Minimum and Maximum limiting the range the answer must be in for the question |
| [questionLabel](questionLabel.md) | The text of the question itself, which is displayed to the user |
| [questionnaireAuthoredByOrg](questionnaireAuthoredByOrg.md) | The Organization that has created this Questionnaire |
| [questionnaireHasOrderedQuestion](questionnaireHasOrderedQuestion.md) | The Question that is part of this Questionnaire, with their display order |
| [questionnaireHasOrderedSection](questionnaireHasOrderedSection.md) | The Section that is part of this Questionnaire, with their display order |
| [questionnaireHasQuestionnaireResponse](questionnaireHasQuestionnaireResponse.md) | The QuestionnaireResponse that is associated with this Questionnaire |
| [questionnaireId](questionnaireId.md) | The unique identifier for the questionnaire |
| [questionnaireLabel](questionnaireLabel.md) | The label or title of the questionnaire, which is displayed to the user |
| [questionnaireLastUpdated](questionnaireLastUpdated.md) | The date and time when the questionnaire was last updated |
| [questionnairePartOfProcedure](questionnairePartOfProcedure.md) | Procedure this questionnaire is part of |
| [questionnaireResponseBySubject](questionnaireResponseBySubject.md) | The subject that has authored this QuestionnaireResponse |
| [questionnaireResponseHasAnswer](questionnaireResponseHasAnswer.md) | The Answer that is part of this QuestionnaireResponse |
| [questionnaireResponseHasDerivedScoreValue](questionnaireResponseHasDerivedScoreValue.md) | The ScoreValue that is calculated from this QuestionnaireResponse's answers |
| [questionnaireResponseId](questionnaireResponseId.md) | The unique identifier for a specific questionnaire response |
| [questionnaireResponseLastUpdated](questionnaireResponseLastUpdated.md) | The date and time when the questionnaire response was last updated |
| [questionnaireResponseStatus](questionnaireResponseStatus.md) | The status of the questionnaire response, indicating whether it is 	'in-progr... |
| [questionnaireResponseTimeStamp](questionnaireResponseTimeStamp.md) | The date and time when the questionnaire response was created (when the quest... |
| [questionnaireResponseToQuestionnaire](questionnaireResponseToQuestionnaire.md) | The Questionnaire that this QuestionnaireResponse is for |
| [questionnaireStatus](questionnaireStatus.md) | The status of the questionnaire, indicating whether it is draft, active, reti... |
| [questionnaireVersion](questionnaireVersion.md) | Version of the questionnaire |
| [questionNumericalParams](questionNumericalParams.md) | Unit and Precision limiting the quantitative answer for the question |
| [questionOrder](questionOrder.md) | Question position in the questionnaire or section (1-based index) |
| [questionRequired](questionRequired.md) | Indicates whether answering this question is mandatory (true) or it's optiona... |
| [questionTag](questionTag.md) | Internal English identifier, e |
| [questionType](questionType.md) | Type of the question (e |
| [questionUsedInScoreDefinition](questionUsedInScoreDefinition.md) | The ScoreDefinition that this Question is used in |
| [scoreDefinitionAuthoredByOrg](scoreDefinitionAuthoredByOrg.md) | The Organization that has created this ScoreDefinition |
| [scoreDefinitionCategories](scoreDefinitionCategories.md) | Categories for categorical scores |
| [scoreDefinitionFormula](scoreDefinitionFormula.md) | The formula used to calculate the score |
| [scoreDefinitionHasScoreParameter](scoreDefinitionHasScoreParameter.md) | The ScoreParameter that is required for this ScoreDefinition |
| [scoreDefinitionHasScoreValue](scoreDefinitionHasScoreValue.md) | The ScoreValue that is calculated following this ScoreDefinition |
| [scoreDefinitionId](scoreDefinitionId.md) | Unique identifier for the score definition |
| [scoreDefinitionInterpretationGuide](scoreDefinitionInterpretationGuide.md) | How to interpret the score values |
| [scoreDefinitionIntervalParams](scoreDefinitionIntervalParams.md) | Minimum and maximum values for numerical_percentage and numerical_z_score sco... |
| [scoreDefinitionLabel](scoreDefinitionLabel.md) | Label or title of the score definition |
| [scoreDefinitionType](scoreDefinitionType.md) | Type of score: numerical_continuous, numerical_integer, numerical_percentage,... |
| [scoreDefinitionUsesQuestion](scoreDefinitionUsesQuestion.md) | The Question(s) that this ScoreDefinition is based on |
| [scoreParameterId](scoreParameterId.md) | Unique identifier for the score parameter |
| [scoreParameterLabel](scoreParameterLabel.md) | Label or title of the parameter |
| [scoreParameterPartOfScoreDefinition](scoreParameterPartOfScoreDefinition.md) | The ScoreDefinition(s) that this ScoreParameter is part of |
| [scoreParameterType](scoreParameterType.md) | Type of parameter: numerical or dateTime |
| [scoreParameterValueDateTime](scoreParameterValueDateTime.md) | DateTime value parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz |
| [scoreParameterValueNumerical](scoreParameterValueNumerical.md) | Numerical value parameter (e |
| [scoreValueBasedOnScoreDefinition](scoreValueBasedOnScoreDefinition.md) | The ScoreDefinition that this ScoreValue is based on |
| [scoreValueDerivedFromQuestionnaireResponse](scoreValueDerivedFromQuestionnaireResponse.md) | The QuestionnaireResponse that contains the answers this ScoreValue is calcul... |
| [scoreValueId](scoreValueId.md) | Unique identifier for the score value |
| [scoreValueNumerical](scoreValueNumerical.md) | Numerical value of the score, used for numerical scores |
| [scoreValueStatus](scoreValueStatus.md) | Status of the score value, e |
| [scoreValueString](scoreValueString.md) | String representation of the score value, used for categorical scores |
| [scoreValueTimeStamp](scoreValueTimeStamp.md) | Timestamp when the score value was calculated |
| [sectionAuthoredByOrg](sectionAuthoredByOrg.md) | The Organization that has created this Section |
| [sectionHasOrderedQuestion](sectionHasOrderedQuestion.md) | The Question that is part of this Section, with their display order |
| [sectionHasOrderedSection](sectionHasOrderedSection.md) | The Section that is part of this Section |
| [sectionId](sectionId.md) | The unique identifier for a section in the questionnaire |
| [sectionInOrderedSection](sectionInOrderedSection.md) | OrderedSections that this Section is indexed in |
| [sectionLabel](sectionLabel.md) | The label or title of the section, which is displayed to the user |
| [sectionOrder](sectionOrder.md) | Section position in the questionnaire or section (1-based index) |
| [stringValue](stringValue.md) | The string value, which can be any text |
| [vaultId](vaultId.md) | The unique identifier for a vault |
| [vaultManagedByOrg](vaultManagedByOrg.md) | Organization managing this vault |
| [weight](weight.md) | The weight of the vault's user |
| [weightType](weightType.md) | The type of weight measurement, e |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [MassUnit](MassUnit.md) | Allowed units from UCUM standard for mass |
| [OrganizationType](OrganizationType.md) | Type of organization: hospital, government, professional, research or service... |
| [QuestionnaireResponseStatus](QuestionnaireResponseStatus.md) | The quesionnaire response status must be one of the following: 'in-progress',... |
| [QuestionnaireStatus](QuestionnaireStatus.md) | Questionnaires must have one of the following status (FHIR inspired):  |
| [QuestionType](QuestionType.md) | The type of question asked in the questionnaire |
| [ScoreParameterType](ScoreParameterType.md) | The type of parameter used in the score definition |
| [ScoreType](ScoreType.md) | The type of score definition, which can be numerical or categorical |
| [ScoreValueStatus](ScoreValueStatus.md) | The status of a score value, indicating its validity and completeness |
| [UnitOfMeasure](UnitOfMeasure.md) | Allowed units from UCUM standard |
| [WeightType](WeightType.md) | Allowed LOINC codes for weight |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
