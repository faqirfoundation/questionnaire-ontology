

# Class: QoOrderedSection 


_A contextual wrapper that binds a thematic grouping of inquiry items to a specific sequence index within a survey template or parent group._





URI: [qo:OrderedSection](https://ns.faqir.org/q-o#OrderedSection)






```mermaid
 classDiagram
    class QoOrderedSection
    click QoOrderedSection href "../QoOrderedSection"
      ProvEntity <|-- QoOrderedSection
        click ProvEntity href "../ProvEntity"
      
      QoOrderedSection : dcterms_created
        
      QoOrderedSection : dcterms_creator
        
          
    
        
        
        QoOrderedSection --> "*" FoafAgent : dcterms_creator
        click FoafAgent href "../FoafAgent"
    

        
      QoOrderedSection : dcterms_hasPart
        
          
    
        
        
        QoOrderedSection --> "*" OwlThing : dcterms_hasPart
        click OwlThing href "../OwlThing"
    

        
      QoOrderedSection : dcterms_isPartOf
        
          
    
        
        
        QoOrderedSection --> "*" OwlThing : dcterms_isPartOf
        click OwlThing href "../OwlThing"
    

        
      QoOrderedSection : dcterms_modified
        
      QoOrderedSection : fhir_status
        
          
    
        
        
        QoOrderedSection --> "*" SarefPropertyValue : fhir_status
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      QoOrderedSection : owl_versionInfo
        
      QoOrderedSection : prov_generatedAtTime
        
      QoOrderedSection : prov_hadPrimarySource
        
          
    
        
        
        QoOrderedSection --> "*" ProvEntity : prov_hadPrimarySource
        click ProvEntity href "../ProvEntity"
    

        
      QoOrderedSection : prov_type
        
      QoOrderedSection : prov_wasAttributedTo
        
          
    
        
        
        QoOrderedSection --> "*" FoafAgent : prov_wasAttributedTo
        click FoafAgent href "../FoafAgent"
    

        
      QoOrderedSection : prov_wasGeneratedBy
        
          
    
        
        
        QoOrderedSection --> "*" SuloProcess : prov_wasGeneratedBy
        click SuloProcess href "../SuloProcess"
    

        
      QoOrderedSection : qo_conditionalValidity
        
      QoOrderedSection : qo_hardValidity
        
      QoOrderedSection : qo_order
        
      QoOrderedSection : qo_section
        
          
    
        
        
        QoOrderedSection --> "1..*" QoSection : qo_section
        click QoSection href "../QoSection"
    

        
      QoOrderedSection : qo_temporalValidity
        
          
    
        
        
        QoOrderedSection --> "1" TimeDuration : qo_temporalValidity
        click TimeDuration href "../TimeDuration"
    

        
      QoOrderedSection : rdfs_comment
        
      QoOrderedSection : rdfs_label
        
      QoOrderedSection : saref_hasProperty
        
          
    
        
        
        QoOrderedSection --> "*" SarefProperty : saref_hasProperty
        click SarefProperty href "../SarefProperty"
    

        
      QoOrderedSection : saref_hasPropertyValue
        
          
    
        
        
        QoOrderedSection --> "*" SarefPropertyValue : saref_hasPropertyValue
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      
```





## Inheritance
* [OwlThing](OwlThing.md)
    * [ProvEntity](ProvEntity.md)
        * **QoOrderedSection**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [qo_section](qo_section.md) | 1..* <br/> [QoSection](QoSection.md) | Identifies the specific thematic grouping referenced at a given positional in... | direct |
| [qo_order](qo_order.md) | 1 <br/> [Integer](Integer.md) | Section position in the questionnaire or section (1-based index) | direct |
| [qo_hardValidity](qo_hardValidity.md) | 0..1 <br/> [Boolean](Boolean.md) | Specifies the operational enforcement mechanism of a duration limit; when tru... | direct |
| [qo_temporalValidity](qo_temporalValidity.md) | 1 <br/> [TimeDuration](TimeDuration.md) | Defines the time extent following generation during which a recorded answer r... | direct |
| [qo_conditionalValidity](qo_conditionalValidity.md) | 0..1 <br/> [String](String.md) | A machine-readable rule statement defining an intervening event or state chan... | direct |
| [prov_wasAttributedTo](prov_wasAttributedTo.md) | * <br/> [FoafAgent](FoafAgent.md) | Attribution is the ascribing of an entity to an agent | [ProvEntity](ProvEntity.md) |
| [dcterms_created](dcterms_created.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the entity was created | [ProvEntity](ProvEntity.md) |
| [dcterms_modified](dcterms_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the entity was last updated | [ProvEntity](ProvEntity.md) |
| [prov_type](prov_type.md) | * <br/> [Uriorcurie](Uriorcurie.md) | The attribute prov:type provides further typing information for any construct... | [ProvEntity](ProvEntity.md) |
| [dcterms_hasPart](dcterms_hasPart.md) | * <br/> [OwlThing](OwlThing.md) | A related resource that is included either physically or logically in the des... | [ProvEntity](ProvEntity.md) |
| [dcterms_isPartOf](dcterms_isPartOf.md) | * <br/> [OwlThing](OwlThing.md) | A related resource in which the described resource is physically or logically... | [ProvEntity](ProvEntity.md) |
| [prov_generatedAtTime](prov_generatedAtTime.md) | * <br/> [Datetime](Datetime.md) | The time at which an entity was completely created and is available for use | [ProvEntity](ProvEntity.md) |
| [fhir_status](fhir_status.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | A code specifying the state of the observation/procedure/questionnaire | [ProvEntity](ProvEntity.md) |
| [dcterms_creator](dcterms_creator.md) | * <br/> [FoafAgent](FoafAgent.md) | An entity responsible for making the resource | [ProvEntity](ProvEntity.md) |
| [saref_hasProperty](saref_hasProperty.md) | * <br/> [SarefProperty](SarefProperty.md) | Links a feature kind or a feature of interest to one of its properties | [ProvEntity](ProvEntity.md) |
| [saref_hasPropertyValue](saref_hasPropertyValue.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | Links a feature kind, a feature of interest, or a property of interest, to a ... | [ProvEntity](ProvEntity.md) |
| [owl_versionInfo](owl_versionInfo.md) | 0..1 <br/> [String](String.md) | An owl:versionInfo statement generally has as its object a string giving info... | [OwlThing](OwlThing.md) |
| [rdfs_label](rdfs_label.md) | 1..* <br/> [String](String.md) | human-readable version of a resource's name | [OwlThing](OwlThing.md) |
| [rdfs_comment](rdfs_comment.md) | 1..* <br/> [String](String.md) | A textual comment helps clarify the meaning of RDF classes and properties | [OwlThing](OwlThing.md) |
| [prov_hadPrimarySource](prov_hadPrimarySource.md) | * <br/> [ProvEntity](ProvEntity.md) | A primary source for a topic refers to something produced by some agent with ... | [OwlThing](OwlThing.md) |
| [prov_wasGeneratedBy](prov_wasGeneratedBy.md) | * <br/> [SuloProcess](SuloProcess.md) | Generation is the completion of production of a new entity by an activity | [OwlThing](OwlThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoQuestionnaire](QoQuestionnaire.md) | [qo_hasOrderedSection](qo_hasOrderedSection.md) | range | [QoOrderedSection](QoOrderedSection.md) |
| [QoOrderedSection](QoOrderedSection.md) | [qo_section](qo_section.md) | domain | [QoOrderedSection](QoOrderedSection.md) |
| [QoSection](QoSection.md) | [qo_hasOrderedSection](qo_hasOrderedSection.md) | range | [QoOrderedSection](QoOrderedSection.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:OrderedSection |
| native | qo:QoOrderedSection |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: qo_OrderedSection
description: A contextual wrapper that binds a thematic grouping of inquiry items
  to a specific sequence index within a survey template or parent group.
from_schema: https://ns.faqir.org/q-o
is_a: prov_Entity
slots:
- qo_section
- qo_order
- qo_hardValidity
- qo_temporalValidity
- qo_conditionalValidity
slot_usage:
  qo_order:
    name: qo_order
    description: Section position in the questionnaire or section (1-based index).
class_uri: qo:OrderedSection
unique_keys:
  unique_section_order_per_questionnaire:
    unique_key_name: unique_section_order_per_questionnaire
    unique_key_slots:
    - qo_order
    description: Section order values must be unique

```
</details>

### Induced

<details>
```yaml
name: qo_OrderedSection
description: A contextual wrapper that binds a thematic grouping of inquiry items
  to a specific sequence index within a survey template or parent group.
from_schema: https://ns.faqir.org/q-o
is_a: prov_Entity
slot_usage:
  qo_order:
    name: qo_order
    description: Section position in the questionnaire or section (1-based index).
attributes:
  qo_section:
    name: qo_section
    description: Identifies the specific thematic grouping referenced at a given positional
      index.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    is_a: dcterms_hasPart
    domain: qo_OrderedSection
    slot_uri: qo:section
    alias: qo_section
    owner: qo_OrderedSection
    domain_of:
    - qo_OrderedSection
    range: qo_Section
    required: true
    multivalued: true
  qo_order:
    name: qo_order
    description: Section position in the questionnaire or section (1-based index).
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:order
    alias: qo_order
    owner: qo_OrderedSection
    domain_of:
    - qo_OrderedSection
    - qo_OrderedQuestion
    range: integer
    required: true
    minimum_value: 1
  qo_hardValidity:
    name: qo_hardValidity
    description: Specifies the operational enforcement mechanism of a duration limit;
      when true, expiration acts as a strict invalidation threshold for re-use, whereas
      when false, it serves as a non-binding recommendation.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:hardValidity
    ifabsent: 'False'
    alias: qo_hardValidity
    owner: qo_OrderedSection
    domain_of:
    - qo_Questionnaire
    - qo_OrderedSection
    - qo_Section
    - qo_OrderedQuestion
    - qo_Question
    range: boolean
    required: false
  qo_temporalValidity:
    name: qo_temporalValidity
    description: Defines the time extent following generation during which a recorded
      answer remains valid for automated longitudinal reuse without requiring re-administration.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    is_a: time_hasDuration
    slot_uri: qo:temporalValidity
    alias: qo_temporalValidity
    owner: qo_OrderedSection
    domain_of:
    - qo_Questionnaire
    - qo_OrderedSection
    - qo_Section
    - qo_OrderedQuestion
    - qo_Question
    range: time_Duration
    required: true
  qo_conditionalValidity:
    name: qo_conditionalValidity
    description: A machine-readable rule statement defining an intervening event or
      state change that revokes the validity of a recorded observation prior to its
      natural temporal expiration.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:conditionalValidity
    alias: qo_conditionalValidity
    owner: qo_OrderedSection
    domain_of:
    - qo_Questionnaire
    - qo_OrderedSection
    - qo_Section
    - qo_OrderedQuestion
    - qo_Question
    range: string
    required: false
  prov_wasAttributedTo:
    name: prov_wasAttributedTo
    description: Attribution is the ascribing of an entity to an agent.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: prov_Entity
    slot_uri: prov:wasAttributedTo
    alias: prov_wasAttributedTo
    owner: qo_OrderedSection
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
    owner: qo_OrderedSection
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
    owner: qo_OrderedSection
    domain_of:
    - prov_Entity
    range: datetime
    required: false
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
    slot_uri: prov:type
    alias: prov_type
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: uriorcurie
    required: false
    multivalued: true
  dcterms_hasPart:
    name: dcterms_hasPart
    description: A related resource that is included either physically or logically
      in the described resource.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:hasPart
    alias: dcterms_hasPart
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
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
    slot_uri: dcterms:isPartOf
    alias: dcterms_isPartOf
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
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
    slot_uri: prov:generatedAtTime
    alias: prov_generatedAtTime
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - prov_Entity
    range: datetime
    required: false
    multivalued: true
  fhir_status:
    name: fhir_status
    description: A code specifying the state of the observation/procedure/questionnaire...
      Generally, this will be the in-progress or completed state.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    is_a: saref_hasPropertyValue
    slot_uri: fhir:resource-status
    alias: fhir_status
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
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
    slot_uri: dcterms:creator
    alias: dcterms_creator
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: foaf_Agent
    required: false
    multivalued: true
  saref_hasProperty:
    name: saref_hasProperty
    description: Links a feature kind or a feature of interest to one of its properties.
    from_schema: https://ns.faqir.org/q-o
    mappings:
    - ssn:hasProperty
    rank: 1000
    slot_uri: saref:hasProperty
    alias: saref_hasProperty
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
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
    slot_uri: saref:hasPropertyValue
    alias: saref_hasPropertyValue
    owner: qo_OrderedSection
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: saref_PropertyValue
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
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
    owner: qo_OrderedSection
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
    owner: qo_OrderedSection
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
    owner: qo_OrderedSection
    domain_of:
    - owl_Thing
    range: string
    required: true
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
    owner: qo_OrderedSection
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
    owner: qo_OrderedSection
    domain_of:
    - owl_Thing
    range: sulo_Process
    required: false
    multivalued: true
class_uri: qo:OrderedSection
unique_keys:
  unique_section_order_per_questionnaire:
    unique_key_name: unique_section_order_per_questionnaire
    unique_key_slots:
    - qo_order
    description: Section order values must be unique

```
</details>