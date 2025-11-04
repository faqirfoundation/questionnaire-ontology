
# datamodel


**metamodel version:** 1.7.0

**version:** None


The datamodel used in faqir vaults.


### Classes

 * [Answer](Answer.md) - Answer in the questionnaire response.
 * [FullName](FullName.md) - Structured full name.
 * [IntervalParams](IntervalParams.md) - Parameters for interval values, including minimum and maximum values.
 * [Metadata](Metadata.md) - Base class for metadata tracking (e.g. schema versioning & last updated).
     * [Vault](Vault.md) - The FAQIR healthdata vault.
 * [NumericalParams](NumericalParams.md) - Parameters for quantitative values, including unit and precision.
 * [OrderedQuestion](OrderedQuestion.md) - Question's position within a specific questionnaire or section.
 * [OrderedSection](OrderedSection.md) - Section's position within a specific questionnaire or section.
 * [Organization](Organization.md) - An entity acting in a healthcare context
 * [Procedure](Procedure.md) - A clinical or administrative process that uses resources like questionnaires
 * [Question](Question.md) - A question in the questionnaire.
 * [Questionnaire](Questionnaire.md) - A questionnaire that can be answered (collection of questions).
 * [QuestionnaireResponse](QuestionnaireResponse.md) - A response to a questionnaire (collection of answers).
 * [ScoreDefinition](ScoreDefinition.md) - A score calculated from questions.
 * [ScoreParameter](ScoreParameter.md) - Parameters for score definitions, such as min/max values, categories or constants needed.
 * [ScoreValue](ScoreValue.md) - The score value calculated from a QuestionnaireResponse following a ScoreDefinition.
 * [Section](Section.md) - A section of questions in the questionnaire.
 * [ValueCoding](ValueCoding.md) - A coded value with a unique code for each display text, typically used for standardized questionnaires.
 * [ValueDateTime](ValueDateTime.md) - A date and time value, typically in ISO 8601 format.
 * [ValueNumerical](ValueNumerical.md) - Base class for quantitative values, they may have units and precision.
     * [Weight](Weight.md) - Weight.
 * [ValueString](ValueString.md) - A string value, typically used for text or identifiers.

### Mixins


### Slots

 * [answerInQuestionnaireResponse](answerInQuestionnaireResponse.md) - The QuestionnaireResponse that this Answer is part of.
 * [answerToQuestion](answerToQuestion.md) - The Question that this Answer is for.
 * [➞answerId](answer__answerId.md) - The unique identifier for an answer in the questionnaire response.
 * [➞answerIsEmpty](answer__answerIsEmpty.md) - True if the answer is intentionally empty.
 * [➞answerTimeStamp](answer__answerTimeStamp.md) - The exact date and time when the answer was provided.
 * [➞answerValueDateTime](answer__answerValueDateTime.md) - The value of the answer to a dateTime type of question, which is a datetime value.
 * [➞answerValueNumerical](answer__answerValueNumerical.md) - The value of the answer to a decimal or numberInterval type of question, which is a numeric value.
 * [➞answerValueString](answer__answerValueString.md) - The value of the answer to a choice, openChoice or text type of question, which is a stringValue.
 * [➞family_name](fullName__family_name.md) - Family or last name.
 * [➞first_name](fullName__first_name.md) - Given or first name.
 * [➞middle_name](fullName__middle_name.md) - Middle name.
 * [hasQuestionnaireResponse](hasQuestionnaireResponse.md) - QuestionnaireResponse authored by this vault's user.
 * [id](id.md) - Unique identifier for all entities.
 * [➞maxLabel](intervalParams__maxLabel.md) - The label for the maximum value of the interval.
 * [➞maxValue](intervalParams__maxValue.md) - The maximum value of the interval.
 * [➞minLabel](intervalParams__minLabel.md) - The label for the minimum value of the interval.
 * [➞minValue](intervalParams__minValue.md) - The minimum value of the interval.
 * [➞lastUpdated](metadata__lastUpdated.md) - The date and time when the entity was last updated.
 * [➞numericalPrecision](numericalParams__numericalPrecision.md) - The precision of the quantitative value, e.g. number of decimal places.
 * [➞numericalUnit](numericalParams__numericalUnit.md) - The unit of measure for the quantitative value, from UCUM standard.
 * [orderedQuestionHasQuestion](orderedQuestionHasQuestion.md) - Question indexed in this OrderedQuestion.
 * [orderedQuestionPartOfQuestionnaire](orderedQuestionPartOfQuestionnaire.md) - The Questionnaire that this Question is part of in the specified order.
 * [orderedQuestionPartOfSection](orderedQuestionPartOfSection.md) - The Section that this Question is part of in the specified order.
 * [➞orderedQuestionId](orderedQuestion__orderedQuestionId.md) - The unique identifier for the ordered question.
 * [➞questionOrder](orderedQuestion__questionOrder.md) - Question position in the questionnaire or section (1-based index).
 * [orderedSectionHasSection](orderedSectionHasSection.md) - Section indexed in this OrderedSection.
 * [orderedSectionPartOfQuestionnaire](orderedSectionPartOfQuestionnaire.md) - The Questionnaire that this Section is part of in the specified order.
 * [orderedSectionPartOfSection](orderedSectionPartOfSection.md) - The Section that this Section is part of in the specified order.
 * [➞orderedSectionId](orderedSection__orderedSectionId.md) - The unique identifier for the ordered Section.
 * [➞sectionOrder](orderedSection__sectionOrder.md) - Section position in the questionnaire or section (1-based index).
 * [organizationAuthorsQuestion](organizationAuthorsQuestion.md) - Question created by this organization.
 * [organizationAuthorsQuestionnaire](organizationAuthorsQuestionnaire.md) - Questionnaire created by this organization.
 * [organizationAuthorsScoreDefinition](organizationAuthorsScoreDefinition.md) - Score definition created by this organization.
 * [organizationAuthorsSection](organizationAuthorsSection.md) - Section created by this organization.
 * [organizationManagesVault](organizationManagesVault.md) - Vault managed by this organization.
 * [organizationPerformsProcedure](organizationPerformsProcedure.md) - Procedure managed and performed by this organization.
 * [➞organizationId](organization__organizationId.md) - Unique identifier of the organization.
 * [➞organizationLabel](organization__organizationLabel.md) - Name of the organization.
 * [➞organizationType](organization__organizationType.md) - Type of organization.
 * [procedureHasQuestionnaire](procedureHasQuestionnaire.md) - Questionnaires part of this procedure.
 * [procedurePerformedByOrg](procedurePerformedByOrg.md) - Organization that manages and perfomes this procedure.
 * [➞procedureDescription](procedure__procedureDescription.md) - Description of the procedure
 * [➞procedureId](procedure__procedureId.md) - unique identifier of the procedure.
 * [➞procedureLabel](procedure__procedureLabel.md) - Name of the procedure.
 * [questionAuthoredByOrg](questionAuthoredByOrg.md) - The organization that has designed this Question.
 * [questionHasAnswer](questionHasAnswer.md) - The Answer to this Question.
 * [questionInOrderedQuestion](questionInOrderedQuestion.md) - OrderedQuestions that this Question is indexed in.
 * [questionMultivaluedAnswer](questionMultivaluedAnswer.md) - Indicates whether this question allows multiple answers (true) or it's single answer (false).
 * [questionType](questionType.md) - Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
 * [questionUsedInScoreDefinition](questionUsedInScoreDefinition.md) - The ScoreDefinition that this Question is used in.
 * [➞questionCodingOrdinal](question__questionCodingOrdinal.md) - Indicates if the choices in a choice or open-choice question are ordered (true) or unordered (false, categorical).
 * [➞questionCodingParams](question__questionCodingParams.md) - Code and Display of each option offered as answer to the choice or open-choice question.
 * [➞questionId](question__questionId.md) - The unique identifier for a question in the questionnaire.
 * [➞questionIntervalParams](question__questionIntervalParams.md) - Minimum and Maximum limiting the range the answer must be in for the question.
 * [➞questionLabel](question__questionLabel.md) - The text of the question itself, which is displayed to the user.
 * [➞questionNumericalParams](question__questionNumericalParams.md) - Unit and Precision limiting the quantitative answer for the question.
 * [➞questionRequired](question__questionRequired.md) - Indicates whether answering this question is mandatory (true) or it's optional (false).
 * [➞questionTag](question__questionTag.md) - Internal English identifier, e.g., 'q_pain_level'.
 * [questionnaireAuthoredByOrg](questionnaireAuthoredByOrg.md) - The Organization that has created this Questionnaire.
 * [questionnaireHasOrderedQuestion](questionnaireHasOrderedQuestion.md) - The Question that is part of this Questionnaire, with their display order.
 * [questionnaireHasOrderedSection](questionnaireHasOrderedSection.md) - The Section that is part of this Questionnaire, with their display order.
 * [questionnaireHasQuestionnaireResponse](questionnaireHasQuestionnaireResponse.md) - The QuestionnaireResponse that is associated with this Questionnaire.
 * [questionnairePartOfProcedure](questionnairePartOfProcedure.md) - Procedure this questionnaire is part of.
 * [questionnaireResponseBySubject](questionnaireResponseBySubject.md) - The subject that has authored this QuestionnaireResponse.
 * [questionnaireResponseHasAnswer](questionnaireResponseHasAnswer.md) - The Answer that is part of this QuestionnaireResponse.
 * [questionnaireResponseHasDerivedScoreValue](questionnaireResponseHasDerivedScoreValue.md) - The ScoreValue that is calculated from this QuestionnaireResponse's answers.
 * [questionnaireResponseToQuestionnaire](questionnaireResponseToQuestionnaire.md) - The Questionnaire that this QuestionnaireResponse is for.
 * [➞questionnaireResponseId](questionnaireResponse__questionnaireResponseId.md) - The unique identifier for a specific questionnaire response.
 * [➞questionnaireResponseLastUpdated](questionnaireResponse__questionnaireResponseLastUpdated.md) - The date and time when the questionnaire response was last updated.
 * [➞questionnaireResponseStatus](questionnaireResponse__questionnaireResponseStatus.md) - The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
 * [➞questionnaireResponseTimeStamp](questionnaireResponse__questionnaireResponseTimeStamp.md) - The date and time when the questionnaire response was created (when the questionnaire starts to be answered, not when it's finished).
 * [questionnaireUsesScoreDefinition](questionnaireUsesScoreDefinition.md) - The ScoreDefinition that is applied in this Questionnaire.
 * [➞questionnaireId](questionnaire__questionnaireId.md) - The unique identifier for the questionnaire.
 * [➞questionnaireLabel](questionnaire__questionnaireLabel.md) - The label or title of the questionnaire, which is displayed to the user.
 * [➞questionnaireLastUpdated](questionnaire__questionnaireLastUpdated.md) - The date and time when the questionnaire was last updated.
 * [➞questionnaireStatus](questionnaire__questionnaireStatus.md) - The status of the questionnaire, indicating whether it is draft, active, retired or unknown.
 * [➞questionnaireVersion](questionnaire__questionnaireVersion.md) - Version of the questionnaire.
 * [scoreDefinitionAuthoredByOrg](scoreDefinitionAuthoredByOrg.md) - The Organization that has created this ScoreDefinition.
 * [scoreDefinitionHasScoreParameter](scoreDefinitionHasScoreParameter.md) - The ScoreParameter that is required for this ScoreDefinition.
 * [scoreDefinitionHasScoreValue](scoreDefinitionHasScoreValue.md) - The ScoreValue that is calculated following this ScoreDefinition.
 * [scoreDefinitionType](scoreDefinitionType.md) - Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values.
 * [scoreDefinitionUsedByQuestionnare](scoreDefinitionUsedByQuestionnare.md) - The Questionnaires that this ScoreDefinition is applied in.
 * [scoreDefinitionUsedBySection](scoreDefinitionUsedBySection.md) - The Sections that this ScoreDefinition is applied in.
 * [scoreDefinitionUsesQuestion](scoreDefinitionUsesQuestion.md) - The Question(s) that this ScoreDefinition is based on.
 * [➞scoreDefinitionCategories](scoreDefinition__scoreDefinitionCategories.md) - Categories for categorical scores.
 * [➞scoreDefinitionFormula](scoreDefinition__scoreDefinitionFormula.md) - The formula used to calculate the score.
 * [➞scoreDefinitionId](scoreDefinition__scoreDefinitionId.md) - Unique identifier for the score definition.
 * [➞scoreDefinitionInterpretationGuide](scoreDefinition__scoreDefinitionInterpretationGuide.md) - How to interpret the score values. English explanation.
 * [➞scoreDefinitionIntervalParams](scoreDefinition__scoreDefinitionIntervalParams.md) - Minimum and maximum values for numerical_percentage and numerical_z_score scores.
 * [➞scoreDefinitionLabel](scoreDefinition__scoreDefinitionLabel.md) - Label or title of the score definition.
 * [scoreParameterPartOfScoreDefinition](scoreParameterPartOfScoreDefinition.md) - The ScoreDefinition(s) that this ScoreParameter is part of.
 * [➞scoreParameterId](scoreParameter__scoreParameterId.md) - Unique identifier for the score parameter.
 * [➞scoreParameterLabel](scoreParameter__scoreParameterLabel.md) - Label or title of the parameter. Standard English name.
 * [➞scoreParameterType](scoreParameter__scoreParameterType.md) - Type of parameter: numerical or dateTime.
 * [➞scoreParameterValueDateTime](scoreParameter__scoreParameterValueDateTime.md) - DateTime value parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
 * [➞scoreParameterValueNumerical](scoreParameter__scoreParameterValueNumerical.md) - Numerical value parameter (e.g., 0.785, 82).
 * [scoreValueBasedOnScoreDefinition](scoreValueBasedOnScoreDefinition.md) - The ScoreDefinition that this ScoreValue is based on.
 * [scoreValueDerivedFromQuestionnaireResponse](scoreValueDerivedFromQuestionnaireResponse.md) - The QuestionnaireResponse that contains the answers this ScoreValue is calculated from.
 * [➞scoreValueId](scoreValue__scoreValueId.md) - Unique identifier for the score value.
 * [➞scoreValueNumerical](scoreValue__scoreValueNumerical.md) - Numerical value of the score, used for numerical scores.
 * [➞scoreValueStatus](scoreValue__scoreValueStatus.md) - Status of the score value, e.g., draft, final.
 * [➞scoreValueString](scoreValue__scoreValueString.md) - String representation of the score value, used for categorical scores.
 * [➞scoreValueTimeStamp](scoreValue__scoreValueTimeStamp.md) - Timestamp when the score value was calculated.
 * [sectionAuthoredByOrg](sectionAuthoredByOrg.md) - The Organization that has created this Section.
 * [sectionHasOrderedQuestion](sectionHasOrderedQuestion.md) - The Question that is part of this Section, with their display order.
 * [sectionHasOrderedSection](sectionHasOrderedSection.md) - The Section that is part of this Section.
 * [sectionInOrderedSection](sectionInOrderedSection.md) - OrderedSections that this Section is indexed in.
 * [sectionUsesScoreDefinition](sectionUsesScoreDefinition.md) - The ScoreDefinition that is applied in this Section.
 * [➞sectionId](section__sectionId.md) - The unique identifier for a section in the questionnaire.
 * [➞sectionLabel](section__sectionLabel.md) - The label or title of the section, which is displayed to the user.
 * [➞code](valueCoding__code.md) - The code representing the value (e.g. code '1' for display 'Yes').
 * [➞display](valueCoding__display.md) - The human-readable display text for the code (e.g. code '1' for display 'Yes').
 * [➞dateTimeValue](valueDateTime__dateTimeValue.md) - The date and time value in ISO 8601 format.
 * [➞numericalValue](valueNumerical__numericalValue.md) - The quantitative value, which can be an integer or a float.
 * [➞stringValue](valueString__stringValue.md) - The string value, which can be any text.
 * [vaultManagedByOrg](vaultManagedByOrg.md) - Organization managing this vault.
 * [➞birthdate](vault__birthdate.md) - The date of birth.
 * [➞full_name](vault__full_name.md) - The full name of the vault's user.
 * [➞vaultId](vault__vaultId.md) - The unique identifier for a vault.
 * [➞weight](vault__weight.md) - The weight of the vault's user.
 * [➞weightType](weight__weightType.md) - The type of weight measurement, e.g. measured or stated.

### Enums

 * [MassUnit](MassUnit.md) - Allowed units from UCUM standard for mass.
 * [OrganizationType](OrganizationType.md) - Type of organization: hospital, government, professional, research or serviceProvider.
 * [QuestionType](QuestionType.md) - The type of question asked in the questionnaire. It defines the expected answer format.
 * [QuestionnaireResponseStatus](QuestionnaireResponseStatus.md) - The quesionnaire response status must be one of the following: 'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
 * [QuestionnaireStatus](QuestionnaireStatus.md) - Questionnaires must have one of the following status (FHIR inspired): 
 * [ScoreParameterType](ScoreParameterType.md) - The type of parameter used in the score definition.
 * [ScoreType](ScoreType.md) - The type of score definition, which can be numerical or categorical.
 * [ScoreValueStatus](ScoreValueStatus.md) - The status of a score value, indicating its validity and completeness.
 * [UnitOfMeasure](UnitOfMeasure.md) - Allowed units from UCUM standard.
 * [WeightType](WeightType.md) - Allowed LOINC codes for weight.

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
