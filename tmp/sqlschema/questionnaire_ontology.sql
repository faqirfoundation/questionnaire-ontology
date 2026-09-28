-- # Class: "owl_Thing" Description: "This defines IOT as the set of OWL individuals."
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "prov_Attribution" Description: "An instance of prov:Attribution provides additional descriptions about the binary prov:wasAttributedTo relation from an prov:Entity to some prov:Agent that had some responsible for it. For example, :cake prov:wasAttributedTo :baker; prov:qualifiedAttribution [ a prov:Attribution; prov:entity :baker; :foo :bar ]."
--     * Slot: id Description: 
-- # Class: "foaf_Agent" Description: "An agent (eg. person, group, software or physical artifact)."
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "foaf_Person" Description: "A person."
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "prov_Organization" Description: "An organization is a social or legal institution such as a company, society, etc."
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "sulo_Process" Description: "a process is a entity that unfolds in time, has temporal parts, and has objects that participate in the process."
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "s4ehaw_Activity" Description: "The activity of a patient/user, i.e. daily and nocturnal activities."
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "fhir_Procedure" Description: "An action that is being or was performed on an individual or entity"
--     * Slot: id Description: 
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "prov_Entity" Description: "An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary."
--     * Slot: id Description: 
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "saref_Property" Description: "Identifiable qualities of features of interest that can be target of devices, such as observed or controlled. A property can apply to different features of interest."
--     * Slot: id Description: 
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: fhir_referenceRange_id Description: Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange elements would be used.
-- # Class: "saref_PropertyValue" Description: "Describes the value for a property. The property value is optionally linked to its value expressed as an RDF literal (DP saref:hasValue), optionally to the unit of measurement (OP saref:isMeasuredIn), and optionally to the properties or properties of interest it is a value of (OP saref:isValueOfProperty)."
--     * Slot: id Description: 
--     * Slot: prov_atTime Description: The time at which an InstantaneousEvent occurred.
--     * Slot: saref_hasValue Description: Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes.
--     * Slot: fhir_valueReference Description: The Reference type contains at least one of a reference (literal reference), an identifier (logical reference), and a display (text description of target). In addition, it may contain a target type.
--     * Slot: fhir_valueAttachement Description: This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type.
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: saref_isValueOfProperty_id Description: Links a property value to the property or property of interest it is a value of.
--     * Slot: fhir_valueCodeableConcept_id Description: A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the provision of text. This is a common pattern in healthcare data.
--     * Slot: fhir_valueRange_id Description: A set of ordered Quantity values defined by a low and high limit.
--     * Slot: fhir_valueRatio_id Description: A relationship between two Quantity values expressed as a numerator and a denominator. The Ratio datatype should only be used to express a relationship of two numbers if the relationship cannot be suitably expressed using a Quantity and a common unit. Where the denominator value is known to be fixed to '1', Quantity should be used instead of Ratio.
--     * Slot: fhir_valuePeriod_id Description: A time period defined by a start and end date/time. A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. 'the patient was an inpatient of the hospital for this time range') or one value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun 2013').
-- # Class: "QuantityValue" Description: "A measured amount (or an amount that can potentially be measured)."
--     * Slot: id Description: 
--     * Slot: saref_isMeasuredIn Description: A relationship identifying the unit of measure used for a certain entity.
--     * Slot: saref_hasValue Description: Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes.
-- # Class: "NumericalParams" Description: "Parameters for quantitative values, including unit and precision."
--     * Slot: id Description: 
--     * Slot: numericalUnit Description: The unit of measure for the quantitative value, from UCUM standard.
--     * Slot: numericalPrecision Description: The precision of the quantitative value, e.g. number of decimal places.
-- # Class: "ValueCoding" Description: "A coded value with a unique code for each display text, typically used for standardized questionnaires."
--     * Slot: id Description: 
--     * Slot: code Description: The code representing the value (e.g. code '1' for value 'Yes').
--     * Slot: display Description: The human-readable display text for the code (e.g. code '1' for value 'Yes').
-- # Class: "fhir_ValueRatio" Description: "A ratio of two Quantity values - a numerator and a denominator"
--     * Slot: id Description: 
--     * Slot: numerator_id Description: 
--     * Slot: denominator_id Description: 
-- # Class: "IntervalParams" Description: "Parameters for interval values, including minimum and maximum values."
--     * Slot: id Description: 
--     * Slot: minValue Description: The minimum value of the interval.
--     * Slot: minLabel Description: The label for the minimum value of the interval.
--     * Slot: maxValue Description: The maximum value of the interval.
--     * Slot: maxLabel Description: The label for the maximum value of the interval.
-- # Class: "time_Interval" Description: "A temporal entity with an extent or duration"
--     * Slot: id Description: 
--     * Slot: prov_startedAtTime Description: The time at which an activity started.
--     * Slot: prov_endedAtTime Description: The time at which an activity ended.
-- # Class: "time_Duration" Description: "Duration of a temporal extent expressed as a decimal number scaled by a temporal unit"
--     * Slot: id Description: 
--     * Slot: saref_hasValue Description: Value of a property value expressed as an RDF literal. Note that, even if decimal values are expected, values could use other datatypes.
--     * Slot: saref_isMeasuredIn Description: A relationship identifying the unit of measure used for a certain entity.
-- # Class: "fhir_ReferenceRange" Description: "Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange elements would be used."
--     * Slot: id Description: 
--     * Slot: lowRange_id Description: Low range, if relevant.
--     * Slot: highRange_id Description: High range, if relevant.
-- # Class: "qo_Questionnaire" Description: "A questionnaire that can be answered (collection of questions)."
--     * Slot: id Description: 
--     * Slot: dcterms_created Description: The date and time when the questionnaire was created.
--     * Slot: dcterms_modified Description: The date and time when the questionnaire was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: fhir_status_id Description: A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
-- # Class: "qo_QuestionnaireStatus" Description: "The status of the questionnaire, indicating whether it is 	draft, active, retired or unknown."
--     * Slot: id Description: 
--     * Slot: prov_atTime Description: The time at which an InstantaneousEvent occurred.
--     * Slot: saref_hasValue Description: The status of the questionnaire, indicating whether it is 	draft, active, retired or unknown.
--     * Slot: fhir_valueReference Description: The Reference type contains at least one of a reference (literal reference), an identifier (logical reference), and a display (text description of target). In addition, it may contain a target type.
--     * Slot: fhir_valueAttachement Description: This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type.
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: saref_isValueOfProperty_id Description: Links a property value to the property or property of interest it is a value of.
--     * Slot: fhir_valueCodeableConcept_id Description: A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the provision of text. This is a common pattern in healthcare data.
--     * Slot: fhir_valueRange_id Description: A set of ordered Quantity values defined by a low and high limit.
--     * Slot: fhir_valueRatio_id Description: A relationship between two Quantity values expressed as a numerator and a denominator. The Ratio datatype should only be used to express a relationship of two numbers if the relationship cannot be suitably expressed using a Quantity and a common unit. Where the denominator value is known to be fixed to '1', Quantity should be used instead of Ratio.
--     * Slot: fhir_valuePeriod_id Description: A time period defined by a start and end date/time. A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. 'the patient was an inpatient of the hospital for this time range') or one value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun 2013').
-- # Class: "qo_OrderedSection" Description: "Section's position within a specific questionnaire or section."
--     * Slot: id Description: 
--     * Slot: qo_order Description: Section position in the questionnaire or section (1-based index).
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: qo_Section_id Description: Autocreated FK slot
-- # Class: "qo_Section" Description: "A section of questions in the questionnaire."
--     * Slot: id Description: 
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
-- # Class: "qo_OrderedQuestion" Description: "Question's position within a specific questionnaire or section."
--     * Slot: id Description: 
--     * Slot: qo_hardValidity Description: if true, the temporal duration is a strict deadline; if false, it is an orientative guideline.
--     * Slot: qo_conditionalValidity Description: a condition (expressed in a machine-readable rule language) that would invalidate the answer earlier than the temporal duration, e.g., 'a documented smoking cessation intervention' invalidates the answer to 'Do you smoke?''.
--     * Slot: qo_order Description: Question position in the questionnaire or section (1-based index).
--     * Slot: qo_required Description: Whether the question can be left un-answered (false) or an answer is mandatory (true).
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: qo_temporalValidity_id Description: The time duration during which the answer is considered valid.
-- # Class: "qo_Question" Description: "A question."
--     * Slot: id Description: 
--     * Slot: qo_multivalued Description: Indicates whether this question allows multiple answers (true) or it's single answer (false).
--     * Slot: qo_codingOrdinal Description: Indicates if the choices in a choice or open-choice question are ordered (true) or unordered (false, categorical).
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: qo_numericalParams_id Description: Unit and Precision limiting the quantitative answer for the question.
--     * Slot: qo_intervalParams_id Description: Minimum and Maximum limiting the range the answer must be in for the question.
-- # Class: "qo_QuestionnaireResponse" Description: "A response to a questionnaire (collection of answers)."
--     * Slot: id Description: 
--     * Slot: dcterms_created Description: The date and time when the questionnaire response was created (when the questionnaire starts to be answered, not when it's finished).
--     * Slot: dcterms_modified Description: The date and time when the questionnaire response was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: qo_responds_id Description: The Questionnaire that this QuestionnaireResponse is for.
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
--     * Slot: fhir_status_id Description: A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
-- # Class: "qo_QuestionnaireResponseStatus" Description: "The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'."
--     * Slot: id Description: 
--     * Slot: prov_atTime Description: The time at which an InstantaneousEvent occurred.
--     * Slot: saref_hasValue Description: The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
--     * Slot: fhir_valueReference Description: The Reference type contains at least one of a reference (literal reference), an identifier (logical reference), and a display (text description of target). In addition, it may contain a target type.
--     * Slot: fhir_valueAttachement Description: This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type.
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: saref_isValueOfProperty_id Description: Links a property value to the property or property of interest it is a value of.
--     * Slot: fhir_valueCodeableConcept_id Description: A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the provision of text. This is a common pattern in healthcare data.
--     * Slot: fhir_valueRange_id Description: A set of ordered Quantity values defined by a low and high limit.
--     * Slot: fhir_valueRatio_id Description: A relationship between two Quantity values expressed as a numerator and a denominator. The Ratio datatype should only be used to express a relationship of two numbers if the relationship cannot be suitably expressed using a Quantity and a common unit. Where the denominator value is known to be fixed to '1', Quantity should be used instead of Ratio.
--     * Slot: fhir_valuePeriod_id Description: A time period defined by a start and end date/time. A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. 'the patient was an inpatient of the hospital for this time range') or one value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun 2013').
-- # Class: "qo_Answer" Description: "Answer in the questionnaire response."
--     * Slot: id Description: 
--     * Slot: qo_answerValue Description: The value of the answer to: a decimal or numberInterval type of question, which is a numeric value; a choice, openChoice or text type of question, which is a stringValue; dateTime type of question, which is a datetime value.
--     * Slot: qo_isEmpty Description: True if the answer is intentionally left empty.
--     * Slot: dcterms_created Description: The date and time when the entity was created.
--     * Slot: dcterms_modified Description: The date and time when the entity was last updated.
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
--     * Slot: owl_versionInfo Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
--     * Slot: qo_toQuestion_id Description: The Question that this Answer is for.
-- # Class: "owl_Thing_rdfs_label" Description: ""
--     * Slot: owl_Thing_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "owl_Thing_rdfs_comment" Description: ""
--     * Slot: owl_Thing_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "owl_Thing_prov_hadPrimarySource" Description: ""
--     * Slot: owl_Thing_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "owl_Thing_prov_wasGeneratedBy" Description: ""
--     * Slot: owl_Thing_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "foaf_Agent_prov_type" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "foaf_Agent_dcterms_hasPart" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "foaf_Agent_dcterms_isPartOf" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "foaf_Agent_prov_generatedAtTime" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "foaf_Agent_dcterms_creator" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "foaf_Agent_rdfs_label" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "foaf_Agent_rdfs_comment" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "foaf_Agent_prov_hadPrimarySource" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "foaf_Agent_prov_wasGeneratedBy" Description: ""
--     * Slot: foaf_Agent_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "foaf_Person_prov_type" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "foaf_Person_dcterms_hasPart" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "foaf_Person_dcterms_isPartOf" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "foaf_Person_prov_generatedAtTime" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "foaf_Person_dcterms_creator" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "foaf_Person_rdfs_label" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "foaf_Person_rdfs_comment" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "foaf_Person_prov_hadPrimarySource" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "foaf_Person_prov_wasGeneratedBy" Description: ""
--     * Slot: foaf_Person_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "prov_Organization_prov_type" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "prov_Organization_dcterms_hasPart" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "prov_Organization_dcterms_isPartOf" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "prov_Organization_prov_generatedAtTime" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "prov_Organization_dcterms_creator" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "prov_Organization_rdfs_label" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "prov_Organization_rdfs_comment" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "prov_Organization_prov_hadPrimarySource" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "prov_Organization_prov_wasGeneratedBy" Description: ""
--     * Slot: prov_Organization_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "sulo_Process_prov_type" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "sulo_Process_dcterms_hasPart" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "sulo_Process_dcterms_isPartOf" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "sulo_Process_prov_generatedAtTime" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "sulo_Process_dcterms_creator" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "sulo_Process_rdfs_label" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "sulo_Process_rdfs_comment" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "sulo_Process_prov_hadPrimarySource" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "sulo_Process_prov_wasGeneratedBy" Description: ""
--     * Slot: sulo_Process_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "s4ehaw_Activity_prov_type" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "s4ehaw_Activity_dcterms_hasPart" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "s4ehaw_Activity_dcterms_isPartOf" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "s4ehaw_Activity_prov_generatedAtTime" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "s4ehaw_Activity_dcterms_creator" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "s4ehaw_Activity_rdfs_label" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "s4ehaw_Activity_rdfs_comment" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "s4ehaw_Activity_prov_hadPrimarySource" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "s4ehaw_Activity_prov_wasGeneratedBy" Description: ""
--     * Slot: s4ehaw_Activity_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "fhir_Procedure_prov_type" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "fhir_Procedure_dcterms_hasPart" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "fhir_Procedure_dcterms_isPartOf" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "fhir_Procedure_prov_generatedAtTime" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "fhir_Procedure_dcterms_creator" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "fhir_Procedure_rdfs_label" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "fhir_Procedure_rdfs_comment" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "fhir_Procedure_prov_hadPrimarySource" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "fhir_Procedure_prov_wasGeneratedBy" Description: ""
--     * Slot: fhir_Procedure_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "prov_Entity_prov_wasAttributedTo" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "prov_Entity_prov_type" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "prov_Entity_dcterms_hasPart" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "prov_Entity_dcterms_isPartOf" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "prov_Entity_prov_generatedAtTime" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "prov_Entity_dcterms_creator" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "prov_Entity_rdfs_label" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "prov_Entity_rdfs_comment" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "prov_Entity_prov_hadPrimarySource" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "prov_Entity_prov_wasGeneratedBy" Description: ""
--     * Slot: prov_Entity_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "saref_Property_prov_wasAttributedTo" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "saref_Property_prov_type" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "saref_Property_dcterms_hasPart" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "saref_Property_dcterms_isPartOf" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "saref_Property_prov_generatedAtTime" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "saref_Property_dcterms_creator" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "saref_Property_rdfs_label" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "saref_Property_rdfs_comment" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "saref_Property_prov_hadPrimarySource" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "saref_Property_prov_wasGeneratedBy" Description: ""
--     * Slot: saref_Property_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "saref_PropertyValue_prov_wasAttributedTo" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "saref_PropertyValue_prov_type" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "saref_PropertyValue_dcterms_hasPart" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "saref_PropertyValue_dcterms_isPartOf" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "saref_PropertyValue_prov_generatedAtTime" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "saref_PropertyValue_dcterms_creator" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "saref_PropertyValue_rdfs_label" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "saref_PropertyValue_rdfs_comment" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "saref_PropertyValue_prov_hadPrimarySource" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "saref_PropertyValue_prov_wasGeneratedBy" Description: ""
--     * Slot: saref_PropertyValue_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "fhir_ReferenceRange_normalValue" Description: ""
--     * Slot: fhir_ReferenceRange_id Description: Autocreated FK slot
--     * Slot: normalValue_id Description: Normal value, if relevant.
-- # Class: "qo_Questionnaire_prov_wasAttributedTo" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_Questionnaire_prov_type" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_Questionnaire_dcterms_hasPart" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_Questionnaire_dcterms_isPartOf" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: Process this questionnaire is part of.
-- # Class: "qo_Questionnaire_prov_generatedAtTime" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_Questionnaire_dcterms_creator" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: The Organization that has created this Questionnaire.
-- # Class: "qo_Questionnaire_rdfs_label" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_Questionnaire_rdfs_comment" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_Questionnaire_prov_hadPrimarySource" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_Questionnaire_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_Questionnaire_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_QuestionnaireStatus_prov_wasAttributedTo" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_QuestionnaireStatus_prov_type" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_QuestionnaireStatus_dcterms_hasPart" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_QuestionnaireStatus_dcterms_isPartOf" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_QuestionnaireStatus_prov_generatedAtTime" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_QuestionnaireStatus_dcterms_creator" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_QuestionnaireStatus_rdfs_label" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_QuestionnaireStatus_rdfs_comment" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_QuestionnaireStatus_prov_hadPrimarySource" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_QuestionnaireStatus_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_QuestionnaireStatus_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_OrderedSection_qo_section" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: qo_section_id Description: Section indexed in this OrderedSection.
-- # Class: "qo_OrderedSection_prov_wasAttributedTo" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_OrderedSection_prov_type" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_OrderedSection_dcterms_hasPart" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_OrderedSection_dcterms_isPartOf" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_OrderedSection_prov_generatedAtTime" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_OrderedSection_dcterms_creator" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_OrderedSection_rdfs_label" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_OrderedSection_rdfs_comment" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_OrderedSection_prov_hadPrimarySource" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_OrderedSection_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_OrderedSection_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_Section_prov_wasAttributedTo" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_Section_prov_type" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_Section_dcterms_hasPart" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_Section_dcterms_isPartOf" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_Section_prov_generatedAtTime" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_Section_dcterms_creator" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_Section_rdfs_label" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_Section_rdfs_comment" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_Section_prov_hadPrimarySource" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_Section_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_Section_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_OrderedQuestion_qo_question" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: qo_question_id Description: Question indexed in this OrderedQuestion.
-- # Class: "qo_OrderedQuestion_prov_wasAttributedTo" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_OrderedQuestion_prov_type" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_OrderedQuestion_dcterms_hasPart" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_OrderedQuestion_dcterms_isPartOf" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_OrderedQuestion_prov_generatedAtTime" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_OrderedQuestion_dcterms_creator" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_OrderedQuestion_rdfs_label" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_OrderedQuestion_rdfs_comment" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_OrderedQuestion_prov_hadPrimarySource" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_OrderedQuestion_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_OrderedQuestion_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_Question_qo_tag" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: qo_tag Description: Internal English identifier, e.g., 'q_pain_level'.
-- # Class: "qo_Question_qo_codingParams" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: qo_codingParams_id Description: Code and Display of each option offered as answer to the choice or open-choice question.
-- # Class: "qo_Question_prov_wasAttributedTo" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_Question_prov_type" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: prov_type Description: Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
-- # Class: "qo_Question_dcterms_hasPart" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_Question_dcterms_isPartOf" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_Question_prov_generatedAtTime" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_Question_dcterms_creator" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_Question_rdfs_label" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_Question_rdfs_comment" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_Question_prov_hadPrimarySource" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_Question_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_Question_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_QuestionnaireResponse_qo_hasAnswer" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: qo_hasAnswer_id Description: The Answer that is part of this QuestionnaireResponse.
-- # Class: "qo_QuestionnaireResponse_prov_type" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_QuestionnaireResponse_dcterms_hasPart" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_QuestionnaireResponse_dcterms_isPartOf" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: Process this questionnaire response instance is part of.
-- # Class: "qo_QuestionnaireResponse_prov_generatedAtTime" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_QuestionnaireResponse_dcterms_creator" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_QuestionnaireResponse_rdfs_label" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_QuestionnaireResponse_rdfs_comment" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_QuestionnaireResponse_prov_hadPrimarySource" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_QuestionnaireResponse_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_QuestionnaireResponse_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_QuestionnaireResponseStatus_prov_wasAttributedTo" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_QuestionnaireResponseStatus_prov_type" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_QuestionnaireResponseStatus_dcterms_hasPart" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_QuestionnaireResponseStatus_dcterms_isPartOf" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_QuestionnaireResponseStatus_prov_generatedAtTime" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: prov_generatedAtTime Description: The time at which an entity was completely created and is available for use.
-- # Class: "qo_QuestionnaireResponseStatus_dcterms_creator" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_QuestionnaireResponseStatus_rdfs_label" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_QuestionnaireResponseStatus_rdfs_comment" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_QuestionnaireResponseStatus_prov_hadPrimarySource" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_QuestionnaireResponseStatus_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_QuestionnaireResponseStatus_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
-- # Class: "qo_Answer_prov_wasAttributedTo" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: prov_wasAttributedTo_id Description: Attribution is the ascribing of an entity to an agent.
-- # Class: "qo_Answer_prov_type" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: prov_type Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
-- # Class: "qo_Answer_dcterms_hasPart" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: dcterms_hasPart_id Description: A related resource that is included either physically or logically in the described resource.
-- # Class: "qo_Answer_dcterms_isPartOf" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: dcterms_isPartOf_id Description: A related resource in which the described resource is physically or logically included.
-- # Class: "qo_Answer_dcterms_creator" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: dcterms_creator_id Description: An entity responsible for making the resource.
-- # Class: "qo_Answer_rdfs_label" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: rdfs_label Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
-- # Class: "qo_Answer_rdfs_comment" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: rdfs_comment Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
-- # Class: "qo_Answer_prov_hadPrimarySource" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: prov_hadPrimarySource_id Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
-- # Class: "qo_Answer_prov_wasGeneratedBy" Description: ""
--     * Slot: qo_Answer_id Description: Autocreated FK slot
--     * Slot: prov_wasGeneratedBy_id Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.

CREATE TABLE "owl_Thing" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "prov_Attribution" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "foaf_Agent" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "foaf_Person" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "prov_Organization" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "sulo_Process" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "s4ehaw_Activity" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "fhir_Procedure" (
	id INTEGER NOT NULL, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "prov_Entity" (
	id INTEGER NOT NULL, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "saref_Property" (
	id INTEGER NOT NULL, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"foaf_Agent_id" INTEGER, 
	"foaf_Person_id" INTEGER, 
	"prov_Organization_id" INTEGER, 
	"sulo_Process_id" INTEGER, 
	"s4ehaw_Activity_id" INTEGER, 
	"fhir_Procedure_id" INTEGER, 
	"prov_Entity_id" INTEGER, 
	"saref_Property_id" INTEGER, 
	"saref_PropertyValue_id" INTEGER, 
	"qo_Questionnaire_id" INTEGER, 
	"qo_QuestionnaireStatus_id" INTEGER, 
	"qo_OrderedSection_id" INTEGER, 
	"qo_Section_id" INTEGER, 
	"qo_OrderedQuestion_id" INTEGER, 
	"qo_Question_id" INTEGER, 
	"qo_QuestionnaireResponse_id" INTEGER, 
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"qo_Answer_id" INTEGER, 
	"fhir_referenceRange_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("fhir_referenceRange_id") REFERENCES "fhir_ReferenceRange" (id)
);
CREATE TABLE "saref_PropertyValue" (
	id INTEGER NOT NULL, 
	"prov_atTime" DATETIME, 
	"saref_hasValue" TEXT, 
	"fhir_valueReference" TEXT, 
	"fhir_valueAttachement" TEXT, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"foaf_Agent_id" INTEGER, 
	"foaf_Person_id" INTEGER, 
	"prov_Organization_id" INTEGER, 
	"sulo_Process_id" INTEGER, 
	"s4ehaw_Activity_id" INTEGER, 
	"fhir_Procedure_id" INTEGER, 
	"prov_Entity_id" INTEGER, 
	"saref_Property_id" INTEGER, 
	"saref_PropertyValue_id" INTEGER, 
	"qo_Questionnaire_id" INTEGER, 
	"qo_QuestionnaireStatus_id" INTEGER, 
	"qo_OrderedSection_id" INTEGER, 
	"qo_Section_id" INTEGER, 
	"qo_OrderedQuestion_id" INTEGER, 
	"qo_Question_id" INTEGER, 
	"qo_QuestionnaireResponse_id" INTEGER, 
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"qo_Answer_id" INTEGER, 
	"saref_isValueOfProperty_id" INTEGER, 
	"fhir_valueCodeableConcept_id" INTEGER, 
	"fhir_valueRange_id" INTEGER, 
	"fhir_valueRatio_id" INTEGER, 
	"fhir_valuePeriod_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("saref_isValueOfProperty_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("fhir_valueCodeableConcept_id") REFERENCES "ValueCoding" (id), 
	FOREIGN KEY("fhir_valueRange_id") REFERENCES "fhir_ReferenceRange" (id), 
	FOREIGN KEY("fhir_valueRatio_id") REFERENCES "fhir_ValueRatio" (id), 
	FOREIGN KEY("fhir_valuePeriod_id") REFERENCES "time_Interval" (id)
);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL, 
	"saref_isMeasuredIn" TEXT, 
	"saref_hasValue" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NumericalParams" (
	id INTEGER NOT NULL, 
	"numericalUnit" TEXT, 
	"numericalPrecision" INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "ValueCoding" (
	id INTEGER NOT NULL, 
	code TEXT NOT NULL, 
	display TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "IntervalParams" (
	id INTEGER NOT NULL, 
	"minValue" FLOAT, 
	"minLabel" TEXT, 
	"maxValue" FLOAT, 
	"maxLabel" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "time_Interval" (
	id INTEGER NOT NULL, 
	"prov_startedAtTime" DATETIME, 
	"prov_endedAtTime" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "time_Duration" (
	id INTEGER NOT NULL, 
	"saref_hasValue" TEXT, 
	"saref_isMeasuredIn" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "qo_Questionnaire" (
	id INTEGER NOT NULL, 
	dcterms_created DATETIME NOT NULL, 
	dcterms_modified DATETIME NOT NULL, 
	"owl_versionInfo" TEXT, 
	fhir_status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(fhir_status_id) REFERENCES "qo_QuestionnaireStatus" (id)
);
CREATE TABLE "qo_QuestionnaireStatus" (
	id INTEGER NOT NULL, 
	"prov_atTime" DATETIME, 
	"saref_hasValue" VARCHAR(7) NOT NULL, 
	"fhir_valueReference" TEXT, 
	"fhir_valueAttachement" TEXT, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"saref_isValueOfProperty_id" INTEGER, 
	"fhir_valueCodeableConcept_id" INTEGER, 
	"fhir_valueRange_id" INTEGER, 
	"fhir_valueRatio_id" INTEGER, 
	"fhir_valuePeriod_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("saref_isValueOfProperty_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("fhir_valueCodeableConcept_id") REFERENCES "ValueCoding" (id), 
	FOREIGN KEY("fhir_valueRange_id") REFERENCES "fhir_ReferenceRange" (id), 
	FOREIGN KEY("fhir_valueRatio_id") REFERENCES "fhir_ValueRatio" (id), 
	FOREIGN KEY("fhir_valuePeriod_id") REFERENCES "time_Interval" (id)
);
CREATE TABLE "qo_OrderedSection" (
	id INTEGER NOT NULL, 
	qo_order INTEGER NOT NULL, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"qo_Questionnaire_id" INTEGER, 
	"qo_Section_id" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (qo_order), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id)
);
CREATE TABLE "qo_Section" (
	id INTEGER NOT NULL, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "qo_OrderedQuestion" (
	id INTEGER NOT NULL, 
	"qo_hardValidity" BOOLEAN, 
	"qo_conditionalValidity" TEXT NOT NULL, 
	qo_order INTEGER NOT NULL, 
	qo_required BOOLEAN NOT NULL, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"qo_Questionnaire_id" INTEGER, 
	"qo_Section_id" INTEGER, 
	"qo_temporalValidity_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (qo_order), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("qo_temporalValidity_id") REFERENCES "time_Duration" (id)
);
CREATE TABLE "qo_QuestionnaireResponse" (
	id INTEGER NOT NULL, 
	dcterms_created DATETIME NOT NULL, 
	dcterms_modified DATETIME NOT NULL, 
	"owl_versionInfo" TEXT, 
	qo_responds_id INTEGER NOT NULL, 
	"prov_wasAttributedTo_id" INTEGER NOT NULL, 
	fhir_status_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(qo_responds_id) REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY(fhir_status_id) REFERENCES "qo_QuestionnaireResponseStatus" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus" (
	id INTEGER NOT NULL, 
	"prov_atTime" DATETIME, 
	"saref_hasValue" VARCHAR(16) NOT NULL, 
	"fhir_valueReference" TEXT, 
	"fhir_valueAttachement" TEXT, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"saref_isValueOfProperty_id" INTEGER, 
	"fhir_valueCodeableConcept_id" INTEGER, 
	"fhir_valueRange_id" INTEGER, 
	"fhir_valueRatio_id" INTEGER, 
	"fhir_valuePeriod_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("saref_isValueOfProperty_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("fhir_valueCodeableConcept_id") REFERENCES "ValueCoding" (id), 
	FOREIGN KEY("fhir_valueRange_id") REFERENCES "fhir_ReferenceRange" (id), 
	FOREIGN KEY("fhir_valueRatio_id") REFERENCES "fhir_ValueRatio" (id), 
	FOREIGN KEY("fhir_valuePeriod_id") REFERENCES "time_Interval" (id)
);
CREATE TABLE "fhir_ValueRatio" (
	id INTEGER NOT NULL, 
	numerator_id INTEGER NOT NULL, 
	denominator_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(numerator_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(denominator_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "fhir_ReferenceRange" (
	id INTEGER NOT NULL, 
	"lowRange_id" INTEGER, 
	"highRange_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("lowRange_id") REFERENCES "QuantityValue" (id), 
	FOREIGN KEY("highRange_id") REFERENCES "QuantityValue" (id)
);
CREATE TABLE "qo_Question" (
	id INTEGER NOT NULL, 
	qo_multivalued BOOLEAN, 
	"qo_codingOrdinal" BOOLEAN, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"owl_versionInfo" TEXT, 
	"qo_numericalParams_id" INTEGER, 
	"qo_intervalParams_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("qo_numericalParams_id") REFERENCES "NumericalParams" (id), 
	FOREIGN KEY("qo_intervalParams_id") REFERENCES "IntervalParams" (id)
);
CREATE TABLE "owl_Thing_rdfs_label" (
	"owl_Thing_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("owl_Thing_id", rdfs_label), 
	FOREIGN KEY("owl_Thing_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "owl_Thing_rdfs_comment" (
	"owl_Thing_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("owl_Thing_id", rdfs_comment), 
	FOREIGN KEY("owl_Thing_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "owl_Thing_prov_hadPrimarySource" (
	"owl_Thing_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("owl_Thing_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("owl_Thing_id") REFERENCES "owl_Thing" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "owl_Thing_prov_wasGeneratedBy" (
	"owl_Thing_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("owl_Thing_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("owl_Thing_id") REFERENCES "owl_Thing" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "foaf_Agent_prov_type" (
	"foaf_Agent_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("foaf_Agent_id", prov_type), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "foaf_Agent_dcterms_hasPart" (
	"foaf_Agent_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("foaf_Agent_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "foaf_Agent_dcterms_isPartOf" (
	"foaf_Agent_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("foaf_Agent_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "foaf_Agent_prov_generatedAtTime" (
	"foaf_Agent_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("foaf_Agent_id", "prov_generatedAtTime"), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "foaf_Agent_dcterms_creator" (
	"foaf_Agent_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("foaf_Agent_id", dcterms_creator_id), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "foaf_Agent_rdfs_label" (
	"foaf_Agent_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("foaf_Agent_id", rdfs_label), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "foaf_Agent_rdfs_comment" (
	"foaf_Agent_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("foaf_Agent_id", rdfs_comment), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "foaf_Agent_prov_hadPrimarySource" (
	"foaf_Agent_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("foaf_Agent_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "foaf_Agent_prov_wasGeneratedBy" (
	"foaf_Agent_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("foaf_Agent_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("foaf_Agent_id") REFERENCES "foaf_Agent" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "foaf_Person_prov_type" (
	"foaf_Person_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("foaf_Person_id", prov_type), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id)
);
CREATE TABLE "foaf_Person_dcterms_hasPart" (
	"foaf_Person_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("foaf_Person_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "foaf_Person_dcterms_isPartOf" (
	"foaf_Person_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("foaf_Person_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "foaf_Person_prov_generatedAtTime" (
	"foaf_Person_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("foaf_Person_id", "prov_generatedAtTime"), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id)
);
CREATE TABLE "foaf_Person_dcterms_creator" (
	"foaf_Person_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("foaf_Person_id", dcterms_creator_id), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "foaf_Person_rdfs_label" (
	"foaf_Person_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("foaf_Person_id", rdfs_label), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id)
);
CREATE TABLE "foaf_Person_rdfs_comment" (
	"foaf_Person_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("foaf_Person_id", rdfs_comment), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id)
);
CREATE TABLE "foaf_Person_prov_hadPrimarySource" (
	"foaf_Person_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("foaf_Person_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "foaf_Person_prov_wasGeneratedBy" (
	"foaf_Person_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("foaf_Person_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("foaf_Person_id") REFERENCES "foaf_Person" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "prov_Organization_prov_type" (
	"prov_Organization_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("prov_Organization_id", prov_type), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id)
);
CREATE TABLE "prov_Organization_dcterms_hasPart" (
	"prov_Organization_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("prov_Organization_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "prov_Organization_dcterms_isPartOf" (
	"prov_Organization_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("prov_Organization_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "prov_Organization_prov_generatedAtTime" (
	"prov_Organization_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("prov_Organization_id", "prov_generatedAtTime"), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id)
);
CREATE TABLE "prov_Organization_dcterms_creator" (
	"prov_Organization_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("prov_Organization_id", dcterms_creator_id), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "prov_Organization_rdfs_label" (
	"prov_Organization_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("prov_Organization_id", rdfs_label), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id)
);
CREATE TABLE "prov_Organization_rdfs_comment" (
	"prov_Organization_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("prov_Organization_id", rdfs_comment), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id)
);
CREATE TABLE "prov_Organization_prov_hadPrimarySource" (
	"prov_Organization_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("prov_Organization_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "prov_Organization_prov_wasGeneratedBy" (
	"prov_Organization_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("prov_Organization_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("prov_Organization_id") REFERENCES "prov_Organization" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "sulo_Process_prov_type" (
	"sulo_Process_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("sulo_Process_id", prov_type), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "sulo_Process_dcterms_hasPart" (
	"sulo_Process_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("sulo_Process_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "sulo_Process_dcterms_isPartOf" (
	"sulo_Process_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("sulo_Process_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "sulo_Process_prov_generatedAtTime" (
	"sulo_Process_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("sulo_Process_id", "prov_generatedAtTime"), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "sulo_Process_dcterms_creator" (
	"sulo_Process_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("sulo_Process_id", dcterms_creator_id), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "sulo_Process_rdfs_label" (
	"sulo_Process_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("sulo_Process_id", rdfs_label), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "sulo_Process_rdfs_comment" (
	"sulo_Process_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("sulo_Process_id", rdfs_comment), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "sulo_Process_prov_hadPrimarySource" (
	"sulo_Process_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("sulo_Process_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "sulo_Process_prov_wasGeneratedBy" (
	"sulo_Process_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("sulo_Process_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("sulo_Process_id") REFERENCES "sulo_Process" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "s4ehaw_Activity_prov_type" (
	"s4ehaw_Activity_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("s4ehaw_Activity_id", prov_type), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id)
);
CREATE TABLE "s4ehaw_Activity_dcterms_hasPart" (
	"s4ehaw_Activity_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("s4ehaw_Activity_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "s4ehaw_Activity_dcterms_isPartOf" (
	"s4ehaw_Activity_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("s4ehaw_Activity_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "s4ehaw_Activity_prov_generatedAtTime" (
	"s4ehaw_Activity_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("s4ehaw_Activity_id", "prov_generatedAtTime"), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id)
);
CREATE TABLE "s4ehaw_Activity_dcterms_creator" (
	"s4ehaw_Activity_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("s4ehaw_Activity_id", dcterms_creator_id), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "s4ehaw_Activity_rdfs_label" (
	"s4ehaw_Activity_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("s4ehaw_Activity_id", rdfs_label), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id)
);
CREATE TABLE "s4ehaw_Activity_rdfs_comment" (
	"s4ehaw_Activity_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("s4ehaw_Activity_id", rdfs_comment), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id)
);
CREATE TABLE "s4ehaw_Activity_prov_hadPrimarySource" (
	"s4ehaw_Activity_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("s4ehaw_Activity_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "s4ehaw_Activity_prov_wasGeneratedBy" (
	"s4ehaw_Activity_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("s4ehaw_Activity_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("s4ehaw_Activity_id") REFERENCES "s4ehaw_Activity" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "fhir_Procedure_prov_type" (
	"fhir_Procedure_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("fhir_Procedure_id", prov_type), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id)
);
CREATE TABLE "fhir_Procedure_dcterms_hasPart" (
	"fhir_Procedure_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("fhir_Procedure_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "fhir_Procedure_dcterms_isPartOf" (
	"fhir_Procedure_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("fhir_Procedure_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "fhir_Procedure_prov_generatedAtTime" (
	"fhir_Procedure_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("fhir_Procedure_id", "prov_generatedAtTime"), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id)
);
CREATE TABLE "fhir_Procedure_dcterms_creator" (
	"fhir_Procedure_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("fhir_Procedure_id", dcterms_creator_id), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "fhir_Procedure_rdfs_label" (
	"fhir_Procedure_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("fhir_Procedure_id", rdfs_label), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id)
);
CREATE TABLE "fhir_Procedure_rdfs_comment" (
	"fhir_Procedure_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("fhir_Procedure_id", rdfs_comment), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id)
);
CREATE TABLE "fhir_Procedure_prov_hadPrimarySource" (
	"fhir_Procedure_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("fhir_Procedure_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "fhir_Procedure_prov_wasGeneratedBy" (
	"fhir_Procedure_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("fhir_Procedure_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("fhir_Procedure_id") REFERENCES "fhir_Procedure" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "prov_Entity_prov_wasAttributedTo" (
	"prov_Entity_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("prov_Entity_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "prov_Entity_prov_type" (
	"prov_Entity_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("prov_Entity_id", prov_type), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "prov_Entity_dcterms_hasPart" (
	"prov_Entity_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("prov_Entity_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "prov_Entity_dcterms_isPartOf" (
	"prov_Entity_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("prov_Entity_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "prov_Entity_prov_generatedAtTime" (
	"prov_Entity_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("prov_Entity_id", "prov_generatedAtTime"), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "prov_Entity_dcterms_creator" (
	"prov_Entity_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("prov_Entity_id", dcterms_creator_id), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "prov_Entity_rdfs_label" (
	"prov_Entity_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("prov_Entity_id", rdfs_label), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "prov_Entity_rdfs_comment" (
	"prov_Entity_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("prov_Entity_id", rdfs_comment), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "prov_Entity_prov_hadPrimarySource" (
	"prov_Entity_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("prov_Entity_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "prov_Entity_prov_wasGeneratedBy" (
	"prov_Entity_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("prov_Entity_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("prov_Entity_id") REFERENCES "prov_Entity" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "saref_Property_prov_wasAttributedTo" (
	"saref_Property_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("saref_Property_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "saref_Property_prov_type" (
	"saref_Property_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("saref_Property_id", prov_type), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id)
);
CREATE TABLE "saref_Property_dcterms_hasPart" (
	"saref_Property_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("saref_Property_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "saref_Property_dcterms_isPartOf" (
	"saref_Property_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("saref_Property_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "saref_Property_prov_generatedAtTime" (
	"saref_Property_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("saref_Property_id", "prov_generatedAtTime"), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id)
);
CREATE TABLE "saref_Property_dcterms_creator" (
	"saref_Property_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("saref_Property_id", dcterms_creator_id), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "saref_Property_rdfs_label" (
	"saref_Property_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("saref_Property_id", rdfs_label), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id)
);
CREATE TABLE "saref_Property_rdfs_comment" (
	"saref_Property_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("saref_Property_id", rdfs_comment), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id)
);
CREATE TABLE "saref_Property_prov_hadPrimarySource" (
	"saref_Property_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("saref_Property_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "saref_Property_prov_wasGeneratedBy" (
	"saref_Property_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("saref_Property_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("saref_Property_id") REFERENCES "saref_Property" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "saref_PropertyValue_prov_wasAttributedTo" (
	"saref_PropertyValue_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("saref_PropertyValue_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "saref_PropertyValue_prov_type" (
	"saref_PropertyValue_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("saref_PropertyValue_id", prov_type), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id)
);
CREATE TABLE "saref_PropertyValue_dcterms_hasPart" (
	"saref_PropertyValue_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("saref_PropertyValue_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "saref_PropertyValue_dcterms_isPartOf" (
	"saref_PropertyValue_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("saref_PropertyValue_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "saref_PropertyValue_prov_generatedAtTime" (
	"saref_PropertyValue_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("saref_PropertyValue_id", "prov_generatedAtTime"), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id)
);
CREATE TABLE "saref_PropertyValue_dcterms_creator" (
	"saref_PropertyValue_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("saref_PropertyValue_id", dcterms_creator_id), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "saref_PropertyValue_rdfs_label" (
	"saref_PropertyValue_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("saref_PropertyValue_id", rdfs_label), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id)
);
CREATE TABLE "saref_PropertyValue_rdfs_comment" (
	"saref_PropertyValue_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("saref_PropertyValue_id", rdfs_comment), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id)
);
CREATE TABLE "saref_PropertyValue_prov_hadPrimarySource" (
	"saref_PropertyValue_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("saref_PropertyValue_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "saref_PropertyValue_prov_wasGeneratedBy" (
	"saref_PropertyValue_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("saref_PropertyValue_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("saref_PropertyValue_id") REFERENCES "saref_PropertyValue" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_Questionnaire_prov_wasAttributedTo" (
	"qo_Questionnaire_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_Questionnaire_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_Questionnaire_prov_type" (
	"qo_Questionnaire_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_Questionnaire_id", prov_type), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id)
);
CREATE TABLE "qo_Questionnaire_dcterms_hasPart" (
	"qo_Questionnaire_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_Questionnaire_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Questionnaire_dcterms_isPartOf" (
	"qo_Questionnaire_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_Questionnaire_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_Questionnaire_prov_generatedAtTime" (
	"qo_Questionnaire_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_Questionnaire_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id)
);
CREATE TABLE "qo_Questionnaire_dcterms_creator" (
	"qo_Questionnaire_id" INTEGER, 
	dcterms_creator_id INTEGER NOT NULL, 
	PRIMARY KEY ("qo_Questionnaire_id", dcterms_creator_id), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "prov_Organization" (id)
);
CREATE TABLE "qo_Questionnaire_rdfs_label" (
	"qo_Questionnaire_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_Questionnaire_id", rdfs_label), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id)
);
CREATE TABLE "qo_Questionnaire_rdfs_comment" (
	"qo_Questionnaire_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_Questionnaire_id", rdfs_comment), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id)
);
CREATE TABLE "qo_Questionnaire_prov_hadPrimarySource" (
	"qo_Questionnaire_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_Questionnaire_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_Questionnaire_prov_wasGeneratedBy" (
	"qo_Questionnaire_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_Questionnaire_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_Questionnaire_id") REFERENCES "qo_Questionnaire" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_prov_wasAttributedTo" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_prov_type" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", prov_type), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_dcterms_hasPart" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_dcterms_isPartOf" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_prov_generatedAtTime" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_dcterms_creator" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", dcterms_creator_id), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_rdfs_label" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", rdfs_label), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_rdfs_comment" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", rdfs_comment), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_prov_hadPrimarySource" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_QuestionnaireStatus_prov_wasGeneratedBy" (
	"qo_QuestionnaireStatus_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireStatus_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_QuestionnaireStatus_id") REFERENCES "qo_QuestionnaireStatus" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_OrderedSection_qo_section" (
	"qo_OrderedSection_id" INTEGER, 
	qo_section_id INTEGER NOT NULL, 
	PRIMARY KEY ("qo_OrderedSection_id", qo_section_id), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY(qo_section_id) REFERENCES "qo_Section" (id)
);
CREATE TABLE "qo_OrderedSection_prov_wasAttributedTo" (
	"qo_OrderedSection_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedSection_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_OrderedSection_prov_type" (
	"qo_OrderedSection_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_OrderedSection_id", prov_type), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id)
);
CREATE TABLE "qo_OrderedSection_dcterms_hasPart" (
	"qo_OrderedSection_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedSection_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_OrderedSection_dcterms_isPartOf" (
	"qo_OrderedSection_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedSection_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_OrderedSection_prov_generatedAtTime" (
	"qo_OrderedSection_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_OrderedSection_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id)
);
CREATE TABLE "qo_OrderedSection_dcterms_creator" (
	"qo_OrderedSection_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("qo_OrderedSection_id", dcterms_creator_id), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_OrderedSection_rdfs_label" (
	"qo_OrderedSection_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_OrderedSection_id", rdfs_label), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id)
);
CREATE TABLE "qo_OrderedSection_rdfs_comment" (
	"qo_OrderedSection_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_OrderedSection_id", rdfs_comment), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id)
);
CREATE TABLE "qo_OrderedSection_prov_hadPrimarySource" (
	"qo_OrderedSection_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedSection_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_OrderedSection_prov_wasGeneratedBy" (
	"qo_OrderedSection_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedSection_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_OrderedSection_id") REFERENCES "qo_OrderedSection" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_Section_prov_wasAttributedTo" (
	"qo_Section_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_Section_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_Section_prov_type" (
	"qo_Section_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_Section_id", prov_type), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id)
);
CREATE TABLE "qo_Section_dcterms_hasPart" (
	"qo_Section_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_Section_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Section_dcterms_isPartOf" (
	"qo_Section_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_Section_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Section_prov_generatedAtTime" (
	"qo_Section_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_Section_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id)
);
CREATE TABLE "qo_Section_dcterms_creator" (
	"qo_Section_id" INTEGER, 
	dcterms_creator_id INTEGER NOT NULL, 
	PRIMARY KEY ("qo_Section_id", dcterms_creator_id), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "prov_Organization" (id)
);
CREATE TABLE "qo_Section_rdfs_label" (
	"qo_Section_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_Section_id", rdfs_label), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id)
);
CREATE TABLE "qo_Section_rdfs_comment" (
	"qo_Section_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_Section_id", rdfs_comment), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id)
);
CREATE TABLE "qo_Section_prov_hadPrimarySource" (
	"qo_Section_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_Section_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_Section_prov_wasGeneratedBy" (
	"qo_Section_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_Section_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_Section_id") REFERENCES "qo_Section" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_OrderedQuestion_prov_wasAttributedTo" (
	"qo_OrderedQuestion_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedQuestion_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_OrderedQuestion_prov_type" (
	"qo_OrderedQuestion_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_OrderedQuestion_id", prov_type), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id)
);
CREATE TABLE "qo_OrderedQuestion_dcterms_hasPart" (
	"qo_OrderedQuestion_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedQuestion_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_OrderedQuestion_dcterms_isPartOf" (
	"qo_OrderedQuestion_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedQuestion_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_OrderedQuestion_prov_generatedAtTime" (
	"qo_OrderedQuestion_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_OrderedQuestion_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id)
);
CREATE TABLE "qo_OrderedQuestion_dcterms_creator" (
	"qo_OrderedQuestion_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("qo_OrderedQuestion_id", dcterms_creator_id), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_OrderedQuestion_rdfs_label" (
	"qo_OrderedQuestion_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_OrderedQuestion_id", rdfs_label), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id)
);
CREATE TABLE "qo_OrderedQuestion_rdfs_comment" (
	"qo_OrderedQuestion_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_OrderedQuestion_id", rdfs_comment), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id)
);
CREATE TABLE "qo_OrderedQuestion_prov_hadPrimarySource" (
	"qo_OrderedQuestion_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedQuestion_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_OrderedQuestion_prov_wasGeneratedBy" (
	"qo_OrderedQuestion_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_OrderedQuestion_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_prov_type" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", prov_type), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_dcterms_hasPart" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_dcterms_isPartOf" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_prov_generatedAtTime" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_dcterms_creator" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", dcterms_creator_id), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_rdfs_label" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", rdfs_label), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_rdfs_comment" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", rdfs_comment), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_prov_hadPrimarySource" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_prov_wasGeneratedBy" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_prov_wasAttributedTo" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_prov_type" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", prov_type), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_dcterms_hasPart" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_dcterms_isPartOf" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_prov_generatedAtTime" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_dcterms_creator" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", dcterms_creator_id), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_rdfs_label" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", rdfs_label), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_rdfs_comment" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", rdfs_comment), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_prov_hadPrimarySource" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_QuestionnaireResponseStatus_prov_wasGeneratedBy" (
	"qo_QuestionnaireResponseStatus_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_QuestionnaireResponseStatus_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_QuestionnaireResponseStatus_id") REFERENCES "qo_QuestionnaireResponseStatus" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_Answer" (
	id INTEGER NOT NULL, 
	"qo_answerValue" TEXT, 
	"qo_isEmpty" BOOLEAN, 
	dcterms_created DATETIME, 
	dcterms_modified DATETIME, 
	"prov_generatedAtTime" DATETIME NOT NULL, 
	"owl_versionInfo" TEXT, 
	"qo_toQuestion_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("qo_toQuestion_id") REFERENCES "qo_Question" (id)
);
CREATE TABLE "fhir_ReferenceRange_normalValue" (
	"fhir_ReferenceRange_id" INTEGER, 
	"normalValue_id" INTEGER, 
	PRIMARY KEY ("fhir_ReferenceRange_id", "normalValue_id"), 
	FOREIGN KEY("fhir_ReferenceRange_id") REFERENCES "fhir_ReferenceRange" (id), 
	FOREIGN KEY("normalValue_id") REFERENCES "QuantityValue" (id)
);
CREATE TABLE "qo_OrderedQuestion_qo_question" (
	"qo_OrderedQuestion_id" INTEGER, 
	qo_question_id INTEGER NOT NULL, 
	PRIMARY KEY ("qo_OrderedQuestion_id", qo_question_id), 
	FOREIGN KEY("qo_OrderedQuestion_id") REFERENCES "qo_OrderedQuestion" (id), 
	FOREIGN KEY(qo_question_id) REFERENCES "qo_Question" (id)
);
CREATE TABLE "qo_Question_qo_tag" (
	"qo_Question_id" INTEGER, 
	qo_tag TEXT NOT NULL, 
	PRIMARY KEY ("qo_Question_id", qo_tag), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id)
);
CREATE TABLE "qo_Question_qo_codingParams" (
	"qo_Question_id" INTEGER, 
	"qo_codingParams_id" INTEGER, 
	PRIMARY KEY ("qo_Question_id", "qo_codingParams_id"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("qo_codingParams_id") REFERENCES "ValueCoding" (id)
);
CREATE TABLE "qo_Question_prov_wasAttributedTo" (
	"qo_Question_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_Question_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_Question_prov_type" (
	"qo_Question_id" INTEGER, 
	prov_type VARCHAR(14) NOT NULL, 
	PRIMARY KEY ("qo_Question_id", prov_type), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id)
);
CREATE TABLE "qo_Question_dcterms_hasPart" (
	"qo_Question_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_Question_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Question_dcterms_isPartOf" (
	"qo_Question_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_Question_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Question_prov_generatedAtTime" (
	"qo_Question_id" INTEGER, 
	"prov_generatedAtTime" DATETIME, 
	PRIMARY KEY ("qo_Question_id", "prov_generatedAtTime"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id)
);
CREATE TABLE "qo_Question_dcterms_creator" (
	"qo_Question_id" INTEGER, 
	dcterms_creator_id INTEGER NOT NULL, 
	PRIMARY KEY ("qo_Question_id", dcterms_creator_id), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "prov_Organization" (id)
);
CREATE TABLE "qo_Question_rdfs_label" (
	"qo_Question_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_Question_id", rdfs_label), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id)
);
CREATE TABLE "qo_Question_rdfs_comment" (
	"qo_Question_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_Question_id", rdfs_comment), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id)
);
CREATE TABLE "qo_Question_prov_hadPrimarySource" (
	"qo_Question_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_Question_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_Question_prov_wasGeneratedBy" (
	"qo_Question_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_Question_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_Question_id") REFERENCES "qo_Question" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);
CREATE TABLE "qo_QuestionnaireResponse_qo_hasAnswer" (
	"qo_QuestionnaireResponse_id" INTEGER, 
	"qo_hasAnswer_id" INTEGER NOT NULL, 
	PRIMARY KEY ("qo_QuestionnaireResponse_id", "qo_hasAnswer_id"), 
	FOREIGN KEY("qo_QuestionnaireResponse_id") REFERENCES "qo_QuestionnaireResponse" (id), 
	FOREIGN KEY("qo_hasAnswer_id") REFERENCES "qo_Answer" (id)
);
CREATE TABLE "qo_Answer_prov_wasAttributedTo" (
	"qo_Answer_id" INTEGER, 
	"prov_wasAttributedTo_id" INTEGER, 
	PRIMARY KEY ("qo_Answer_id", "prov_wasAttributedTo_id"), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("prov_wasAttributedTo_id") REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_Answer_prov_type" (
	"qo_Answer_id" INTEGER, 
	prov_type TEXT, 
	PRIMARY KEY ("qo_Answer_id", prov_type), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id)
);
CREATE TABLE "qo_Answer_dcterms_hasPart" (
	"qo_Answer_id" INTEGER, 
	"dcterms_hasPart_id" INTEGER, 
	PRIMARY KEY ("qo_Answer_id", "dcterms_hasPart_id"), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("dcterms_hasPart_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Answer_dcterms_isPartOf" (
	"qo_Answer_id" INTEGER, 
	"dcterms_isPartOf_id" INTEGER, 
	PRIMARY KEY ("qo_Answer_id", "dcterms_isPartOf_id"), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("dcterms_isPartOf_id") REFERENCES "owl_Thing" (id)
);
CREATE TABLE "qo_Answer_dcterms_creator" (
	"qo_Answer_id" INTEGER, 
	dcterms_creator_id INTEGER, 
	PRIMARY KEY ("qo_Answer_id", dcterms_creator_id), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY(dcterms_creator_id) REFERENCES "foaf_Agent" (id)
);
CREATE TABLE "qo_Answer_rdfs_label" (
	"qo_Answer_id" INTEGER, 
	rdfs_label TEXT NOT NULL, 
	PRIMARY KEY ("qo_Answer_id", rdfs_label), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id)
);
CREATE TABLE "qo_Answer_rdfs_comment" (
	"qo_Answer_id" INTEGER, 
	rdfs_comment TEXT NOT NULL, 
	PRIMARY KEY ("qo_Answer_id", rdfs_comment), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id)
);
CREATE TABLE "qo_Answer_prov_hadPrimarySource" (
	"qo_Answer_id" INTEGER, 
	"prov_hadPrimarySource_id" INTEGER, 
	PRIMARY KEY ("qo_Answer_id", "prov_hadPrimarySource_id"), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("prov_hadPrimarySource_id") REFERENCES "prov_Entity" (id)
);
CREATE TABLE "qo_Answer_prov_wasGeneratedBy" (
	"qo_Answer_id" INTEGER, 
	"prov_wasGeneratedBy_id" INTEGER, 
	PRIMARY KEY ("qo_Answer_id", "prov_wasGeneratedBy_id"), 
	FOREIGN KEY("qo_Answer_id") REFERENCES "qo_Answer" (id), 
	FOREIGN KEY("prov_wasGeneratedBy_id") REFERENCES "sulo_Process" (id)
);