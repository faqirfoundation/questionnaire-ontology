# Questionnaire Ontology

FAQIR Questionnaire Ontology

URI: https://ns.faqir.org/q-o

Name: Questionnaire-Ontology



## Classes

| Class | Description |
| --- | --- |
| [FhirReferenceRange](FhirReferenceRange.md) | Guidance on how to interpret the value by comparison to a normal or recommend... |
| [FhirValueRatio](FhirValueRatio.md) | A ratio of two Quantity values - a numerator and a denominator |
| [IntervalParams](IntervalParams.md) | Parameters for interval values, including minimum and maximum values |
| [NumericalParams](NumericalParams.md) | Parameters for quantitative values, including unit and precision |
| [OwlThing](OwlThing.md) | This defines IOT as the set of OWL individuals |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FoafAgent](FoafAgent.md) | An agent (eg |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FoafPerson](FoafPerson.md) | A person |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProvOrganization](ProvOrganization.md) | An organization is a social or legal institution such as a company, society, ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProvEntity](ProvEntity.md) | An entity is a physical, digital, conceptual, or other kind of thing with som... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoOrderedQuestion](QoOrderedQuestion.md) | A contextual wrapper that binds an inquiry item to a specific sequence index ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoOrderedSection](QoOrderedSection.md) | A contextual wrapper that binds a thematic grouping of inquiry items to a spe... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoQuestion](QoQuestion.md) | An individual inquiry item within an instrument that specifies an information... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoQuestionnaire](QoQuestionnaire.md) | A structured, reusable instrument or template composed of ordered items desig... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoQuestionnaireResponse](QoQuestionnaireResponse.md) | A completed or partially completed instance containing recorded values collec... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoSection](QoSection.md) | A logical grouping or thematic partition of items within a structured survey ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SarefProperty](SarefProperty.md) | Identifiable qualities of features of interest that can be target of devices,... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SarefPropertyValue](SarefPropertyValue.md) | Describes the value for a property |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QoQuestionnaireStatus](QoQuestionnaireStatus.md) | Defines the lifecycle state governing the operational readiness and availabil... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SuloProcess](SuloProcess.md) | a process is a entity that unfolds in time, has temporal parts, and has objec... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FhirProcedure](FhirProcedure.md) | An action that is being or was performed on an individual or entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[S4ehawActivity](S4ehawActivity.md) | The activity of a patient/user, i |
| [ProvAttribution](ProvAttribution.md) | An instance of prov:Attribution provides additional descriptions about the bi... |
| [QuantityValue](QuantityValue.md) | A measured amount (or an amount that can potentially be measured) |
| [TimeDuration](TimeDuration.md) | Duration of a temporal extent expressed as a decimal number scaled by a tempo... |
| [TimeInterval](TimeInterval.md) | A temporal entity with an extent or duration |
| [ValueCoding](ValueCoding.md) | A coded value with a unique code for each display text, typically used for st... |



## Slots

| Slot | Description |
| --- | --- |
| [code](code.md) | The code representing the value (e |
| [dcterms_created](dcterms_created.md) | The date and time when the entity was created |
| [dcterms_creator](dcterms_creator.md) | An entity responsible for making the resource |
| [dcterms_hasPart](dcterms_hasPart.md) | A related resource that is included either physically or logically in the des... |
| [dcterms_isPartOf](dcterms_isPartOf.md) | A related resource in which the described resource is physically or logically... |
| [dcterms_modified](dcterms_modified.md) | The date and time when the entity was last updated |
| [denominator](denominator.md) |  |
| [display](display.md) | The human-readable display text for the code (e |
| [fhir_referenceRange](fhir_referenceRange.md) | Guidance on how to interpret the value by comparison to a normal or recommend... |
| [fhir_status](fhir_status.md) | A code specifying the state of the observation/procedure/questionnaire |
| [fhir_valueAttachment](fhir_valueAttachment.md) | This type is for containing or referencing attachments - additional data cont... |
| [fhir_valueCodeableConcept](fhir_valueCodeableConcept.md) | A CodeableConcept represents a value that is usually supplied by providing a ... |
| [fhir_valuePeriod](fhir_valuePeriod.md) | A time period defined by a start and end date/time |
| [fhir_valueRange](fhir_valueRange.md) | A set of ordered Quantity values defined by a low and high limit |
| [fhir_valueRatio](fhir_valueRatio.md) | A relationship between two Quantity values expressed as a numerator and a den... |
| [fhir_valueReference](fhir_valueReference.md) | The Reference type contains at least one of a reference (literal reference), ... |
| [highRange](highRange.md) | High range, if relevant |
| [lowRange](lowRange.md) | Low range, if relevant |
| [maxLabel](maxLabel.md) | The label for the maximum value of the interval |
| [maxValue](maxValue.md) | The maximum value of the interval |
| [minLabel](minLabel.md) | The label for the minimum value of the interval |
| [minValue](minValue.md) | The minimum value of the interval |
| [normalValue](normalValue.md) | Normal value, if relevant |
| [numerator](numerator.md) |  |
| [numericalPrecision](numericalPrecision.md) | The precision of the quantitative value, e |
| [numericalUnit](numericalUnit.md) | The unit of measure for the quantitative value, from UCUM standard |
| [owl_versionInfo](owl_versionInfo.md) | An owl:versionInfo statement generally has as its object a string giving info... |
| [prov_atTime](prov_atTime.md) | The time at which an InstantaneousEvent occurred |
| [prov_endedAtTime](prov_endedAtTime.md) | The time at which an activity ended |
| [prov_generated](prov_generated.md) | Generation is the completion of production of a new entity by an activity |
| [prov_generatedAtTime](prov_generatedAtTime.md) | The time at which an entity was completely created and is available for use |
| [prov_hadPrimarySource](prov_hadPrimarySource.md) | A primary source for a topic refers to something produced by some agent with ... |
| [prov_qualifiedAttribution](prov_qualifiedAttribution.md) | Attribution is the ascribing of an entity to an agent |
| [prov_startedAtTime](prov_startedAtTime.md) | The time at which an activity started |
| [prov_type](prov_type.md) | The attribute prov:type provides further typing information for any construct... |
| [prov_wasAttributedTo](prov_wasAttributedTo.md) | Attribution is the ascribing of an entity to an agent |
| [prov_wasGeneratedBy](prov_wasGeneratedBy.md) | Generation is the completion of production of a new entity by an activity |
| [qo_answerValue](qo_answerValue.md) | The recorded literal payload (numeric scalar, textual/coded string, or timest... |
| [qo_codingOrdinal](qo_codingOrdinal.md) | Specifies whether permissible selection options possess a meaningful inherent... |
| [qo_codingParams](qo_codingParams.md) | Defines the permissible standardized concept codes and human-readable labels ... |
| [qo_conditionalValidity](qo_conditionalValidity.md) | A machine-readable rule statement defining an intervening event or state chan... |
| [qo_hardValidity](qo_hardValidity.md) | Specifies the operational enforcement mechanism of a duration limit; when tru... |
| [qo_hasAnswer](qo_hasAnswer.md) | Associates a recorded instance with its constituent individual response value... |
| [qo_hasOrderedQuestion](qo_hasOrderedQuestion.md) | Associates a survey container or group with a sequence-indexed wrapper holdin... |
| [qo_hasOrderedSection](qo_hasOrderedSection.md) | Associates a survey container or group with a sequence-indexed wrapper holdin... |
| [qo_intervalParams](qo_intervalParams.md) | Defines lower and upper boundary limits bounding acceptable numeric values |
| [qo_isEmpty](qo_isEmpty.md) | Specifies an explicit assertion that an item was purposefully omitted or unpo... |
| [qo_multivalued](qo_multivalued.md) | Indicates whether this question allows more than one answer (true) or only on... |
| [qo_numericalParams](qo_numericalParams.md) | Specifies measurement units and decimal precision constraints governing accep... |
| [qo_order](qo_order.md) | An integer specifying the sequence or display arrangement (1-based index) of ... |
| [qo_question](qo_question.md) | Identifies the specific inquiry item referenced at a given positional index |
| [qo_required](qo_required.md) | Whether the question can be left un-answered (false) or an answer is mandator... |
| [qo_responds](qo_responds.md) | Links a record instance back to the underlying survey template it answers |
| [qo_section](qo_section.md) | Identifies the specific thematic grouping referenced at a given positional in... |
| [qo_tag](qo_tag.md) | A machine-readable alphanumeric code or mnemonic string used for internal ref... |
| [qo_temporalValidity](qo_temporalValidity.md) | Defines the time extent following generation during which a recorded answer r... |
| [qo_toQuestion](qo_toQuestion.md) | Links a recorded response value back to its originating inquiry item definiti... |
| [rdfs_comment](rdfs_comment.md) | A textual comment helps clarify the meaning of RDF classes and properties |
| [rdfs_label](rdfs_label.md) | human-readable version of a resource's name |
| [s4ehaw_maximumValue](s4ehaw_maximumValue.md) | The maximum allowable value of a measurement |
| [s4ehaw_minimumValue](s4ehaw_minimumValue.md) | The minimum allowable value of a measurement |
| [saref_hasProperty](saref_hasProperty.md) | Links a feature kind or a feature of interest to one of its properties |
| [saref_hasPropertyValue](saref_hasPropertyValue.md) | Links a feature kind, a feature of interest, or a property of interest, to a ... |
| [saref_hasValue](saref_hasValue.md) | Value of a property value expressed as an RDF literal |
| [saref_isMeasuredIn](saref_isMeasuredIn.md) | A relationship identifying the unit of measure used for a certain entity |
| [saref_isValueOfProperty](saref_isValueOfProperty.md) | Links a property value to the property or property of interest it is a value ... |
| [time_hasDuration](time_hasDuration.md) | Duration of a temporal entity, expressed as a scaled value or nominal value |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [QoQuestionnaireResponseStatusEnum](QoQuestionnaireResponseStatusEnum.md) | The questionnaire response status must be one of the following: 'in-progress'... |
| [QoQuestionnaireStatusEnum](QoQuestionnaireStatusEnum.md) | Questionnaires must have one of the following status (FHIR inspired):  |
| [QoQuestionType](QoQuestionType.md) | Specifies the structural classification and data-type constraints governing a... |


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
