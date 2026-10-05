

# Class: QoQuestion 


_An individual inquiry item within an instrument that specifies an information requirement and constrains the acceptable response format._





URI: [qo:Question](https://ns.faqir.org/q-o#Question)






```mermaid
 classDiagram
    class QoQuestion
    click QoQuestion href "../QoQuestion"
      ProvEntity <|-- QoQuestion
        click ProvEntity href "../ProvEntity"
      
      QoQuestion : dcterms_created
        
      QoQuestion : dcterms_creator
        
          
    
        
        
        QoQuestion --> "1..*" ProvOrganization : dcterms_creator
        click ProvOrganization href "../ProvOrganization"
    

        
      QoQuestion : dcterms_hasPart
        
          
    
        
        
        QoQuestion --> "*" OwlThing : dcterms_hasPart
        click OwlThing href "../OwlThing"
    

        
      QoQuestion : dcterms_isPartOf
        
          
    
        
        
        QoQuestion --> "*" OwlThing : dcterms_isPartOf
        click OwlThing href "../OwlThing"
    

        
      QoQuestion : dcterms_modified
        
      QoQuestion : fhir_status
        
          
    
        
        
        QoQuestion --> "*" SarefPropertyValue : fhir_status
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      QoQuestion : owl_versionInfo
        
      QoQuestion : prov_generatedAtTime
        
      QoQuestion : prov_hadPrimarySource
        
          
    
        
        
        QoQuestion --> "*" ProvEntity : prov_hadPrimarySource
        click ProvEntity href "../ProvEntity"
    

        
      QoQuestion : prov_type
        
          
    
        
        
        QoQuestion --> "1..*" QoQuestionType : prov_type
        click QoQuestionType href "../QoQuestionType"
    

        
      QoQuestion : prov_wasAttributedTo
        
          
    
        
        
        QoQuestion --> "*" FoafAgent : prov_wasAttributedTo
        click FoafAgent href "../FoafAgent"
    

        
      QoQuestion : prov_wasGeneratedBy
        
          
    
        
        
        QoQuestion --> "*" SuloProcess : prov_wasGeneratedBy
        click SuloProcess href "../SuloProcess"
    

        
      QoQuestion : qo_codingOrdinal
        
      QoQuestion : qo_codingParams
        
          
    
        
        
        QoQuestion --> "*" ValueCoding : qo_codingParams
        click ValueCoding href "../ValueCoding"
    

        
      QoQuestion : qo_intervalParams
        
          
    
        
        
        QoQuestion --> "0..1" IntervalParams : qo_intervalParams
        click IntervalParams href "../IntervalParams"
    

        
      QoQuestion : qo_multivalued
        
      QoQuestion : qo_numericalParams
        
          
    
        
        
        QoQuestion --> "0..1" NumericalParams : qo_numericalParams
        click NumericalParams href "../NumericalParams"
    

        
      QoQuestion : qo_tag
        
      QoQuestion : rdfs_comment
        
      QoQuestion : rdfs_label
        
      QoQuestion : saref_hasProperty
        
          
    
        
        
        QoQuestion --> "*" SarefProperty : saref_hasProperty
        click SarefProperty href "../SarefProperty"
    

        
      QoQuestion : saref_hasPropertyValue
        
          
    
        
        
        QoQuestion --> "*" SarefPropertyValue : saref_hasPropertyValue
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      
```





## Inheritance
* [OwlThing](OwlThing.md)
    * [ProvEntity](ProvEntity.md)
        * **QoQuestion**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [qo_multivalued](qo_multivalued.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether this question allows more than one answer (true) or only on... | direct |
| [qo_tag](qo_tag.md) | 1..* <br/> [String](String.md) | A machine-readable alphanumeric code or mnemonic string used for internal ref... | direct |
| [qo_numericalParams](qo_numericalParams.md) | 0..1 <br/> [NumericalParams](NumericalParams.md) | Specifies measurement units and decimal precision constraints governing accep... | direct |
| [qo_codingParams](qo_codingParams.md) | * <br/> [ValueCoding](ValueCoding.md) | Defines the permissible standardized concept codes and human-readable labels ... | direct |
| [qo_codingOrdinal](qo_codingOrdinal.md) | 0..1 <br/> [Boolean](Boolean.md) | Specifies whether permissible selection options possess a meaningful inherent... | direct |
| [qo_intervalParams](qo_intervalParams.md) | 0..1 <br/> [IntervalParams](IntervalParams.md) | Defines lower and upper boundary limits bounding acceptable numeric values | direct |
| [prov_wasAttributedTo](prov_wasAttributedTo.md) | * <br/> [FoafAgent](FoafAgent.md) | Attribution is the ascribing of an entity to an agent | [ProvEntity](ProvEntity.md) |
| [dcterms_created](dcterms_created.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the entity was created | [ProvEntity](ProvEntity.md) |
| [dcterms_modified](dcterms_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the entity was last updated | [ProvEntity](ProvEntity.md) |
| [prov_type](prov_type.md) | 1..* <br/> [QoQuestionType](QoQuestionType.md) | Type of the question (e | [ProvEntity](ProvEntity.md) |
| [dcterms_hasPart](dcterms_hasPart.md) | * <br/> [OwlThing](OwlThing.md) | A related resource that is included either physically or logically in the des... | [ProvEntity](ProvEntity.md) |
| [dcterms_isPartOf](dcterms_isPartOf.md) | * <br/> [OwlThing](OwlThing.md) | A related resource in which the described resource is physically or logically... | [ProvEntity](ProvEntity.md) |
| [prov_generatedAtTime](prov_generatedAtTime.md) | * <br/> [Datetime](Datetime.md) | The time at which an entity was completely created and is available for use | [ProvEntity](ProvEntity.md) |
| [fhir_status](fhir_status.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | A code specifying the state of the observation/procedure/questionnaire | [ProvEntity](ProvEntity.md) |
| [dcterms_creator](dcterms_creator.md) | 1..* <br/> [ProvOrganization](ProvOrganization.md) | An entity responsible for making the resource | [ProvEntity](ProvEntity.md) |
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
| [QoOrderedQuestion](QoOrderedQuestion.md) | [qo_question](qo_question.md) | range | [QoQuestion](QoQuestion.md) |
| [QoAnswer](QoAnswer.md) | [qo_toQuestion](qo_toQuestion.md) | range | [QoQuestion](QoQuestion.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:Question |
| native | qo:QoQuestion |
| narrow | fhir:Questionnaire.item.where(type='question') |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: qo_Question
description: An individual inquiry item within an instrument that specifies an information
  requirement and constrains the acceptable response format.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire.item.where(type='question')
is_a: prov_Entity
slots:
- qo_multivalued
slot_usage:
  prov_type:
    name: prov_type
    description: Type of the question (e.g., choice, openChoice, numberInterval, decimal,
      dateTime, text). Determines valid answers.
    range: qo_QuestionType
    required: true
  dcterms_creator:
    name: dcterms_creator
    range: prov_Organization
    required: true
attributes:
  qo_tag:
    name: qo_tag
    description: A machine-readable alphanumeric code or mnemonic string used for
      internal reference and translation lookup.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:tag
    domain_of:
    - qo_Question
    range: string
    required: true
    multivalued: true
  qo_numericalParams:
    name: qo_numericalParams
    description: Specifies measurement units and decimal precision constraints governing
      acceptable quantitative input.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:numericalParams
    domain_of:
    - qo_Question
    range: NumericalParams
    required: false
    multivalued: false
  qo_codingParams:
    name: qo_codingParams
    description: Defines the permissible standardized concept codes and human-readable
      labels available for selection.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:codingParams
    domain_of:
    - qo_Question
    range: ValueCoding
    required: false
    multivalued: true
  qo_codingOrdinal:
    name: qo_codingOrdinal
    description: Specifies whether permissible selection options possess a meaningful
      inherent ranking (true) or represent nominal categories (false).
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:codingOrdinal
    ifabsent: 'False'
    domain_of:
    - qo_Question
    range: boolean
  qo_intervalParams:
    name: qo_intervalParams
    description: Defines lower and upper boundary limits bounding acceptable numeric
      values.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:intervalParams
    domain_of:
    - qo_Question
    range: IntervalParams
    required: false
    multivalued: false
class_uri: qo:Question
rules:
- preconditions:
    slot_conditions:
      prov_type:
        name: prov_type
        equals_string_in:
        - choice
        - openChoice
  postconditions:
    slot_conditions:
      qo_codingParams:
        name: qo_codingParams
        required: true
  description: If prov_type is 'choice' or 'openChoice', codingParams is required.
- preconditions:
    slot_conditions:
      prov_type:
        name: prov_type
        equals_string_in:
        - numberInterval
  postconditions:
    slot_conditions:
      qo_numericalParams:
        name: qo_numericalParams
        required: true
      qo_intervalParams:
        name: qo_intervalParams
        required: true
  description: If prov_type is 'numberInterval', numericalParams and intervalParams
    are required.
- preconditions:
    slot_conditions:
      prov_type:
        name: prov_type
        equals_string_in:
        - decimal
  postconditions:
    slot_conditions:
      qo_numericalParams:
        name: qo_numericalParams
        required: true
  description: If prov_type is 'decimal', numericalParams is required.

```
</details>

### Induced

<details>
```yaml
name: qo_Question
description: An individual inquiry item within an instrument that specifies an information
  requirement and constrains the acceptable response format.
from_schema: https://ns.faqir.org/q-o
narrow_mappings:
- fhir:Questionnaire.item.where(type='question')
is_a: prov_Entity
slot_usage:
  prov_type:
    name: prov_type
    description: Type of the question (e.g., choice, openChoice, numberInterval, decimal,
      dateTime, text). Determines valid answers.
    range: qo_QuestionType
    required: true
  dcterms_creator:
    name: dcterms_creator
    range: prov_Organization
    required: true
attributes:
  qo_tag:
    name: qo_tag
    description: A machine-readable alphanumeric code or mnemonic string used for
      internal reference and translation lookup.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:tag
    alias: qo_tag
    owner: qo_Question
    domain_of:
    - qo_Question
    range: string
    required: true
    multivalued: true
  qo_numericalParams:
    name: qo_numericalParams
    description: Specifies measurement units and decimal precision constraints governing
      acceptable quantitative input.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:numericalParams
    alias: qo_numericalParams
    owner: qo_Question
    domain_of:
    - qo_Question
    range: NumericalParams
    required: false
    multivalued: false
  qo_codingParams:
    name: qo_codingParams
    description: Defines the permissible standardized concept codes and human-readable
      labels available for selection.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:codingParams
    alias: qo_codingParams
    owner: qo_Question
    domain_of:
    - qo_Question
    range: ValueCoding
    required: false
    multivalued: true
  qo_codingOrdinal:
    name: qo_codingOrdinal
    description: Specifies whether permissible selection options possess a meaningful
      inherent ranking (true) or represent nominal categories (false).
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:codingOrdinal
    ifabsent: 'False'
    alias: qo_codingOrdinal
    owner: qo_Question
    domain_of:
    - qo_Question
    range: boolean
  qo_intervalParams:
    name: qo_intervalParams
    description: Defines lower and upper boundary limits bounding acceptable numeric
      values.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:intervalParams
    alias: qo_intervalParams
    owner: qo_Question
    domain_of:
    - qo_Question
    range: IntervalParams
    required: false
    multivalued: false
  qo_multivalued:
    name: qo_multivalued
    description: Indicates whether this question allows more than one answer (true)
      or only one (false).
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:multivalued
    ifabsent: 'False'
    alias: qo_multivalued
    owner: qo_Question
    domain_of:
    - qo_Question
    range: boolean
  prov_wasAttributedTo:
    name: prov_wasAttributedTo
    description: Attribution is the ascribing of an entity to an agent.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: prov_Entity
    slot_uri: prov:wasAttributedTo
    alias: prov_wasAttributedTo
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
    domain_of:
    - prov_Entity
    range: datetime
    required: false
  prov_type:
    name: prov_type
    description: Type of the question (e.g., choice, openChoice, numberInterval, decimal,
      dateTime, text). Determines valid answers.
    from_schema: https://ns.faqir.org/q-o
    exact_mappings:
    - rdf:type
    - sphn:hasTypeCode
    narrow_mappings:
    - schema:procedureType
    rank: 1000
    slot_uri: prov:type
    alias: prov_type
    owner: qo_Question
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: qo_QuestionType
    required: true
    multivalued: true
  dcterms_hasPart:
    name: dcterms_hasPart
    description: A related resource that is included either physically or logically
      in the described resource.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:hasPart
    alias: dcterms_hasPart
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
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
    owner: qo_Question
    domain_of:
    - owl_Thing
    range: sulo_Process
    required: false
    multivalued: true
class_uri: qo:Question
rules:
- preconditions:
    slot_conditions:
      prov_type:
        name: prov_type
        equals_string_in:
        - choice
        - openChoice
  postconditions:
    slot_conditions:
      qo_codingParams:
        name: qo_codingParams
        required: true
  description: If prov_type is 'choice' or 'openChoice', codingParams is required.
- preconditions:
    slot_conditions:
      prov_type:
        name: prov_type
        equals_string_in:
        - numberInterval
  postconditions:
    slot_conditions:
      qo_numericalParams:
        name: qo_numericalParams
        required: true
      qo_intervalParams:
        name: qo_intervalParams
        required: true
  description: If prov_type is 'numberInterval', numericalParams and intervalParams
    are required.
- preconditions:
    slot_conditions:
      prov_type:
        name: prov_type
        equals_string_in:
        - decimal
  postconditions:
    slot_conditions:
      qo_numericalParams:
        name: qo_numericalParams
        required: true
  description: If prov_type is 'decimal', numericalParams is required.

```
</details>