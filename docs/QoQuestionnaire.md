

# Class: QoQuestionnaire 


_A structured, reusable instrument or template composed of ordered items designed to collect standardized information from an individual or system._





URI: [qo:Questionnaire](https://ns.faqir.org/q-o#Questionnaire)






```mermaid
 classDiagram
    class QoQuestionnaire
    click QoQuestionnaire href "../QoQuestionnaire"
      ProvEntity <|-- QoQuestionnaire
        click ProvEntity href "../ProvEntity"
      
      QoQuestionnaire : dcterms_created
        
      QoQuestionnaire : dcterms_creator
        
          
    
        
        
        QoQuestionnaire --> "1..*" ProvOrganization : dcterms_creator
        click ProvOrganization href "../ProvOrganization"
    

        
      QoQuestionnaire : dcterms_hasPart
        
          
    
        
        
        QoQuestionnaire --> "*" OwlThing : dcterms_hasPart
        click OwlThing href "../OwlThing"
    

        
      QoQuestionnaire : dcterms_isPartOf
        
          
    
        
        
        QoQuestionnaire --> "*" SuloProcess : dcterms_isPartOf
        click SuloProcess href "../SuloProcess"
    

        
      QoQuestionnaire : dcterms_modified
        
      QoQuestionnaire : fhir_status
        
          
    
        
        
        QoQuestionnaire --> "1" QoQuestionnaireStatus : fhir_status
        click QoQuestionnaireStatus href "../QoQuestionnaireStatus"
    

        
      QoQuestionnaire : owl_versionInfo
        
      QoQuestionnaire : prov_generatedAtTime
        
      QoQuestionnaire : prov_hadPrimarySource
        
          
    
        
        
        QoQuestionnaire --> "*" ProvEntity : prov_hadPrimarySource
        click ProvEntity href "../ProvEntity"
    

        
      QoQuestionnaire : prov_type
        
      QoQuestionnaire : prov_wasAttributedTo
        
          
    
        
        
        QoQuestionnaire --> "*" FoafAgent : prov_wasAttributedTo
        click FoafAgent href "../FoafAgent"
    

        
      QoQuestionnaire : prov_wasGeneratedBy
        
          
    
        
        
        QoQuestionnaire --> "*" SuloProcess : prov_wasGeneratedBy
        click SuloProcess href "../SuloProcess"
    

        
      QoQuestionnaire : qo_hasOrderedQuestion
        
          
    
        
        
        QoQuestionnaire --> "*" QoOrderedQuestion : qo_hasOrderedQuestion
        click QoOrderedQuestion href "../QoOrderedQuestion"
    

        
      QoQuestionnaire : qo_hasOrderedSection
        
          
    
        
        
        QoQuestionnaire --> "*" QoOrderedSection : qo_hasOrderedSection
        click QoOrderedSection href "../QoOrderedSection"
    

        
      QoQuestionnaire : rdfs_comment
        
      QoQuestionnaire : rdfs_label
        
      QoQuestionnaire : saref_hasProperty
        
          
    
        
        
        QoQuestionnaire --> "*" SarefProperty : saref_hasProperty
        click SarefProperty href "../SarefProperty"
    

        
      QoQuestionnaire : saref_hasPropertyValue
        
          
    
        
        
        QoQuestionnaire --> "*" SarefPropertyValue : saref_hasPropertyValue
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      
```





## Inheritance
* [OwlThing](OwlThing.md)
    * [ProvEntity](ProvEntity.md)
        * **QoQuestionnaire**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [qo_hasOrderedQuestion](qo_hasOrderedQuestion.md) | * <br/> [QoOrderedQuestion](QoOrderedQuestion.md) | Associates a survey container or group with a sequence-indexed wrapper holdin... | direct |
| [qo_hasOrderedSection](qo_hasOrderedSection.md) | * <br/> [QoOrderedSection](QoOrderedSection.md) | Associates a survey container or group with a sequence-indexed wrapper holdin... | direct |
| [prov_wasAttributedTo](prov_wasAttributedTo.md) | * <br/> [FoafAgent](FoafAgent.md) | Attribution is the ascribing of an entity to an agent | [ProvEntity](ProvEntity.md) |
| [dcterms_created](dcterms_created.md) | 1 <br/> [Datetime](Datetime.md) | The date and time when the questionnaire was created | [ProvEntity](ProvEntity.md) |
| [dcterms_modified](dcterms_modified.md) | 1 <br/> [Datetime](Datetime.md) | The date and time when the questionnaire was last updated | [ProvEntity](ProvEntity.md) |
| [prov_type](prov_type.md) | * <br/> [Uriorcurie](Uriorcurie.md) | The attribute prov:type provides further typing information for any construct... | [ProvEntity](ProvEntity.md) |
| [dcterms_hasPart](dcterms_hasPart.md) | * <br/> [OwlThing](OwlThing.md) | A related resource that is included either physically or logically in the des... | [ProvEntity](ProvEntity.md) |
| [dcterms_isPartOf](dcterms_isPartOf.md) | * <br/> [SuloProcess](SuloProcess.md) | Process this questionnaire is part of | [ProvEntity](ProvEntity.md) |
| [prov_generatedAtTime](prov_generatedAtTime.md) | * <br/> [Datetime](Datetime.md) | The time at which an entity was completely created and is available for use | [ProvEntity](ProvEntity.md) |
| [fhir_status](fhir_status.md) | 1 <br/> [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | A code specifying the state of the observation/procedure/questionnaire | [ProvEntity](ProvEntity.md) |
| [dcterms_creator](dcterms_creator.md) | 1..* <br/> [ProvOrganization](ProvOrganization.md) | The Organization that has created this Questionnaire | [ProvEntity](ProvEntity.md) |
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
| [QoQuestionnaire](QoQuestionnaire.md) | [qo_hasOrderedQuestion](qo_hasOrderedQuestion.md) | domain | [QoQuestionnaire](QoQuestionnaire.md) |
| [QoQuestionnaire](QoQuestionnaire.md) | [qo_hasOrderedSection](qo_hasOrderedSection.md) | domain | [QoQuestionnaire](QoQuestionnaire.md) |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | [qo_responds](qo_responds.md) | range | [QoQuestionnaire](QoQuestionnaire.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:Questionnaire |
| native | qo:QoQuestionnaire |
| narrow | fhir:Questionnaire |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: qo_Questionnaire
description: A structured, reusable instrument or template composed of ordered items
  designed to collect standardized information from an individual or system.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire
is_a: prov_Entity
slots:
- qo_hasOrderedQuestion
- qo_hasOrderedSection
slot_usage:
  dcterms_created:
    name: dcterms_created
    description: The date and time when the questionnaire was created.
    required: true
  dcterms_modified:
    name: dcterms_modified
    description: The date and time when the questionnaire was last updated.
    mappings:
    - prov:endedAtTime
    - fhir:Questionnaire.date
    required: true
  dcterms_creator:
    name: dcterms_creator
    description: The Organization that has created this Questionnaire.
    mappings:
    - fhir:Questionnaire.author
    range: prov_Organization
    required: true
    multivalued: true
  dcterms_isPartOf:
    name: dcterms_isPartOf
    description: Process this questionnaire is part of.
    range: sulo_Process
    required: false
    multivalued: true
  fhir_status:
    name: fhir_status
    range: qo_QuestionnaireStatus
    required: true
    multivalued: false
  qo_hasOrderedQuestion:
    name: qo_hasOrderedQuestion
    domain: qo_Questionnaire
  qo_hasOrderedSection:
    name: qo_hasOrderedSection
    domain: qo_Questionnaire
class_uri: qo:Questionnaire

```
</details>

### Induced

<details>
```yaml
name: qo_Questionnaire
description: A structured, reusable instrument or template composed of ordered items
  designed to collect standardized information from an individual or system.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire
is_a: prov_Entity
slot_usage:
  dcterms_created:
    name: dcterms_created
    description: The date and time when the questionnaire was created.
    required: true
  dcterms_modified:
    name: dcterms_modified
    description: The date and time when the questionnaire was last updated.
    mappings:
    - prov:endedAtTime
    - fhir:Questionnaire.date
    required: true
  dcterms_creator:
    name: dcterms_creator
    description: The Organization that has created this Questionnaire.
    mappings:
    - fhir:Questionnaire.author
    range: prov_Organization
    required: true
    multivalued: true
  dcterms_isPartOf:
    name: dcterms_isPartOf
    description: Process this questionnaire is part of.
    range: sulo_Process
    required: false
    multivalued: true
  fhir_status:
    name: fhir_status
    range: qo_QuestionnaireStatus
    required: true
    multivalued: false
  qo_hasOrderedQuestion:
    name: qo_hasOrderedQuestion
    domain: qo_Questionnaire
  qo_hasOrderedSection:
    name: qo_hasOrderedSection
    domain: qo_Questionnaire
attributes:
  qo_hasOrderedQuestion:
    name: qo_hasOrderedQuestion
    description: Associates a survey container or group with a sequence-indexed wrapper
      holding an individual inquiry item.
    from_schema: https://ns.faqir.org/q-o
    narrow_mappings:
    - fhir:Questionnaire.item.where(type='question')
    rank: 1000
    is_a: dcterms_hasPart
    domain: qo_Questionnaire
    slot_uri: qo:hasOrderedQuestion
    alias: qo_hasOrderedQuestion
    owner: qo_Questionnaire
    domain_of:
    - qo_Questionnaire
    - qo_Section
    range: qo_OrderedQuestion
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  qo_hasOrderedSection:
    name: qo_hasOrderedSection
    description: Associates a survey container or group with a sequence-indexed wrapper
      holding a nested thematic subgroup.
    from_schema: https://ns.faqir.org/q-o
    narrow_mappings:
    - fhir:Questionnaire.item.where(type='group')
    rank: 1000
    is_a: dcterms_hasPart
    domain: qo_Questionnaire
    slot_uri: qo:hasOrderedSection
    alias: qo_hasOrderedSection
    owner: qo_Questionnaire
    domain_of:
    - qo_Questionnaire
    - qo_Section
    range: qo_OrderedSection
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  prov_wasAttributedTo:
    name: prov_wasAttributedTo
    description: Attribution is the ascribing of an entity to an agent.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: prov_Entity
    slot_uri: prov:wasAttributedTo
    alias: prov_wasAttributedTo
    owner: qo_Questionnaire
    domain_of:
    - prov_Entity
    range: foaf_Agent
    required: false
    multivalued: true
  dcterms_created:
    name: dcterms_created
    description: The date and time when the questionnaire was created.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:created
    alias: dcterms_created
    owner: qo_Questionnaire
    domain_of:
    - prov_Entity
    range: datetime
    required: true
  dcterms_modified:
    name: dcterms_modified
    description: The date and time when the questionnaire was last updated.
    from_schema: https://ns.faqir.org/q-o
    mappings:
    - prov:endedAtTime
    - fhir:Questionnaire.date
    rank: 1000
    slot_uri: dcterms:modified
    alias: dcterms_modified
    owner: qo_Questionnaire
    domain_of:
    - prov_Entity
    range: datetime
    required: true
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
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
    description: Process this questionnaire is part of.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:isPartOf
    alias: dcterms_isPartOf
    owner: qo_Questionnaire
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    inverse: dcterms_hasPart
    range: sulo_Process
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: qo_QuestionnaireStatus
    required: true
    multivalued: false
    inlined: true
    inlined_as_list: true
  dcterms_creator:
    name: dcterms_creator
    description: The Organization that has created this Questionnaire.
    from_schema: https://ns.faqir.org/q-o
    mappings:
    - fhir:Questionnaire.author
    rank: 1000
    slot_uri: dcterms:creator
    alias: dcterms_creator
    owner: qo_Questionnaire
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: prov_Organization
    required: true
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
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
    owner: qo_Questionnaire
    domain_of:
    - owl_Thing
    range: sulo_Process
    required: false
    multivalued: true
class_uri: qo:Questionnaire

```
</details>