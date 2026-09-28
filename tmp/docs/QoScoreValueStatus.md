
# Class: qo_ScoreValueStatus

Status of the score value, e.g., draft, final.

URI: [qo:QoScoreValueStatus](https://ns.faqir.org/q-o#QoScoreValueStatus)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimeInterval],[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoScoreValue]++-%20fhir_status%201..*>[QoScoreValueStatus&#124;saref_hasValue:qo_QuestionnaireStatusEnum;fhir_valueReference(i):uriorcurie%20%3F;fhir_valueAttachement(i):uriorcurie%20%3F;dcterms_created(i):datetime%20%3F;dcterms_modified(i):datetime%20%3F;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B;prov_type(i):uriorcurie%20*],[SarefPropertyValue]^-[QoScoreValueStatus],[QoScoreValue],[ProvEntity],[OwlThing],[FoafAgent],[FhirValueRatio],[FhirReferenceRange],[ValueCoding],[FlexibleDateTime])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimeInterval],[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoScoreValue]++-%20fhir_status%201..*>[QoScoreValueStatus&#124;saref_hasValue:qo_QuestionnaireStatusEnum;fhir_valueReference(i):uriorcurie%20%3F;fhir_valueAttachement(i):uriorcurie%20%3F;dcterms_created(i):datetime%20%3F;dcterms_modified(i):datetime%20%3F;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B;prov_type(i):uriorcurie%20*],[SarefPropertyValue]^-[QoScoreValueStatus],[QoScoreValue],[ProvEntity],[OwlThing],[FoafAgent],[FhirValueRatio],[FhirReferenceRange],[ValueCoding],[FlexibleDateTime])

## Parents

 *  is_a: [SarefPropertyValue](SarefPropertyValue.md) - Describes the value for a property. The property value is optionally linked to its value expressed as an RDF literal (DP saref:hasValue), optionally to the unit of measurement (OP saref:isMeasuredIn), and optionally to the properties or properties of interest it is a value of (OP saref:isValueOfProperty).

## Referenced by Class

 *  **[QoScoreValue](QoScoreValue.md)** *[qo_ScoreValue➞fhir_status](qo_ScoreValue_fhir_status.md)*  <sub>1..\*</sub>  **[QoScoreValueStatus](QoScoreValueStatus.md)**

## Attributes


### Own

 * [qo_ScoreValueStatus➞saref_hasValue](qo_ScoreValueStatus_saref_hasValue.md)  <sub>1..1</sub>
     * Description: The status of the score value, e.g., draft, final.
     * Range: [qo_QuestionnaireStatusEnum](qo_QuestionnaireStatusEnum.md)

### Inherited from saref_PropertyValue:

 * [owl_versionInfo](owl_versionInfo.md)  <sub>0..1</sub>
     * Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
     * Range: [String](types/String.md)
 * [rdfs_label](rdfs_label.md)  <sub>1..\*</sub>
     * Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
     * Range: [String](types/String.md)
 * [rdfs_comment](rdfs_comment.md)  <sub>1..\*</sub>
     * Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
     * Range: [String](types/String.md)
 * [prov_type](prov_type.md)  <sub>0..\*</sub>
     * Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [dcterms_hasPart](dcterms_hasPart.md)  <sub>0..\*</sub>
     * Description: A related resource that is included either physically or logically in the described resource.
     * Range: [OwlThing](OwlThing.md)
 * [dcterms_isPartOf](dcterms_isPartOf.md)  <sub>0..\*</sub>
     * Description: A related resource in which the described resource is physically or logically included.
     * Range: [OwlThing](OwlThing.md)
 * [prov_generatedAtTime](prov_generatedAtTime.md)  <sub>0..\*</sub>
     * Description: The time at which an entity was completely created and is available for use.
     * Range: [FlexibleDateTime](FlexibleDateTime.md)
 * [fhir_status](fhir_status.md)  <sub>0..\*</sub>
     * Description: A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)
 * [dcterms_creator](dcterms_creator.md)  <sub>0..\*</sub>
     * Description: An entity responsible for making the resource.
     * Range: [FoafAgent](FoafAgent.md)
 * [prov_hadPrimarySource](prov_hadPrimarySource.md)  <sub>0..\*</sub>
     * Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
     * Range: [ProvEntity](ProvEntity.md)
 * [prov_wasGeneratedBy](prov_wasGeneratedBy.md)  <sub>0..\*</sub>
     * Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
     * Range: [SuloProcess](SuloProcess.md)
 * [saref_hasProperty](saref_hasProperty.md)  <sub>0..\*</sub>
     * Description: Links a feature kind or a feature of interest to one of its properties.
     * Range: [SarefProperty](SarefProperty.md)
 * [saref_hasPropertyValue](saref_hasPropertyValue.md)  <sub>0..\*</sub>
     * Description: Links a feature kind, a feature of interest, or a property of interest, to a property value.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)
 * [prov_wasAttributedTo](prov_wasAttributedTo.md)  <sub>0..\*</sub>
     * Description: Attribution is the ascribing of an entity to an agent.
     * Range: [FoafAgent](FoafAgent.md)
 * [dcterms_created](dcterms_created.md)  <sub>0..1</sub>
     * Description: The date and time when the entity was created.
     * Range: [Datetime](types/Datetime.md)
 * [dcterms_modified](dcterms_modified.md)  <sub>0..1</sub>
     * Description: The date and time when the entity was last updated.
     * Range: [Datetime](types/Datetime.md)
 * [prov_atTime](prov_atTime.md)  <sub>0..1</sub>
     * Description: The time at which an InstantaneousEvent occurred.
     * Range: [FlexibleDateTime](FlexibleDateTime.md)
 * [saref_isValueOfProperty](saref_isValueOfProperty.md)  <sub>0..1</sub>
     * Description: Links a property value to the property or property of interest it is a value of.
     * Range: [SarefProperty](SarefProperty.md)
 * [fhir_valueReference](fhir_valueReference.md)  <sub>0..1</sub>
     * Description: The Reference type contains at least one of a reference (literal reference), an identifier (logical reference), and a display (text description of target). In addition, it may contain a target type.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞fhir_valueCodeableConcept](sarefPropertyValue__fhir_valueCodeableConcept.md)  <sub>0..1</sub>
     * Description: A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies but may also be defined by the provision of text. This is a common pattern in healthcare data.
     * Range: [ValueCoding](ValueCoding.md)
 * [➞fhir_valueRange](sarefPropertyValue__fhir_valueRange.md)  <sub>0..1</sub>
     * Description: A set of ordered Quantity values defined by a low and high limit.
     * Range: [FhirReferenceRange](FhirReferenceRange.md)
 * [➞fhir_valueRatio](sarefPropertyValue__fhir_valueRatio.md)  <sub>0..1</sub>
     * Description: A relationship between two Quantity values expressed as a numerator and a denominator. The Ratio datatype should only be used to express a relationship of two numbers if the relationship cannot be suitably expressed using a Quantity and a common unit. Where the denominator value is known to be fixed to '1', Quantity should be used instead of Ratio.
     * Range: [FhirValueRatio](FhirValueRatio.md)
 * [➞fhir_valuePeriod](sarefPropertyValue__fhir_valuePeriod.md)  <sub>0..1</sub>
     * Description: A time period defined by a start and end date/time. A period specifies a range of times. The context of use will specify whether the entire range applies (e.g. 'the patient was an inpatient of the hospital for this time range') or one value from the period applies (e.g. 'give to the patient between 2 and 4 pm on 24-Jun 2013').
     * Range: [TimeInterval](TimeInterval.md)
 * [➞fhir_valueAttachement](sarefPropertyValue__fhir_valueAttachement.md)  <sub>0..1</sub>
     * Description: This type is for containing or referencing attachments - additional data content defined in other formats. The most common use of this type is to include images or reports in some report format such as PDF. However, it can be used for any data that has a MIME type.
     * Range: [Uriorcurie](types/Uriorcurie.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | qo:ScoreValueStatus |