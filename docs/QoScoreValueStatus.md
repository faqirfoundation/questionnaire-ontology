

# Class: QoScoreValueStatus 


_Status of the score value, e.g., draft, final._





URI: [qo:ScoreValueStatus](https://ns.faqir.org/q-o#ScoreValueStatus)






```mermaid
 classDiagram
    class QoScoreValueStatus
    click QoScoreValueStatus href "../QoScoreValueStatus"
      SarefPropertyValue <|-- QoScoreValueStatus
        click SarefPropertyValue href "../SarefPropertyValue"
      
      QoScoreValueStatus : dcterms_created
        
      QoScoreValueStatus : dcterms_creator
        
          
    
        
        
        QoScoreValueStatus --> "*" FoafAgent : dcterms_creator
        click FoafAgent href "../FoafAgent"
    

        
      QoScoreValueStatus : dcterms_hasPart
        
          
    
        
        
        QoScoreValueStatus --> "*" OwlThing : dcterms_hasPart
        click OwlThing href "../OwlThing"
    

        
      QoScoreValueStatus : dcterms_isPartOf
        
          
    
        
        
        QoScoreValueStatus --> "*" OwlThing : dcterms_isPartOf
        click OwlThing href "../OwlThing"
    

        
      QoScoreValueStatus : dcterms_modified
        
      QoScoreValueStatus : fhir_status
        
          
    
        
        
        QoScoreValueStatus --> "*" SarefPropertyValue : fhir_status
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      QoScoreValueStatus : fhir_valueAttachement
        
      QoScoreValueStatus : fhir_valueCodeableConcept
        
          
    
        
        
        QoScoreValueStatus --> "0..1" ValueCoding : fhir_valueCodeableConcept
        click ValueCoding href "../ValueCoding"
    

        
      QoScoreValueStatus : fhir_valuePeriod
        
          
    
        
        
        QoScoreValueStatus --> "0..1" TimeInterval : fhir_valuePeriod
        click TimeInterval href "../TimeInterval"
    

        
      QoScoreValueStatus : fhir_valueRange
        
          
    
        
        
        QoScoreValueStatus --> "0..1" FhirReferenceRange : fhir_valueRange
        click FhirReferenceRange href "../FhirReferenceRange"
    

        
      QoScoreValueStatus : fhir_valueRatio
        
          
    
        
        
        QoScoreValueStatus --> "0..1" FhirValueRatio : fhir_valueRatio
        click FhirValueRatio href "../FhirValueRatio"
    

        
      QoScoreValueStatus : fhir_valueReference
        
      QoScoreValueStatus : owl_versionInfo
        
      QoScoreValueStatus : prov_atTime
        
          
    
        
        
        QoScoreValueStatus --> "0..1" FlexibleDateTime : prov_atTime
        click FlexibleDateTime href "../FlexibleDateTime"
    

        
      QoScoreValueStatus : prov_generatedAtTime
        
          
    
        
        
        QoScoreValueStatus --> "*" FlexibleDateTime : prov_generatedAtTime
        click FlexibleDateTime href "../FlexibleDateTime"
    

        
      QoScoreValueStatus : prov_hadPrimarySource
        
          
    
        
        
        QoScoreValueStatus --> "*" ProvEntity : prov_hadPrimarySource
        click ProvEntity href "../ProvEntity"
    

        
      QoScoreValueStatus : prov_type
        
      QoScoreValueStatus : prov_wasAttributedTo
        
          
    
        
        
        QoScoreValueStatus --> "*" FoafAgent : prov_wasAttributedTo
        click FoafAgent href "../FoafAgent"
    

        
      QoScoreValueStatus : prov_wasGeneratedBy
        
          
    
        
        
        QoScoreValueStatus --> "*" SuloProcess : prov_wasGeneratedBy
        click SuloProcess href "../SuloProcess"
    

        
      QoScoreValueStatus : rdfs_comment
        
      QoScoreValueStatus : rdfs_label
        
      QoScoreValueStatus : saref_hasProperty
        
          
    
        
        
        QoScoreValueStatus --> "*" SarefProperty : saref_hasProperty
        click SarefProperty href "../SarefProperty"
    

        
      QoScoreValueStatus : saref_hasPropertyValue
        
          
    
        
        
        QoScoreValueStatus --> "*" SarefPropertyValue : saref_hasPropertyValue
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      QoScoreValueStatus : saref_hasValue
        
          
    
        
        
        QoScoreValueStatus --> "1" QoQuestionnaireStatusEnum : saref_hasValue
        click QoQuestionnaireStatusEnum href "../QoQuestionnaireStatusEnum"
    

        
      QoScoreValueStatus : saref_isValueOfProperty
        
          
    
        
        
        QoScoreValueStatus --> "0..1" SarefProperty : saref_isValueOfProperty
        click SarefProperty href "../SarefProperty"
    

        
      
```





## Inheritance
* [OwlThing](OwlThing.md)
    * [ProvEntity](ProvEntity.md)
        * [SarefPropertyValue](SarefPropertyValue.md)
            * **QoScoreValueStatus**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [prov_atTime](prov_atTime.md) | 0..1 <br/> [FlexibleDateTime](FlexibleDateTime.md) | The time at which an InstantaneousEvent occurred | [SarefPropertyValue](SarefPropertyValue.md) |
| [saref_hasValue](saref_hasValue.md) | 1 <br/> [QoQuestionnaireStatusEnum](QoQuestionnaireStatusEnum.md) | The status of the score value, e | [SarefPropertyValue](SarefPropertyValue.md) |
| [saref_isValueOfProperty](saref_isValueOfProperty.md) | 0..1 <br/> [SarefProperty](SarefProperty.md) | Links a property value to the property or property of interest it is a value ... | [SarefPropertyValue](SarefPropertyValue.md) |
| [fhir_valueReference](fhir_valueReference.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The Reference type contains at least one of a reference (literal reference), ... | [SarefPropertyValue](SarefPropertyValue.md) |
| [fhir_valueCodeableConcept](fhir_valueCodeableConcept.md) | 0..1 <br/> [ValueCoding](ValueCoding.md) | A CodeableConcept represents a value that is usually supplied by providing a ... | [SarefPropertyValue](SarefPropertyValue.md) |
| [fhir_valueRange](fhir_valueRange.md) | 0..1 <br/> [FhirReferenceRange](FhirReferenceRange.md) | A set of ordered Quantity values defined by a low and high limit | [SarefPropertyValue](SarefPropertyValue.md) |
| [fhir_valueRatio](fhir_valueRatio.md) | 0..1 <br/> [FhirValueRatio](FhirValueRatio.md) | A relationship between two Quantity values expressed as a numerator and a den... | [SarefPropertyValue](SarefPropertyValue.md) |
| [fhir_valuePeriod](fhir_valuePeriod.md) | 0..1 <br/> [TimeInterval](TimeInterval.md) | A time period defined by a start and end date/time | [SarefPropertyValue](SarefPropertyValue.md) |
| [fhir_valueAttachement](fhir_valueAttachement.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | This type is for containing or referencing attachments - additional data cont... | [SarefPropertyValue](SarefPropertyValue.md) |
| [prov_wasAttributedTo](prov_wasAttributedTo.md) | * <br/> [FoafAgent](FoafAgent.md) | Attribution is the ascribing of an entity to an agent | [ProvEntity](ProvEntity.md) |
| [dcterms_created](dcterms_created.md) | 0..1 <br/> [datetime](datetime.md) | The date and time when the entity was created | [ProvEntity](ProvEntity.md) |
| [dcterms_modified](dcterms_modified.md) | 0..1 <br/> [datetime](datetime.md) | The date and time when the entity was last updated | [ProvEntity](ProvEntity.md) |
| [owl_versionInfo](owl_versionInfo.md) | 0..1 <br/> [String](String.md) | An owl:versionInfo statement generally has as its object a string giving info... | [OwlThing](OwlThing.md) |
| [rdfs_label](rdfs_label.md) | 1..* <br/> [String](String.md) | human-readable version of a resource's name | [OwlThing](OwlThing.md) |
| [rdfs_comment](rdfs_comment.md) | 1..* <br/> [String](String.md) | A textual comment helps clarify the meaning of RDF classes and properties | [OwlThing](OwlThing.md) |
| [prov_type](prov_type.md) | * <br/> [Uriorcurie](Uriorcurie.md) | The attribute prov:type provides further typing information for any construct... | [OwlThing](OwlThing.md) |
| [dcterms_hasPart](dcterms_hasPart.md) | * <br/> [OwlThing](OwlThing.md) | A related resource that is included either physically or logically in the des... | [OwlThing](OwlThing.md) |
| [dcterms_isPartOf](dcterms_isPartOf.md) | * <br/> [OwlThing](OwlThing.md) | A related resource in which the described resource is physically or logically... | [OwlThing](OwlThing.md) |
| [prov_generatedAtTime](prov_generatedAtTime.md) | * <br/> [FlexibleDateTime](FlexibleDateTime.md) | The time at which an entity was completely created and is available for use | [OwlThing](OwlThing.md) |
| [fhir_status](fhir_status.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | A code specifying the state of the observation/procedure/questionnaire | [OwlThing](OwlThing.md) |
| [dcterms_creator](dcterms_creator.md) | * <br/> [FoafAgent](FoafAgent.md) | An entity responsible for making the resource | [OwlThing](OwlThing.md) |
| [prov_hadPrimarySource](prov_hadPrimarySource.md) | * <br/> [ProvEntity](ProvEntity.md) | A primary source for a topic refers to something produced by some agent with ... | [OwlThing](OwlThing.md) |
| [prov_wasGeneratedBy](prov_wasGeneratedBy.md) | * <br/> [SuloProcess](SuloProcess.md) | Generation is the completion of production of a new entity by an activity | [OwlThing](OwlThing.md) |
| [saref_hasProperty](saref_hasProperty.md) | * <br/> [SarefProperty](SarefProperty.md) | Links a feature kind or a feature of interest to one of its properties | [OwlThing](OwlThing.md) |
| [saref_hasPropertyValue](saref_hasPropertyValue.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | Links a feature kind, a feature of interest, or a property of interest, to a ... | [OwlThing](OwlThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoScoreValue](QoScoreValue.md) | [fhir_status](fhir_status.md) | range | [QoScoreValueStatus](QoScoreValueStatus.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:ScoreValueStatus |
| native | qo:QoScoreValueStatus |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: qo_ScoreValueStatus
description: Status of the score value, e.g., draft, final.
from_schema: https://ns.faqir.org/q-o
is_a: saref_PropertyValue
slot_usage:
  saref_hasValue:
    name: saref_hasValue
    description: The status of the score value, e.g., draft, final.
    range: qo_QuestionnaireStatusEnum
    required: true
    multivalued: false
    inlined: false
class_uri: qo:ScoreValueStatus

```
</details>

### Induced

<details>
```yaml
name: qo_ScoreValueStatus
description: Status of the score value, e.g., draft, final.
from_schema: https://ns.faqir.org/q-o
is_a: saref_PropertyValue
slot_usage:
  saref_hasValue:
    name: saref_hasValue
    description: The status of the score value, e.g., draft, final.
    range: qo_QuestionnaireStatusEnum
    required: true
    multivalued: false
    inlined: false
attributes:
  prov_atTime:
    name: prov_atTime
    description: The time at which an InstantaneousEvent occurred.
    from_schema: https://ns.faqir.org/q-o
    mappings:
    - saref:hasTimestamp
    - fhir:DeviceMetric.calibration.time
    - sosa:phenomenonTime
    rank: 1000
    domain: sulo_Process
    slot_uri: prov:atTime
    alias: prov_atTime
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: FlexibleDateTime
    required: false
    multivalued: false
  saref_hasValue:
    name: saref_hasValue
    description: The status of the score value, e.g., draft, final.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: saref:hasValue
    alias: saref_hasValue
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    - QuantityValue
    - time_Duration
    range: qo_QuestionnaireStatusEnum
    required: true
    multivalued: false
    inlined: false
  saref_isValueOfProperty:
    name: saref_isValueOfProperty
    description: Links a property value to the property or property of interest it
      is a value of.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: saref_PropertyValue
    slot_uri: saref:isValueOfProperty
    alias: saref_isValueOfProperty
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: saref_Property
    required: false
    multivalued: false
  fhir_valueReference:
    name: fhir_valueReference
    description: The Reference type contains at least one of a reference (literal
      reference), an identifier (logical reference), and a display (text description
      of target). In addition, it may contain a target type.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: fhir:valueReference
    alias: fhir_valueReference
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: uriorcurie
    required: false
    multivalued: false
  fhir_valueCodeableConcept:
    name: fhir_valueCodeableConcept
    description: A CodeableConcept represents a value that is usually supplied by
      providing a reference to one or more terminologies or ontologies but may also
      be defined by the provision of text. This is a common pattern in healthcare
      data.
    from_schema: https://ns.faqir.org/phr-o/featureOfInterest
    rank: 1000
    slot_uri: fhir:valueCodeableConcept
    alias: fhir_valueCodeableConcept
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: ValueCoding
    required: false
    multivalued: false
  fhir_valueRange:
    name: fhir_valueRange
    description: A set of ordered Quantity values defined by a low and high limit.
    from_schema: https://ns.faqir.org/phr-o/featureOfInterest
    rank: 1000
    slot_uri: fhir:valueRange
    alias: fhir_valueRange
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: fhir_ReferenceRange
    required: false
    multivalued: false
  fhir_valueRatio:
    name: fhir_valueRatio
    description: A relationship between two Quantity values expressed as a numerator
      and a denominator. The Ratio datatype should only be used to express a relationship
      of two numbers if the relationship cannot be suitably expressed using a Quantity
      and a common unit. Where the denominator value is known to be fixed to '1',
      Quantity should be used instead of Ratio.
    from_schema: https://ns.faqir.org/phr-o/featureOfInterest
    rank: 1000
    slot_uri: fhir:valueRatio
    alias: fhir_valueRatio
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: fhir_ValueRatio
    required: false
    multivalued: false
  fhir_valuePeriod:
    name: fhir_valuePeriod
    description: A time period defined by a start and end date/time. A period specifies
      a range of times. The context of use will specify whether the entire range applies
      (e.g. 'the patient was an inpatient of the hospital for this time range') or
      one value from the period applies (e.g. 'give to the patient between 2 and 4
      pm on 24-Jun 2013').
    from_schema: https://ns.faqir.org/phr-o/featureOfInterest
    rank: 1000
    slot_uri: fhir:valuePeriod
    alias: fhir_valuePeriod
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: time_Interval
    required: false
    multivalued: false
  fhir_valueAttachement:
    name: fhir_valueAttachement
    description: This type is for containing or referencing attachments - additional
      data content defined in other formats. The most common use of this type is to
      include images or reports in some report format such as PDF. However, it can
      be used for any data that has a MIME type.
    from_schema: https://ns.faqir.org/phr-o/featureOfInterest
    rank: 1000
    slot_uri: fhir:valueAttachement
    alias: fhir_valueAttachement
    owner: qo_ScoreValueStatus
    domain_of:
    - saref_PropertyValue
    range: uriorcurie
    required: false
    multivalued: false
  prov_wasAttributedTo:
    name: prov_wasAttributedTo
    description: Attribution is the ascribing of an entity to an agent.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: prov_Entity
    slot_uri: prov:wasAttributedTo
    alias: prov_wasAttributedTo
    owner: qo_ScoreValueStatus
    domain_of:
    - prov_Entity
    range: foaf_Agent
    required: false
    multivalued: true
  dcterms_created:
    name: dcterms_created
    description: The date and time when the entity was created.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:created
    alias: dcterms_created
    owner: qo_ScoreValueStatus
    domain_of:
    - prov_Entity
    range: datetime
    required: false
  dcterms_modified:
    name: dcterms_modified
    description: The date and time when the entity was last updated.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:modified
    alias: dcterms_modified
    owner: qo_ScoreValueStatus
    domain_of:
    - prov_Entity
    range: datetime
    required: false
  owl_versionInfo:
    name: owl_versionInfo
    description: An owl:versionInfo statement generally has as its object a string
      giving information about this version, for example RCS/CVS keywords. This statement
      does not contribute to the logical meaning of the ontology other than that given
      by the RDF(S) model theory.
    from_schema: https://ns.faqir.org/q-o
    close_mappings:
    - saref:hasVersion
    rank: 1000
    domain: owl_Thing
    slot_uri: owl:versionInfo
    alias: owl_versionInfo
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: string
    required: false
    multivalued: false
  rdfs_label:
    name: rdfs_label
    description: human-readable version of a resource's name. Multilingual labels
      are supported using the language tagging facility of RDF literals.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: rdfs:label
    alias: rdfs_label
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: string
    required: true
    multivalued: true
  rdfs_comment:
    name: rdfs_comment
    description: A textual comment helps clarify the meaning of RDF classes and properties.
      Such in-line documentation complements the use of both formal techniques (Ontology
      and rule languages) and informal (prose documentation, examples, test cases).
      A variety of documentation forms can be combined to indicate the intended meaning
      of the classes and properties described in an RDF vocabulary. Since RDF vocabularies
      are expressed as RDF graphs, vocabularies defined in other namespaces may be
      used to provide richer documentation.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: rdfs:comment
    alias: rdfs_comment
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: string
    required: true
    multivalued: true
  prov_type:
    name: prov_type
    description: The attribute prov:type provides further typing information for any
      construct with an optional set of attribute-value pairs.
    from_schema: https://ns.faqir.org/q-o
    exact_mappings:
    - rdf:type
    - sphn:hasTypeCode
    narrow_mappings:
    - schema:procedureType
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:type
    alias: prov_type
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    - sphn_TimePattern
    range: uriorcurie
    required: false
    multivalued: true
  dcterms_hasPart:
    name: dcterms_hasPart
    description: A related resource that is included either physically or logically
      in the described resource.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: dcterms:hasPart
    alias: dcterms_hasPart
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    inverse: dcterms_isPartOf
    range: owl_Thing
    required: false
    multivalued: true
  dcterms_isPartOf:
    name: dcterms_isPartOf
    description: A related resource in which the described resource is physically
      or logically included.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: dcterms:isPartOf
    alias: dcterms_isPartOf
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    inverse: dcterms_hasPart
    range: owl_Thing
    required: false
    multivalued: true
  prov_generatedAtTime:
    name: prov_generatedAtTime
    description: The time at which an entity was completely created and is available
      for use.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:generatedAtTime
    alias: prov_generatedAtTime
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: FlexibleDateTime
    required: false
    multivalued: true
  fhir_status:
    name: fhir_status
    description: A code specifying the state of the observation/procedure/questionnaire...
      Generally, this will be the in-progress or completed state.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    is_a: saref_hasPropertyValue
    domain: owl_Thing
    slot_uri: fhir:resource-status
    alias: fhir_status
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: saref_PropertyValue
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  dcterms_creator:
    name: dcterms_creator
    description: An entity responsible for making the resource.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: dcterms:creator
    alias: dcterms_creator
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: foaf_Agent
    required: false
    multivalued: true
  prov_hadPrimarySource:
    name: prov_hadPrimarySource
    description: A primary source for a topic refers to something produced by some
      agent with direct experience and knowledge about the topic, at the time of the
      topic's study, without benefit from hindsight. Because of the directness of
      primary sources, they 'speak for themselves' in ways that cannot be captured
      through the filter of secondary sources. As such, it is important for secondary
      sources to reference those primary sources from which they were derived, so
      that their reliability can be investigated. A primary source relation is a particular
      case of derivation of secondary materials from their primary sources. It is
      recognized that the determination of primary sources can be up to interpretation,
      and should be done according to conventions accepted within the application's
      domain.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:hadPrimarySource
    alias: prov_hadPrimarySource
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: prov_Entity
    required: false
    multivalued: true
  prov_wasGeneratedBy:
    name: prov_wasGeneratedBy
    description: Generation is the completion of production of a new entity by an
      activity. This entity did not exist before generation and becomes available
      for usage after this generation.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:wasGeneratedBy
    alias: prov_wasGeneratedBy
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: sulo_Process
    required: false
    multivalued: true
  saref_hasProperty:
    name: saref_hasProperty
    description: Links a feature kind or a feature of interest to one of its properties.
    from_schema: https://ns.faqir.org/q-o
    mappings:
    - ssn:hasProperty
    rank: 1000
    domain: owl_Thing
    slot_uri: saref:hasProperty
    alias: saref_hasProperty
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: saref_Property
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  saref_hasPropertyValue:
    name: saref_hasPropertyValue
    description: Links a feature kind, a feature of interest, or a property of interest,
      to a property value.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: saref:hasPropertyValue
    alias: saref_hasPropertyValue
    owner: qo_ScoreValueStatus
    domain_of:
    - owl_Thing
    range: saref_PropertyValue
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
class_uri: qo:ScoreValueStatus

```
</details>