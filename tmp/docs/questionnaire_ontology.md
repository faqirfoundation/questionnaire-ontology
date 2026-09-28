
# Questionnaire-Ontology


**metamodel version:** 1.7.0

**version:** 2.0.0


FAQIR Questionnaire Ontology


### Classes

 * [IntervalParams](IntervalParams.md) - Parameters for interval values, including minimum and maximum values.
 * [NumericalParams](NumericalParams.md) - Parameters for quantitative values, including unit and precision.
 * [QuantityValue](QuantityValue.md) - A measured amount (or an amount that can potentially be measured).
 * [ValueCoding](ValueCoding.md) - A coded value with a unique code for each display text, typically used for standardized questionnaires.
 * [FhirReferenceRange](FhirReferenceRange.md) - Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange elements would be used.
 * [FhirValueRatio](FhirValueRatio.md) - A ratio of two Quantity values - a numerator and a denominator
 * [OwlThing](OwlThing.md) - This defines IOT as the set of OWL individuals.
     * [FoafAgent](FoafAgent.md) - An agent (eg. person, group, software or physical artifact).
         * [FoafPerson](FoafPerson.md) - A person.
         * [ProvOrganization](ProvOrganization.md) - An organization is a social or legal institution such as a company, society, etc.
     * [ProvEntity](ProvEntity.md) - An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
         * [QoAnswer](QoAnswer.md) - Answer in the questionnaire response.
         * [QoOrderedQuestion](QoOrderedQuestion.md) - Question's position within a specific questionnaire or section.
         * [QoOrderedSection](QoOrderedSection.md) - Section's position within a specific questionnaire or section.
         * [QoQuestion](QoQuestion.md) - A question.
         * [QoQuestionnaire](QoQuestionnaire.md) - A questionnaire that can be answered (collection of questions).
         * [QoQuestionnaireResponse](QoQuestionnaireResponse.md) - A response to a questionnaire (collection of answers).
         * [QoSection](QoSection.md) - A section of questions in the questionnaire.
         * [SarefProperty](SarefProperty.md) - Identifiable qualities of features of interest that can be target of devices, such as observed or controlled. A property can apply to different features of interest.
         * [SarefPropertyValue](SarefPropertyValue.md) - Describes the value for a property. The property value is optionally linked to its value expressed as an RDF literal (DP saref:hasValue), optionally to the unit of measurement (OP saref:isMeasuredIn), and optionally to the properties or properties of interest it is a value of (OP saref:isValueOfProperty).
             * [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) - The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
             * [QoQuestionnaireStatus](QoQuestionnaireStatus.md) - The status of the questionnaire, indicating whether it is 	draft, active, retired or unknown.
     * [SuloProcess](SuloProcess.md) - a process is a entity that unfolds in time, has temporal parts, and has objects that participate in the process.
         * [FhirProcedure](FhirProcedure.md) - An action that is being or was performed on an individual or entity
         * [S4ehawActivity](S4ehawActivity.md) - The activity of a patient/user, i.e. daily and nocturnal activities.
 * [ProvAttribution](ProvAttribution.md) - An instance of prov:Attribution provides additional descriptions about the binary prov:wasAttributedTo relation from an prov:Entity to some prov:Agent that had some responsible for it. For example, :cake prov:wasAttributedTo :baker; prov:qualifiedAttribution [ a prov:Attribution; prov:entity :baker; :foo :bar ].
 * [TimeDuration](TimeDuration.md) - Duration of a temporal extent expressed as a decimal number scaled by a temporal unit
 * [TimeInterval](TimeInterval.md) - A temporal entity with an extent or duration

### Mixins


### Slots

 * [dcterms_created](dcterms_created.md) - The date and time when the entity was created.
     * [qo_QuestionnaireResponse➞dcterms_created](qo_QuestionnaireResponse_dcterms_created.md) - The date and time when the questionnaire response was created (when the questionnaire starts to be answered, not when it's finished).
     * [qo_Questionnaire➞dcterms_created](qo_Questionnaire_dcterms_created.md) - The date and time when the questionnaire was created.
 * [dcterms_creator](dcterms_creator.md) - An entity responsible for making the resource.
     * [qo_Question➞dcterms_creator](qo_Question_dcterms_creator.md)
     * [qo_Questionnaire➞dcterms_creator](qo_Questionnaire_dcterms_creator.md) - The Organization that has created this Questionnaire.
     * [qo_Section➞dcterms_creator](qo_Section_dcterms_creator.md)
 * [dcterms_hasPart](dcterms_hasPart.md) - A related resource that is included either physically or logically in the described resource.
     * [qo_hasOrderedQuestion](qo_hasOrderedQuestion.md) - The Question that is part of this Questionnaire or Section, with their display order.
         * [qo_Questionnaire➞qo_hasOrderedQuestion](qo_Questionnaire_qo_hasOrderedQuestion.md)
         * [qo_Section➞qo_hasOrderedQuestion](qo_Section_qo_hasOrderedQuestion.md)
     * [qo_hasOrderedSection](qo_hasOrderedSection.md) - The Section that is part of this Questionnaire or Section, with their display order.
         * [qo_Questionnaire➞qo_hasOrderedSection](qo_Questionnaire_qo_hasOrderedSection.md)
         * [qo_Section➞qo_hasOrderedSection](qo_Section_qo_hasOrderedSection.md)
     * [qo_question](qo_question.md) - Question indexed in this OrderedQuestion.
     * [qo_section](qo_section.md) - Section indexed in this OrderedSection.
 * [dcterms_isPartOf](dcterms_isPartOf.md) - A related resource in which the described resource is physically or logically included.
     * [qo_QuestionnaireResponse➞dcterms_isPartOf](qo_QuestionnaireResponse_dcterms_isPartOf.md) - Process this questionnaire response instance is part of.
     * [qo_Questionnaire➞dcterms_isPartOf](qo_Questionnaire_dcterms_isPartOf.md) - Process this questionnaire is part of.
 * [dcterms_modified](dcterms_modified.md) - The date and time when the entity was last updated.
     * [qo_QuestionnaireResponse➞dcterms_modified](qo_QuestionnaireResponse_dcterms_modified.md) - The date and time when the questionnaire response was last updated.
     * [qo_Questionnaire➞dcterms_modified](qo_Questionnaire_dcterms_modified.md) - The date and time when the questionnaire was last updated.
 * [➞highRange](fhirReferenceRange__highRange.md) - High range, if relevant.
 * [➞lowRange](fhirReferenceRange__lowRange.md) - Low range, if relevant.
 * [➞normalValue](fhirReferenceRange__normalValue.md) - Normal value, if relevant.
 * [➞denominator](fhirValueRatio__denominator.md)
 * [➞numerator](fhirValueRatio__numerator.md)
 * [fhir_valueReference](fhir_valueReference.md) - The Reference type contains at least one of a reference (literal reference), an identifier (logical reference), and a display (text description of target). In addition, it may contain a target type.
 * [➞maxLabel](intervalParams__maxLabel.md) - The label for the maximum value of the interval.
 * [➞maxValue](intervalParams__maxValue.md) - The maximum value of the interval.
 * [➞minLabel](intervalParams__minLabel.md) - The label for the minimum value of the interval.
 * [➞minValue](intervalParams__minValue.md) - The minimum value of the interval.
 * [➞numericalPrecision](numericalParams__numericalPrecision.md) - The precision of the quantitative value, e.g. number of decimal places.
 * [➞numericalUnit](numericalParams__numericalUnit.md) - The unit of measure for the quantitative value, from UCUM standard.
 * [owl_versionInfo](owl_versionInfo.md) - An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
 * [prov_atTime](prov_atTime.md) - The time at which an InstantaneousEvent occurred.
 * [prov_endedAtTime](prov_endedAtTime.md) - The time at which an activity ended.
 * [prov_generated](prov_generated.md) - Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
 * [prov_generatedAtTime](prov_generatedAtTime.md) - The time at which an entity was completely created and is available for use.
     * [qo_Answer➞prov_generatedAtTime](qo_Answer_prov_generatedAtTime.md)
 * [prov_hadPrimarySource](prov_hadPrimarySource.md) - A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
 * [prov_qualifiedAttribution](prov_qualifiedAttribution.md) - Attribution is the ascribing of an entity to an agent. When an entity e is attributed to agent ag, entity e was generated by some unspecified activity that in turn was associated to agent ag. Thus, this relation is useful when the activity is not known, or irrelevant.
 * [prov_startedAtTime](prov_startedAtTime.md) - The time at which an activity started.
 * [prov_type](prov_type.md) - The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
     * [qo_Question➞prov_type](qo_Question_prov_type.md) - Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
 * [prov_wasAttributedTo](prov_wasAttributedTo.md) - Attribution is the ascribing of an entity to an agent.
     * [qo_QuestionnaireResponse➞prov_wasAttributedTo](qo_QuestionnaireResponse_prov_wasAttributedTo.md)
 * [prov_wasGeneratedBy](prov_wasGeneratedBy.md) - Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
 * [➞qo_answerValue](qoAnswer__qo_answerValue.md) - The value of the answer to: a decimal or numberInterval type of question, which is a numeric value; a choice, openChoice or text type of question, which is a stringValue; dateTime type of question, which is a datetime value.
 * [➞qo_isEmpty](qoAnswer__qo_isEmpty.md) - True if the answer is intentionally left empty.
 * [➞qo_required](qoOrderedQuestion__qo_required.md) - Whether the question can be left un-answered (false) or an answer is mandatory (true).
 * [➞qo_codingOrdinal](qoQuestion__qo_codingOrdinal.md) - Indicates if the choices in a choice or open-choice question are ordered (true) or unordered (false, categorical).
 * [➞qo_codingParams](qoQuestion__qo_codingParams.md) - Code and Display of each option offered as answer to the choice or open-choice question.
 * [➞qo_intervalParams](qoQuestion__qo_intervalParams.md) - Minimum and Maximum limiting the range the answer must be in for the question.
 * [➞qo_numericalParams](qoQuestion__qo_numericalParams.md) - Unit and Precision limiting the quantitative answer for the question.
 * [➞qo_tag](qoQuestion__qo_tag.md) - Internal English identifier, e.g., 'q_pain_level'.
 * [qo_conditionalValidity](qo_conditionalValidity.md) - a condition (expressed in a machine-readable rule language) that would invalidate the answer earlier than the temporal duration, e.g., 'a documented smoking cessation intervention' invalidates the answer to 'Do you smoke?''.
 * [qo_hardValidity](qo_hardValidity.md) - if true, the temporal duration is a strict deadline; if false, it is an orientative guideline.
 * [qo_hasAnswer](qo_hasAnswer.md) - The Answer that is part of this QuestionnaireResponse.
 * [qo_multivalued](qo_multivalued.md) - Indicates whether this question allows multiple answers (true) or it's single answer (false).
 * [qo_order](qo_order.md) - Position in the questionnaire or section (1-based index).
     * [qo_OrderedQuestion➞qo_order](qo_OrderedQuestion_qo_order.md) - Question position in the questionnaire or section (1-based index).
     * [qo_OrderedSection➞qo_order](qo_OrderedSection_qo_order.md) - Section position in the questionnaire or section (1-based index).
 * [qo_responds](qo_responds.md) - The Questionnaire that this QuestionnaireResponse is for.
 * [qo_temporalValidity](qo_temporalValidity.md) - The time duration during which the answer is considered valid.
 * [qo_toQuestion](qo_toQuestion.md) - The Question that this Answer is for.
 * [rdfs_comment](rdfs_comment.md) - A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
 * [rdfs_label](rdfs_label.md) - human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
 * [s4ehaw_maximumValue](s4ehaw_maximumValue.md) - The maximum allowable value of a measurement.
 * [s4ehaw_minimumValue](s4ehaw_minimumValue.md) - The minimum allowable value of a measurement.
 * [➞fhir_valueAttachement](sarefPropertyValue__fhir_valueAttachement.md) - This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type.
 * [➞fhir_valueCodeableConcept](sarefPropertyValue__fhir_valueCodeableConcept.md) - A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the provision of text. This is a common pattern in healthcare data.
 * [➞fhir_valuePeriod](sarefPropertyValue__fhir_valuePeriod.md) - A time period defined by a start and end date/time. A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. 'the patient was an inpatient of the hospital for this time range') or one value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun 2013').
 * [➞fhir_valueRange](sarefPropertyValue__fhir_valueRange.md) - A set of ordered Quantity values defined by a low and high limit.
 * [➞fhir_valueRatio](sarefPropertyValue__fhir_valueRatio.md) - A relationship between two Quantity values expressed as a numerator and a denominator. The Ratio datatype should only be used to express a relationship of two numbers if the relationship cannot be suitably expressed using a Quantity and a common unit. Where the denominator value is known to be fixed to '1', Quantity should be used instead of Ratio.
 * [➞fhir_referenceRange](sarefProperty__fhir_referenceRange.md) - Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange elements would be used.
 * [saref_hasProperty](saref_hasProperty.md) - Links a feature kind or a feature of interest to one of its properties.
 * [saref_hasPropertyValue](saref_hasPropertyValue.md) - Links a feature kind, a feature of interest, or a property of interest, to a property value.
     * [fhir_status](fhir_status.md) - A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
         * [qo_QuestionnaireResponse➞fhir_status](qo_QuestionnaireResponse_fhir_status.md)
         * [qo_Questionnaire➞fhir_status](qo_Questionnaire_fhir_status.md)
 * [saref_hasValue](saref_hasValue.md) - Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes.
     * [qo_QuestionnaireResponseStatus➞saref_hasValue](qo_QuestionnaireResponseStatus_saref_hasValue.md) - The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
     * [qo_QuestionnaireStatus➞saref_hasValue](qo_QuestionnaireStatus_saref_hasValue.md) - The status of the questionnaire, indicating whether it is 	draft, active, retired or unknown.
 * [saref_isMeasuredIn](saref_isMeasuredIn.md) - A relationship identifying the unit of measure used for a certain entity.
 * [saref_isValueOfProperty](saref_isValueOfProperty.md) - Links a property value to the property or property of interest it is a value of.
 * [time_hasDuration](time_hasDuration.md) - Duration of a temporal entity, expressed as a scaled value or nominal value
 * [➞code](valueCoding__code.md) - The code representing the value (e.g. code '1' for value 'Yes').
 * [➞display](valueCoding__display.md) - The human-readable display text for the code (e.g. code '1' for value 'Yes').

### Enums

 * [qo_QuestionType](qo_QuestionType.md) - The type of question asked in the questionnaire. It defines the expected answer format.
 * [qo_QuestionnaireResponseStatusEnum](qo_QuestionnaireResponseStatusEnum.md) - The quesionnaire response status must be one of the following: 'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
 * [qo_QuestionnaireStatusEnum](qo_QuestionnaireStatusEnum.md) - Questionnaires must have one of the following status (FHIR inspired): 

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
