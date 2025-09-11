# Auto generated from datamodel.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-11T17:38:46
# Schema: datamodel
#
# id: https://w3id.org/faqir/datamodel
# description: The datamodel used in faqir vaults.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Namespaces
DATAMODEL = CurieNamespace('datamodel', 'https://w3id.org/faqir/datamodel/')
EUVOC = CurieNamespace('euVoc', 'http://publications.europa.eu/resource/authority/resource-type/')
FAQIR = CurieNamespace('faqir', 'https://faqir.org/datamodel/')
FHIR = CurieNamespace('fhir', 'https://www.hl7.org/fhir/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOINC = CurieNamespace('loinc', 'https://loinc.org/')
PROV = CurieNamespace('prov', 'https://www.w3.org/TR/prov-overview/')
QUESTIONNAIRE = CurieNamespace('questionnaire', 'https://w3id.org/faqir/datamodel/questionnaire/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TYPES = CurieNamespace('types', 'https://w3id.org/faqir/datamodel/core/types')
UCUM = CurieNamespace('ucum', 'https://unitsofmeasure.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DATAMODEL


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = DATAMODEL.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = DATAMODEL.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD["boolean"]
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = DATAMODEL.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = DATAMODEL.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = DATAMODEL.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = DATAMODEL.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD["time"]
    type_class_curie = "xsd:time"
    type_name = "time"
    type_model_uri = DATAMODEL.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = DATAMODEL.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = DATAMODEL.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML["DateOrDatetime"]
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = DATAMODEL.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = DATAMODEL.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = DATAMODEL.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = DATAMODEL.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = DATAMODEL.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX["iri"]
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = DATAMODEL.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX["nonLiteral"]
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = DATAMODEL.Nodeidentifier


class Jsonpointer(str):
    """ A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpointer"
    type_model_uri = DATAMODEL.Jsonpointer


class Jsonpath(str):
    """ A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpath"
    type_model_uri = DATAMODEL.Jsonpath


class Sparqlpath(str):
    """ A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sparqlpath"
    type_model_uri = DATAMODEL.Sparqlpath


# Class references
class VaultVaultId(URIorCURIE):
    pass


class OrganizationOrganizationId(URIorCURIE):
    pass


class ProcedureProcedureId(URIorCURIE):
    pass


class QuestionnaireResponseQuestionnaireResponseId(URIorCURIE):
    pass


class AnswerAnswerId(URIorCURIE):
    pass


class OrderedQuestionOrderedQuestionId(URIorCURIE):
    pass


class QuestionQuestionId(URIorCURIE):
    pass


class QuestionnaireQuestionnaireId(URIorCURIE):
    pass


class OrderedSectionOrderedSectionId(URIorCURIE):
    pass


class SectionSectionId(URIorCURIE):
    pass


class ScoreDefinitionScoreDefinitionId(URIorCURIE):
    pass


class ScoreParameterScoreParameterId(URIorCURIE):
    pass


class ScoreValueScoreValueId(URIorCURIE):
    pass


@dataclass(repr=False)
class FullName(YAMLRoot):
    """
    Structured full name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATAMODEL["vault/FullName"]
    class_class_curie: ClassVar[str] = "datamodel:vault/FullName"
    class_name: ClassVar[str] = "FullName"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.FullName

    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    family_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.middle_name is not None and not isinstance(self.middle_name, str):
            self.middle_name = str(self.middle_name)

        if self.family_name is not None and not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueNumerical(YAMLRoot):
    """
    Base class for quantitative values, they may have units and precision.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ValueNumerical"]
    class_class_curie: ClassVar[str] = "faqir:ValueNumerical"
    class_name: ClassVar[str] = "ValueNumerical"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ValueNumerical

    numericalValue: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.numericalValue):
            self.MissingRequiredField("numericalValue")
        if not isinstance(self.numericalValue, Decimal):
            self.numericalValue = Decimal(self.numericalValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Weight(ValueNumerical):
    """
    Weight.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATAMODEL["vault/Weight"]
    class_class_curie: ClassVar[str] = "datamodel:vault/Weight"
    class_name: ClassVar[str] = "Weight"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Weight

    numericalValue: Decimal = None
    weightType: Union[str, "WeightType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.weightType):
            self.MissingRequiredField("weightType")
        if not isinstance(self.weightType, WeightType):
            self.weightType = WeightType(self.weightType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NumericalParams(YAMLRoot):
    """
    Parameters for quantitative values, including unit and precision.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["NumericalParams"]
    class_class_curie: ClassVar[str] = "faqir:NumericalParams"
    class_name: ClassVar[str] = "NumericalParams"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.NumericalParams

    numericalUnit: Optional[Union[str, "UnitOfMeasure"]] = None
    numericalPrecision: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.numericalUnit is not None and not isinstance(self.numericalUnit, UnitOfMeasure):
            self.numericalUnit = UnitOfMeasure(self.numericalUnit)

        if self.numericalPrecision is not None and not isinstance(self.numericalPrecision, int):
            self.numericalPrecision = int(self.numericalPrecision)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntervalParams(YAMLRoot):
    """
    Parameters for interval values, including minimum and maximum values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["IntervalParams"]
    class_class_curie: ClassVar[str] = "faqir:IntervalParams"
    class_name: ClassVar[str] = "IntervalParams"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.IntervalParams

    minValue: float = None
    maxValue: float = None
    minLabel: Optional[str] = None
    maxLabel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.minValue):
            self.MissingRequiredField("minValue")
        if not isinstance(self.minValue, float):
            self.minValue = float(self.minValue)

        if self._is_empty(self.maxValue):
            self.MissingRequiredField("maxValue")
        if not isinstance(self.maxValue, float):
            self.maxValue = float(self.maxValue)

        if self.minLabel is not None and not isinstance(self.minLabel, str):
            self.minLabel = str(self.minLabel)

        if self.maxLabel is not None and not isinstance(self.maxLabel, str):
            self.maxLabel = str(self.maxLabel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueString(YAMLRoot):
    """
    A string value, typically used for text or identifiers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ValueString"]
    class_class_curie: ClassVar[str] = "faqir:ValueString"
    class_name: ClassVar[str] = "ValueString"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ValueString

    stringValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.stringValue):
            self.MissingRequiredField("stringValue")
        if not isinstance(self.stringValue, str):
            self.stringValue = str(self.stringValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueDateTime(YAMLRoot):
    """
    A date and time value, typically in ISO 8601 format.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ValueDateTime"]
    class_class_curie: ClassVar[str] = "faqir:ValueDateTime"
    class_name: ClassVar[str] = "ValueDateTime"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ValueDateTime

    dateTimeValue: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.dateTimeValue is not None and not isinstance(self.dateTimeValue, XSDDateTime):
            self.dateTimeValue = XSDDateTime(self.dateTimeValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueCoding(YAMLRoot):
    """
    A coded value with a unique code for each display text, typically used for standardized questionnaires.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ValueCoding"]
    class_class_curie: ClassVar[str] = "faqir:ValueCoding"
    class_name: ClassVar[str] = "ValueCoding"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ValueCoding

    code: str = None
    display: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self._is_empty(self.display):
            self.MissingRequiredField("display")
        if not isinstance(self.display, str):
            self.display = str(self.display)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Metadata(YAMLRoot):
    """
    Base class for metadata tracking (e.g. schema versioning & last updated).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Metadata"]
    class_class_curie: ClassVar[str] = "faqir:Metadata"
    class_name: ClassVar[str] = "Metadata"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Metadata

    lastUpdated: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lastUpdated):
            self.MissingRequiredField("lastUpdated")
        if not isinstance(self.lastUpdated, XSDDateTime):
            self.lastUpdated = XSDDateTime(self.lastUpdated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vault(Metadata):
    """
    The FAQIR healthdata vault.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["vault"]
    class_class_curie: ClassVar[str] = "faqir:vault"
    class_name: ClassVar[str] = "Vault"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Vault

    vaultId: Union[str, VaultVaultId] = None
    lastUpdated: Union[str, XSDDateTime] = None
    vaultManagedByOrg: Union[str, OrganizationOrganizationId] = None
    hasQuestionnaireResponse: Optional[Union[Union[str, QuestionnaireResponseQuestionnaireResponseId], list[Union[str, QuestionnaireResponseQuestionnaireResponseId]]]] = empty_list()
    birthdate: Optional[Union[str, XSDDateTime]] = None
    weight: Optional[Union[dict, Weight]] = None
    full_name: Optional[Union[dict, FullName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vaultId):
            self.MissingRequiredField("vaultId")
        if not isinstance(self.vaultId, VaultVaultId):
            self.vaultId = VaultVaultId(self.vaultId)

        if self._is_empty(self.vaultManagedByOrg):
            self.MissingRequiredField("vaultManagedByOrg")
        if not isinstance(self.vaultManagedByOrg, OrganizationOrganizationId):
            self.vaultManagedByOrg = OrganizationOrganizationId(self.vaultManagedByOrg)

        if not isinstance(self.hasQuestionnaireResponse, list):
            self.hasQuestionnaireResponse = [self.hasQuestionnaireResponse] if self.hasQuestionnaireResponse is not None else []
        self.hasQuestionnaireResponse = [v if isinstance(v, QuestionnaireResponseQuestionnaireResponseId) else QuestionnaireResponseQuestionnaireResponseId(v) for v in self.hasQuestionnaireResponse]

        if self.birthdate is not None and not isinstance(self.birthdate, XSDDateTime):
            self.birthdate = XSDDateTime(self.birthdate)

        if self.weight is not None and not isinstance(self.weight, Weight):
            self.weight = Weight(**as_dict(self.weight))

        if self.full_name is not None and not isinstance(self.full_name, FullName):
            self.full_name = FullName(**as_dict(self.full_name))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(YAMLRoot):
    """
    An entity acting in a healthcare context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Organization"]
    class_class_curie: ClassVar[str] = "faqir:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Organization

    organizationId: Union[str, OrganizationOrganizationId] = None
    organizationLabel: str = None
    organizationType: Union[str, "OrganizationType"] = None
    organizationAuthorsQuestionnaire: Optional[Union[Union[str, QuestionnaireQuestionnaireId], list[Union[str, QuestionnaireQuestionnaireId]]]] = empty_list()
    organizationAuthorsSection: Optional[Union[Union[str, SectionSectionId], list[Union[str, SectionSectionId]]]] = empty_list()
    organizationAuthorsQuestion: Optional[Union[Union[str, QuestionQuestionId], list[Union[str, QuestionQuestionId]]]] = empty_list()
    organizationAuthorsScoreDefinition: Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]] = empty_list()
    organizationManagesVault: Optional[Union[Union[str, VaultVaultId], list[Union[str, VaultVaultId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.organizationId):
            self.MissingRequiredField("organizationId")
        if not isinstance(self.organizationId, OrganizationOrganizationId):
            self.organizationId = OrganizationOrganizationId(self.organizationId)

        if self._is_empty(self.organizationLabel):
            self.MissingRequiredField("organizationLabel")
        if not isinstance(self.organizationLabel, str):
            self.organizationLabel = str(self.organizationLabel)

        if self._is_empty(self.organizationType):
            self.MissingRequiredField("organizationType")
        if not isinstance(self.organizationType, OrganizationType):
            self.organizationType = OrganizationType(self.organizationType)

        if not isinstance(self.organizationAuthorsQuestionnaire, list):
            self.organizationAuthorsQuestionnaire = [self.organizationAuthorsQuestionnaire] if self.organizationAuthorsQuestionnaire is not None else []
        self.organizationAuthorsQuestionnaire = [v if isinstance(v, QuestionnaireQuestionnaireId) else QuestionnaireQuestionnaireId(v) for v in self.organizationAuthorsQuestionnaire]

        if not isinstance(self.organizationAuthorsSection, list):
            self.organizationAuthorsSection = [self.organizationAuthorsSection] if self.organizationAuthorsSection is not None else []
        self.organizationAuthorsSection = [v if isinstance(v, SectionSectionId) else SectionSectionId(v) for v in self.organizationAuthorsSection]

        if not isinstance(self.organizationAuthorsQuestion, list):
            self.organizationAuthorsQuestion = [self.organizationAuthorsQuestion] if self.organizationAuthorsQuestion is not None else []
        self.organizationAuthorsQuestion = [v if isinstance(v, QuestionQuestionId) else QuestionQuestionId(v) for v in self.organizationAuthorsQuestion]

        if not isinstance(self.organizationAuthorsScoreDefinition, list):
            self.organizationAuthorsScoreDefinition = [self.organizationAuthorsScoreDefinition] if self.organizationAuthorsScoreDefinition is not None else []
        self.organizationAuthorsScoreDefinition = [v if isinstance(v, ScoreDefinitionScoreDefinitionId) else ScoreDefinitionScoreDefinitionId(v) for v in self.organizationAuthorsScoreDefinition]

        if not isinstance(self.organizationManagesVault, list):
            self.organizationManagesVault = [self.organizationManagesVault] if self.organizationManagesVault is not None else []
        self.organizationManagesVault = [v if isinstance(v, VaultVaultId) else VaultVaultId(v) for v in self.organizationManagesVault]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Procedure(YAMLRoot):
    """
    A clinical or administrative process that uses resources like questionnaires
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Procedure"]
    class_class_curie: ClassVar[str] = "faqir:Procedure"
    class_name: ClassVar[str] = "Procedure"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Procedure

    procedureId: Union[str, ProcedureProcedureId] = None
    procedureLabel: str = None
    procedurePerformedByOrg: Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]] = empty_list()
    procedureHasQuestionnaire: Optional[Union[Union[str, QuestionnaireQuestionnaireId], list[Union[str, QuestionnaireQuestionnaireId]]]] = empty_list()
    procedureDescription: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.procedureId):
            self.MissingRequiredField("procedureId")
        if not isinstance(self.procedureId, ProcedureProcedureId):
            self.procedureId = ProcedureProcedureId(self.procedureId)

        if self._is_empty(self.procedureLabel):
            self.MissingRequiredField("procedureLabel")
        if not isinstance(self.procedureLabel, str):
            self.procedureLabel = str(self.procedureLabel)

        if not isinstance(self.procedurePerformedByOrg, list):
            self.procedurePerformedByOrg = [self.procedurePerformedByOrg] if self.procedurePerformedByOrg is not None else []
        self.procedurePerformedByOrg = [v if isinstance(v, OrganizationOrganizationId) else OrganizationOrganizationId(v) for v in self.procedurePerformedByOrg]

        if not isinstance(self.procedureHasQuestionnaire, list):
            self.procedureHasQuestionnaire = [self.procedureHasQuestionnaire] if self.procedureHasQuestionnaire is not None else []
        self.procedureHasQuestionnaire = [v if isinstance(v, QuestionnaireQuestionnaireId) else QuestionnaireQuestionnaireId(v) for v in self.procedureHasQuestionnaire]

        if self.procedureDescription is not None and not isinstance(self.procedureDescription, str):
            self.procedureDescription = str(self.procedureDescription)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuestionnaireResponse(YAMLRoot):
    """
    A response to a questionnaire (collection of answers).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["QuestionnaireResponse"]
    class_class_curie: ClassVar[str] = "faqir:QuestionnaireResponse"
    class_name: ClassVar[str] = "QuestionnaireResponse"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.QuestionnaireResponse

    questionnaireResponseId: Union[str, QuestionnaireResponseQuestionnaireResponseId] = None
    questionnaireResponseBySubject: Union[str, VaultVaultId] = None
    questionnaireResponseToQuestionnaire: Union[str, QuestionnaireQuestionnaireId] = None
    questionnaireResponseHasAnswer: Union[Union[str, AnswerAnswerId], list[Union[str, AnswerAnswerId]]] = None
    questionnaireResponseStatus: Union[str, "QuestionnaireResponseStatus"] = None
    questionnaireResponseTimeStamp: Union[str, XSDDateTime] = None
    questionnaireResponseLastUpdated: Union[str, XSDDateTime] = None
    questionnaireResponseHasDerivedScoreValue: Optional[Union[Union[str, ScoreValueScoreValueId], list[Union[str, ScoreValueScoreValueId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.questionnaireResponseId):
            self.MissingRequiredField("questionnaireResponseId")
        if not isinstance(self.questionnaireResponseId, QuestionnaireResponseQuestionnaireResponseId):
            self.questionnaireResponseId = QuestionnaireResponseQuestionnaireResponseId(self.questionnaireResponseId)

        if self._is_empty(self.questionnaireResponseBySubject):
            self.MissingRequiredField("questionnaireResponseBySubject")
        if not isinstance(self.questionnaireResponseBySubject, VaultVaultId):
            self.questionnaireResponseBySubject = VaultVaultId(self.questionnaireResponseBySubject)

        if self._is_empty(self.questionnaireResponseToQuestionnaire):
            self.MissingRequiredField("questionnaireResponseToQuestionnaire")
        if not isinstance(self.questionnaireResponseToQuestionnaire, QuestionnaireQuestionnaireId):
            self.questionnaireResponseToQuestionnaire = QuestionnaireQuestionnaireId(self.questionnaireResponseToQuestionnaire)

        if self._is_empty(self.questionnaireResponseHasAnswer):
            self.MissingRequiredField("questionnaireResponseHasAnswer")
        if not isinstance(self.questionnaireResponseHasAnswer, list):
            self.questionnaireResponseHasAnswer = [self.questionnaireResponseHasAnswer] if self.questionnaireResponseHasAnswer is not None else []
        self.questionnaireResponseHasAnswer = [v if isinstance(v, AnswerAnswerId) else AnswerAnswerId(v) for v in self.questionnaireResponseHasAnswer]

        if self._is_empty(self.questionnaireResponseStatus):
            self.MissingRequiredField("questionnaireResponseStatus")
        if not isinstance(self.questionnaireResponseStatus, QuestionnaireResponseStatus):
            self.questionnaireResponseStatus = QuestionnaireResponseStatus(self.questionnaireResponseStatus)

        if self._is_empty(self.questionnaireResponseTimeStamp):
            self.MissingRequiredField("questionnaireResponseTimeStamp")
        if not isinstance(self.questionnaireResponseTimeStamp, XSDDateTime):
            self.questionnaireResponseTimeStamp = XSDDateTime(self.questionnaireResponseTimeStamp)

        if self._is_empty(self.questionnaireResponseLastUpdated):
            self.MissingRequiredField("questionnaireResponseLastUpdated")
        if not isinstance(self.questionnaireResponseLastUpdated, XSDDateTime):
            self.questionnaireResponseLastUpdated = XSDDateTime(self.questionnaireResponseLastUpdated)

        if not isinstance(self.questionnaireResponseHasDerivedScoreValue, list):
            self.questionnaireResponseHasDerivedScoreValue = [self.questionnaireResponseHasDerivedScoreValue] if self.questionnaireResponseHasDerivedScoreValue is not None else []
        self.questionnaireResponseHasDerivedScoreValue = [v if isinstance(v, ScoreValueScoreValueId) else ScoreValueScoreValueId(v) for v in self.questionnaireResponseHasDerivedScoreValue]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Answer(YAMLRoot):
    """
    Answer in the questionnaire response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Answer"]
    class_class_curie: ClassVar[str] = "faqir:Answer"
    class_name: ClassVar[str] = "Answer"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Answer

    answerId: Union[str, AnswerAnswerId] = None
    answerInQuestionnaireResponse: Union[str, QuestionnaireResponseQuestionnaireResponseId] = None
    answerToQuestion: Union[str, QuestionQuestionId] = None
    questionType: Union[str, "QuestionType"] = None
    answerTimeStamp: Union[str, XSDDateTime] = None
    answerValueNumerical: Optional[Union[dict, ValueNumerical]] = None
    answerValueString: Optional[Union[Union[dict, ValueString], list[Union[dict, ValueString]]]] = empty_list()
    answerValueDateTime: Optional[Union[dict, ValueDateTime]] = None
    answerIsEmpty: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.answerId):
            self.MissingRequiredField("answerId")
        if not isinstance(self.answerId, AnswerAnswerId):
            self.answerId = AnswerAnswerId(self.answerId)

        if self._is_empty(self.answerInQuestionnaireResponse):
            self.MissingRequiredField("answerInQuestionnaireResponse")
        if not isinstance(self.answerInQuestionnaireResponse, QuestionnaireResponseQuestionnaireResponseId):
            self.answerInQuestionnaireResponse = QuestionnaireResponseQuestionnaireResponseId(self.answerInQuestionnaireResponse)

        if self._is_empty(self.answerToQuestion):
            self.MissingRequiredField("answerToQuestion")
        if not isinstance(self.answerToQuestion, QuestionQuestionId):
            self.answerToQuestion = QuestionQuestionId(self.answerToQuestion)

        if self._is_empty(self.questionType):
            self.MissingRequiredField("questionType")
        if not isinstance(self.questionType, QuestionType):
            self.questionType = QuestionType(self.questionType)

        if self._is_empty(self.answerTimeStamp):
            self.MissingRequiredField("answerTimeStamp")
        if not isinstance(self.answerTimeStamp, XSDDateTime):
            self.answerTimeStamp = XSDDateTime(self.answerTimeStamp)

        if self.answerValueNumerical is not None and not isinstance(self.answerValueNumerical, ValueNumerical):
            self.answerValueNumerical = ValueNumerical(**as_dict(self.answerValueNumerical))

        self._normalize_inlined_as_dict(slot_name="answerValueString", slot_type=ValueString, key_name="stringValue", keyed=False)

        if self.answerValueDateTime is not None and not isinstance(self.answerValueDateTime, ValueDateTime):
            self.answerValueDateTime = ValueDateTime(**as_dict(self.answerValueDateTime))

        if self.answerIsEmpty is not None and not isinstance(self.answerIsEmpty, Bool):
            self.answerIsEmpty = Bool(self.answerIsEmpty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrderedQuestion(YAMLRoot):
    """
    Question's position within a specific questionnaire or section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["OrderedQuestion"]
    class_class_curie: ClassVar[str] = "faqir:OrderedQuestion"
    class_name: ClassVar[str] = "OrderedQuestion"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.OrderedQuestion

    orderedQuestionId: Union[str, OrderedQuestionOrderedQuestionId] = None
    orderedQuestionHasQuestion: Union[str, QuestionQuestionId] = None
    questionOrder: int = None
    orderedQuestionPartOfQuestionnaire: Optional[Union[str, QuestionnaireQuestionnaireId]] = None
    orderedQuestionPartOfSection: Optional[Union[str, SectionSectionId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.orderedQuestionId):
            self.MissingRequiredField("orderedQuestionId")
        if not isinstance(self.orderedQuestionId, OrderedQuestionOrderedQuestionId):
            self.orderedQuestionId = OrderedQuestionOrderedQuestionId(self.orderedQuestionId)

        if self._is_empty(self.orderedQuestionHasQuestion):
            self.MissingRequiredField("orderedQuestionHasQuestion")
        if not isinstance(self.orderedQuestionHasQuestion, QuestionQuestionId):
            self.orderedQuestionHasQuestion = QuestionQuestionId(self.orderedQuestionHasQuestion)

        if self._is_empty(self.questionOrder):
            self.MissingRequiredField("questionOrder")
        if not isinstance(self.questionOrder, int):
            self.questionOrder = int(self.questionOrder)

        if self.orderedQuestionPartOfQuestionnaire is not None and not isinstance(self.orderedQuestionPartOfQuestionnaire, QuestionnaireQuestionnaireId):
            self.orderedQuestionPartOfQuestionnaire = QuestionnaireQuestionnaireId(self.orderedQuestionPartOfQuestionnaire)

        if self.orderedQuestionPartOfSection is not None and not isinstance(self.orderedQuestionPartOfSection, SectionSectionId):
            self.orderedQuestionPartOfSection = SectionSectionId(self.orderedQuestionPartOfSection)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Question(YAMLRoot):
    """
    A question in the questionnaire.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Question"]
    class_class_curie: ClassVar[str] = "faqir:Question"
    class_name: ClassVar[str] = "Question"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Question

    questionId: Union[str, QuestionQuestionId] = None
    questionType: Union[str, "QuestionType"] = None
    questionTag: str = None
    questionLabel: str = None
    questionAuthoredByOrg: Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]] = empty_list()
    questionInOrderedQuestion: Optional[Union[Union[str, OrderedQuestionOrderedQuestionId], list[Union[str, OrderedQuestionOrderedQuestionId]]]] = empty_list()
    questionHasAnswer: Optional[Union[Union[str, AnswerAnswerId], list[Union[str, AnswerAnswerId]]]] = empty_list()
    questionUsedInScoreDefinition: Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]] = empty_list()
    questionNumericalParams: Optional[Union[dict, NumericalParams]] = None
    questionCodingParams: Optional[Union[Union[dict, ValueCoding], list[Union[dict, ValueCoding]]]] = empty_list()
    questionIntervalParams: Optional[Union[dict, IntervalParams]] = None
    questionRequired: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.questionId):
            self.MissingRequiredField("questionId")
        if not isinstance(self.questionId, QuestionQuestionId):
            self.questionId = QuestionQuestionId(self.questionId)

        if self._is_empty(self.questionType):
            self.MissingRequiredField("questionType")
        if not isinstance(self.questionType, QuestionType):
            self.questionType = QuestionType(self.questionType)

        if self._is_empty(self.questionTag):
            self.MissingRequiredField("questionTag")
        if not isinstance(self.questionTag, str):
            self.questionTag = str(self.questionTag)

        if self._is_empty(self.questionLabel):
            self.MissingRequiredField("questionLabel")
        if not isinstance(self.questionLabel, str):
            self.questionLabel = str(self.questionLabel)

        if not isinstance(self.questionAuthoredByOrg, list):
            self.questionAuthoredByOrg = [self.questionAuthoredByOrg] if self.questionAuthoredByOrg is not None else []
        self.questionAuthoredByOrg = [v if isinstance(v, OrganizationOrganizationId) else OrganizationOrganizationId(v) for v in self.questionAuthoredByOrg]

        if not isinstance(self.questionInOrderedQuestion, list):
            self.questionInOrderedQuestion = [self.questionInOrderedQuestion] if self.questionInOrderedQuestion is not None else []
        self.questionInOrderedQuestion = [v if isinstance(v, OrderedQuestionOrderedQuestionId) else OrderedQuestionOrderedQuestionId(v) for v in self.questionInOrderedQuestion]

        if not isinstance(self.questionHasAnswer, list):
            self.questionHasAnswer = [self.questionHasAnswer] if self.questionHasAnswer is not None else []
        self.questionHasAnswer = [v if isinstance(v, AnswerAnswerId) else AnswerAnswerId(v) for v in self.questionHasAnswer]

        if not isinstance(self.questionUsedInScoreDefinition, list):
            self.questionUsedInScoreDefinition = [self.questionUsedInScoreDefinition] if self.questionUsedInScoreDefinition is not None else []
        self.questionUsedInScoreDefinition = [v if isinstance(v, ScoreDefinitionScoreDefinitionId) else ScoreDefinitionScoreDefinitionId(v) for v in self.questionUsedInScoreDefinition]

        if self.questionNumericalParams is not None and not isinstance(self.questionNumericalParams, NumericalParams):
            self.questionNumericalParams = NumericalParams(**as_dict(self.questionNumericalParams))

        self._normalize_inlined_as_dict(slot_name="questionCodingParams", slot_type=ValueCoding, key_name="code", keyed=False)

        if self.questionIntervalParams is not None and not isinstance(self.questionIntervalParams, IntervalParams):
            self.questionIntervalParams = IntervalParams(**as_dict(self.questionIntervalParams))

        if self.questionRequired is not None and not isinstance(self.questionRequired, Bool):
            self.questionRequired = Bool(self.questionRequired)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Questionnaire(YAMLRoot):
    """
    A questionnaire that can be answered (collection of questions).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Questionnaire"]
    class_class_curie: ClassVar[str] = "faqir:Questionnaire"
    class_name: ClassVar[str] = "Questionnaire"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Questionnaire

    questionnaireId: Union[str, QuestionnaireQuestionnaireId] = None
    questionnaireLabel: str = None
    questionnaireStatus: Union[str, "QuestionnaireStatus"] = None
    questionnaireVersion: str = None
    questionnaireLastUpdated: Union[str, XSDDateTime] = None
    questionnaireHasQuestionnaireResponse: Optional[Union[Union[str, QuestionnaireResponseQuestionnaireResponseId], list[Union[str, QuestionnaireResponseQuestionnaireResponseId]]]] = empty_list()
    questionnaireHasOrderedQuestion: Optional[Union[dict[Union[str, OrderedQuestionOrderedQuestionId], Union[dict, OrderedQuestion]], list[Union[dict, OrderedQuestion]]]] = empty_dict()
    questionnaireHasOrderedSection: Optional[Union[dict[Union[str, OrderedSectionOrderedSectionId], Union[dict, "OrderedSection"]], list[Union[dict, "OrderedSection"]]]] = empty_dict()
    questionnaireUsesScoreDefinition: Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]] = empty_list()
    questionnaireAuthoredByOrg: Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]] = empty_list()
    questionnairePartOfProcedure: Optional[Union[Union[str, ProcedureProcedureId], list[Union[str, ProcedureProcedureId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.questionnaireId):
            self.MissingRequiredField("questionnaireId")
        if not isinstance(self.questionnaireId, QuestionnaireQuestionnaireId):
            self.questionnaireId = QuestionnaireQuestionnaireId(self.questionnaireId)

        if self._is_empty(self.questionnaireLabel):
            self.MissingRequiredField("questionnaireLabel")
        if not isinstance(self.questionnaireLabel, str):
            self.questionnaireLabel = str(self.questionnaireLabel)

        if self._is_empty(self.questionnaireStatus):
            self.MissingRequiredField("questionnaireStatus")
        if not isinstance(self.questionnaireStatus, QuestionnaireStatus):
            self.questionnaireStatus = QuestionnaireStatus(self.questionnaireStatus)

        if self._is_empty(self.questionnaireVersion):
            self.MissingRequiredField("questionnaireVersion")
        if not isinstance(self.questionnaireVersion, str):
            self.questionnaireVersion = str(self.questionnaireVersion)

        if self._is_empty(self.questionnaireLastUpdated):
            self.MissingRequiredField("questionnaireLastUpdated")
        if not isinstance(self.questionnaireLastUpdated, XSDDateTime):
            self.questionnaireLastUpdated = XSDDateTime(self.questionnaireLastUpdated)

        if not isinstance(self.questionnaireHasQuestionnaireResponse, list):
            self.questionnaireHasQuestionnaireResponse = [self.questionnaireHasQuestionnaireResponse] if self.questionnaireHasQuestionnaireResponse is not None else []
        self.questionnaireHasQuestionnaireResponse = [v if isinstance(v, QuestionnaireResponseQuestionnaireResponseId) else QuestionnaireResponseQuestionnaireResponseId(v) for v in self.questionnaireHasQuestionnaireResponse]

        self._normalize_inlined_as_list(slot_name="questionnaireHasOrderedQuestion", slot_type=OrderedQuestion, key_name="orderedQuestionId", keyed=True)

        self._normalize_inlined_as_list(slot_name="questionnaireHasOrderedSection", slot_type=OrderedSection, key_name="orderedSectionId", keyed=True)

        if not isinstance(self.questionnaireUsesScoreDefinition, list):
            self.questionnaireUsesScoreDefinition = [self.questionnaireUsesScoreDefinition] if self.questionnaireUsesScoreDefinition is not None else []
        self.questionnaireUsesScoreDefinition = [v if isinstance(v, ScoreDefinitionScoreDefinitionId) else ScoreDefinitionScoreDefinitionId(v) for v in self.questionnaireUsesScoreDefinition]

        if not isinstance(self.questionnaireAuthoredByOrg, list):
            self.questionnaireAuthoredByOrg = [self.questionnaireAuthoredByOrg] if self.questionnaireAuthoredByOrg is not None else []
        self.questionnaireAuthoredByOrg = [v if isinstance(v, OrganizationOrganizationId) else OrganizationOrganizationId(v) for v in self.questionnaireAuthoredByOrg]

        if not isinstance(self.questionnairePartOfProcedure, list):
            self.questionnairePartOfProcedure = [self.questionnairePartOfProcedure] if self.questionnairePartOfProcedure is not None else []
        self.questionnairePartOfProcedure = [v if isinstance(v, ProcedureProcedureId) else ProcedureProcedureId(v) for v in self.questionnairePartOfProcedure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrderedSection(YAMLRoot):
    """
    Section's position within a specific questionnaire or section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["OrderedSection"]
    class_class_curie: ClassVar[str] = "faqir:OrderedSection"
    class_name: ClassVar[str] = "OrderedSection"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.OrderedSection

    orderedSectionId: Union[str, OrderedSectionOrderedSectionId] = None
    orderedSectionHasSection: Union[str, SectionSectionId] = None
    sectionOrder: int = None
    orderedSectionPartOfQuestionnaire: Optional[Union[str, QuestionnaireQuestionnaireId]] = None
    orderedSectionPartOfSection: Optional[Union[str, SectionSectionId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.orderedSectionId):
            self.MissingRequiredField("orderedSectionId")
        if not isinstance(self.orderedSectionId, OrderedSectionOrderedSectionId):
            self.orderedSectionId = OrderedSectionOrderedSectionId(self.orderedSectionId)

        if self._is_empty(self.orderedSectionHasSection):
            self.MissingRequiredField("orderedSectionHasSection")
        if not isinstance(self.orderedSectionHasSection, SectionSectionId):
            self.orderedSectionHasSection = SectionSectionId(self.orderedSectionHasSection)

        if self._is_empty(self.sectionOrder):
            self.MissingRequiredField("sectionOrder")
        if not isinstance(self.sectionOrder, int):
            self.sectionOrder = int(self.sectionOrder)

        if self.orderedSectionPartOfQuestionnaire is not None and not isinstance(self.orderedSectionPartOfQuestionnaire, QuestionnaireQuestionnaireId):
            self.orderedSectionPartOfQuestionnaire = QuestionnaireQuestionnaireId(self.orderedSectionPartOfQuestionnaire)

        if self.orderedSectionPartOfSection is not None and not isinstance(self.orderedSectionPartOfSection, SectionSectionId):
            self.orderedSectionPartOfSection = SectionSectionId(self.orderedSectionPartOfSection)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Section(YAMLRoot):
    """
    A section of questions in the questionnaire.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["Section"]
    class_class_curie: ClassVar[str] = "faqir:Section"
    class_name: ClassVar[str] = "Section"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.Section

    sectionId: Union[str, SectionSectionId] = None
    sectionLabel: str = None
    sectionHasOrderedQuestion: Optional[Union[dict[Union[str, OrderedQuestionOrderedQuestionId], Union[dict, OrderedQuestion]], list[Union[dict, OrderedQuestion]]]] = empty_dict()
    sectionHasOrderedSection: Optional[Union[dict[Union[str, OrderedSectionOrderedSectionId], Union[dict, OrderedSection]], list[Union[dict, OrderedSection]]]] = empty_dict()
    sectionInOrderedSection: Optional[Union[Union[str, OrderedSectionOrderedSectionId], list[Union[str, OrderedSectionOrderedSectionId]]]] = empty_list()
    sectionUsesScoreDefinition: Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]] = empty_list()
    sectionAuthoredByOrg: Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sectionId):
            self.MissingRequiredField("sectionId")
        if not isinstance(self.sectionId, SectionSectionId):
            self.sectionId = SectionSectionId(self.sectionId)

        if self._is_empty(self.sectionLabel):
            self.MissingRequiredField("sectionLabel")
        if not isinstance(self.sectionLabel, str):
            self.sectionLabel = str(self.sectionLabel)

        self._normalize_inlined_as_list(slot_name="sectionHasOrderedQuestion", slot_type=OrderedQuestion, key_name="orderedQuestionId", keyed=True)

        self._normalize_inlined_as_list(slot_name="sectionHasOrderedSection", slot_type=OrderedSection, key_name="orderedSectionId", keyed=True)

        if not isinstance(self.sectionInOrderedSection, list):
            self.sectionInOrderedSection = [self.sectionInOrderedSection] if self.sectionInOrderedSection is not None else []
        self.sectionInOrderedSection = [v if isinstance(v, OrderedSectionOrderedSectionId) else OrderedSectionOrderedSectionId(v) for v in self.sectionInOrderedSection]

        if not isinstance(self.sectionUsesScoreDefinition, list):
            self.sectionUsesScoreDefinition = [self.sectionUsesScoreDefinition] if self.sectionUsesScoreDefinition is not None else []
        self.sectionUsesScoreDefinition = [v if isinstance(v, ScoreDefinitionScoreDefinitionId) else ScoreDefinitionScoreDefinitionId(v) for v in self.sectionUsesScoreDefinition]

        if not isinstance(self.sectionAuthoredByOrg, list):
            self.sectionAuthoredByOrg = [self.sectionAuthoredByOrg] if self.sectionAuthoredByOrg is not None else []
        self.sectionAuthoredByOrg = [v if isinstance(v, OrganizationOrganizationId) else OrganizationOrganizationId(v) for v in self.sectionAuthoredByOrg]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScoreDefinition(YAMLRoot):
    """
    A score calculated from questions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ScoreDefinition"]
    class_class_curie: ClassVar[str] = "faqir:ScoreDefinition"
    class_name: ClassVar[str] = "ScoreDefinition"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ScoreDefinition

    scoreDefinitionId: Union[str, ScoreDefinitionScoreDefinitionId] = None
    scoreDefinitionType: Union[str, "ScoreType"] = None
    scoreDefinitionUsesQuestion: Union[Union[str, QuestionQuestionId], list[Union[str, QuestionQuestionId]]] = None
    scoreDefinitionLabel: str = None
    scoreDefinitionFormula: str = None
    scoreDefinitionHasScoreParameter: Optional[Union[Union[str, ScoreParameterScoreParameterId], list[Union[str, ScoreParameterScoreParameterId]]]] = empty_list()
    scoreDefinitionHasScoreValue: Optional[Union[Union[str, ScoreValueScoreValueId], list[Union[str, ScoreValueScoreValueId]]]] = empty_list()
    scoreDefinitionAuthoredByOrg: Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]] = empty_list()
    scoreDefinitionUsedByQuestionnare: Optional[Union[Union[str, QuestionnaireQuestionnaireId], list[Union[str, QuestionnaireQuestionnaireId]]]] = empty_list()
    scoreDefinitionUsedBySection: Optional[Union[Union[str, SectionSectionId], list[Union[str, SectionSectionId]]]] = empty_list()
    scoreDefinitionIntervalParams: Optional[Union[dict, IntervalParams]] = None
    scoreDefinitionCategories: Optional[Union[str, list[str]]] = empty_list()
    scoreDefinitionInterpretationGuide: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scoreDefinitionId):
            self.MissingRequiredField("scoreDefinitionId")
        if not isinstance(self.scoreDefinitionId, ScoreDefinitionScoreDefinitionId):
            self.scoreDefinitionId = ScoreDefinitionScoreDefinitionId(self.scoreDefinitionId)

        if self._is_empty(self.scoreDefinitionType):
            self.MissingRequiredField("scoreDefinitionType")
        if not isinstance(self.scoreDefinitionType, ScoreType):
            self.scoreDefinitionType = ScoreType(self.scoreDefinitionType)

        if self._is_empty(self.scoreDefinitionUsesQuestion):
            self.MissingRequiredField("scoreDefinitionUsesQuestion")
        if not isinstance(self.scoreDefinitionUsesQuestion, list):
            self.scoreDefinitionUsesQuestion = [self.scoreDefinitionUsesQuestion] if self.scoreDefinitionUsesQuestion is not None else []
        self.scoreDefinitionUsesQuestion = [v if isinstance(v, QuestionQuestionId) else QuestionQuestionId(v) for v in self.scoreDefinitionUsesQuestion]

        if self._is_empty(self.scoreDefinitionLabel):
            self.MissingRequiredField("scoreDefinitionLabel")
        if not isinstance(self.scoreDefinitionLabel, str):
            self.scoreDefinitionLabel = str(self.scoreDefinitionLabel)

        if self._is_empty(self.scoreDefinitionFormula):
            self.MissingRequiredField("scoreDefinitionFormula")
        if not isinstance(self.scoreDefinitionFormula, str):
            self.scoreDefinitionFormula = str(self.scoreDefinitionFormula)

        if not isinstance(self.scoreDefinitionHasScoreParameter, list):
            self.scoreDefinitionHasScoreParameter = [self.scoreDefinitionHasScoreParameter] if self.scoreDefinitionHasScoreParameter is not None else []
        self.scoreDefinitionHasScoreParameter = [v if isinstance(v, ScoreParameterScoreParameterId) else ScoreParameterScoreParameterId(v) for v in self.scoreDefinitionHasScoreParameter]

        if not isinstance(self.scoreDefinitionHasScoreValue, list):
            self.scoreDefinitionHasScoreValue = [self.scoreDefinitionHasScoreValue] if self.scoreDefinitionHasScoreValue is not None else []
        self.scoreDefinitionHasScoreValue = [v if isinstance(v, ScoreValueScoreValueId) else ScoreValueScoreValueId(v) for v in self.scoreDefinitionHasScoreValue]

        if not isinstance(self.scoreDefinitionAuthoredByOrg, list):
            self.scoreDefinitionAuthoredByOrg = [self.scoreDefinitionAuthoredByOrg] if self.scoreDefinitionAuthoredByOrg is not None else []
        self.scoreDefinitionAuthoredByOrg = [v if isinstance(v, OrganizationOrganizationId) else OrganizationOrganizationId(v) for v in self.scoreDefinitionAuthoredByOrg]

        if not isinstance(self.scoreDefinitionUsedByQuestionnare, list):
            self.scoreDefinitionUsedByQuestionnare = [self.scoreDefinitionUsedByQuestionnare] if self.scoreDefinitionUsedByQuestionnare is not None else []
        self.scoreDefinitionUsedByQuestionnare = [v if isinstance(v, QuestionnaireQuestionnaireId) else QuestionnaireQuestionnaireId(v) for v in self.scoreDefinitionUsedByQuestionnare]

        if not isinstance(self.scoreDefinitionUsedBySection, list):
            self.scoreDefinitionUsedBySection = [self.scoreDefinitionUsedBySection] if self.scoreDefinitionUsedBySection is not None else []
        self.scoreDefinitionUsedBySection = [v if isinstance(v, SectionSectionId) else SectionSectionId(v) for v in self.scoreDefinitionUsedBySection]

        if self.scoreDefinitionIntervalParams is not None and not isinstance(self.scoreDefinitionIntervalParams, IntervalParams):
            self.scoreDefinitionIntervalParams = IntervalParams(**as_dict(self.scoreDefinitionIntervalParams))

        if not isinstance(self.scoreDefinitionCategories, list):
            self.scoreDefinitionCategories = [self.scoreDefinitionCategories] if self.scoreDefinitionCategories is not None else []
        self.scoreDefinitionCategories = [v if isinstance(v, str) else str(v) for v in self.scoreDefinitionCategories]

        if self.scoreDefinitionInterpretationGuide is not None and not isinstance(self.scoreDefinitionInterpretationGuide, str):
            self.scoreDefinitionInterpretationGuide = str(self.scoreDefinitionInterpretationGuide)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScoreParameter(YAMLRoot):
    """
    Parameters for score definitions, such as min/max values, categories or constants needed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ScoreParameter"]
    class_class_curie: ClassVar[str] = "faqir:ScoreParameter"
    class_name: ClassVar[str] = "ScoreParameter"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ScoreParameter

    scoreParameterId: Union[str, ScoreParameterScoreParameterId] = None
    scoreParameterPartOfScoreDefinition: Union[str, ScoreDefinitionScoreDefinitionId] = None
    scoreParameterLabel: str = None
    scoreParameterType: Union[str, "ScoreParameterType"] = None
    scoreParameterValueNumerical: Optional[Union[dict, ValueNumerical]] = None
    scoreParameterValueDateTime: Optional[Union[dict, ValueDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scoreParameterId):
            self.MissingRequiredField("scoreParameterId")
        if not isinstance(self.scoreParameterId, ScoreParameterScoreParameterId):
            self.scoreParameterId = ScoreParameterScoreParameterId(self.scoreParameterId)

        if self._is_empty(self.scoreParameterPartOfScoreDefinition):
            self.MissingRequiredField("scoreParameterPartOfScoreDefinition")
        if not isinstance(self.scoreParameterPartOfScoreDefinition, ScoreDefinitionScoreDefinitionId):
            self.scoreParameterPartOfScoreDefinition = ScoreDefinitionScoreDefinitionId(self.scoreParameterPartOfScoreDefinition)

        if self._is_empty(self.scoreParameterLabel):
            self.MissingRequiredField("scoreParameterLabel")
        if not isinstance(self.scoreParameterLabel, str):
            self.scoreParameterLabel = str(self.scoreParameterLabel)

        if self._is_empty(self.scoreParameterType):
            self.MissingRequiredField("scoreParameterType")
        if not isinstance(self.scoreParameterType, ScoreParameterType):
            self.scoreParameterType = ScoreParameterType(self.scoreParameterType)

        if self.scoreParameterValueNumerical is not None and not isinstance(self.scoreParameterValueNumerical, ValueNumerical):
            self.scoreParameterValueNumerical = ValueNumerical(**as_dict(self.scoreParameterValueNumerical))

        if self.scoreParameterValueDateTime is not None and not isinstance(self.scoreParameterValueDateTime, ValueDateTime):
            self.scoreParameterValueDateTime = ValueDateTime(**as_dict(self.scoreParameterValueDateTime))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScoreValue(YAMLRoot):
    """
    The score value calculated from a QuestionnaireResponse following a ScoreDefinition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAQIR["ScoreValue"]
    class_class_curie: ClassVar[str] = "faqir:ScoreValue"
    class_name: ClassVar[str] = "ScoreValue"
    class_model_uri: ClassVar[URIRef] = DATAMODEL.ScoreValue

    scoreValueId: Union[str, ScoreValueScoreValueId] = None
    scoreDefinitionType: Union[str, "ScoreType"] = None
    scoreValueBasedOnScoreDefinition: Union[str, ScoreDefinitionScoreDefinitionId] = None
    scoreValueDerivedFromQuestionnaireResponse: Union[Union[str, QuestionnaireResponseQuestionnaireResponseId], list[Union[str, QuestionnaireResponseQuestionnaireResponseId]]] = None
    scoreValueTimeStamp: Union[str, XSDDateTime] = None
    scoreValueStatus: Union[str, "ScoreValueStatus"] = None
    scoreValueString: Optional[Union[dict, ValueString]] = None
    scoreValueNumerical: Optional[Union[dict, ValueNumerical]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scoreValueId):
            self.MissingRequiredField("scoreValueId")
        if not isinstance(self.scoreValueId, ScoreValueScoreValueId):
            self.scoreValueId = ScoreValueScoreValueId(self.scoreValueId)

        if self._is_empty(self.scoreDefinitionType):
            self.MissingRequiredField("scoreDefinitionType")
        if not isinstance(self.scoreDefinitionType, ScoreType):
            self.scoreDefinitionType = ScoreType(self.scoreDefinitionType)

        if self._is_empty(self.scoreValueBasedOnScoreDefinition):
            self.MissingRequiredField("scoreValueBasedOnScoreDefinition")
        if not isinstance(self.scoreValueBasedOnScoreDefinition, ScoreDefinitionScoreDefinitionId):
            self.scoreValueBasedOnScoreDefinition = ScoreDefinitionScoreDefinitionId(self.scoreValueBasedOnScoreDefinition)

        if self._is_empty(self.scoreValueDerivedFromQuestionnaireResponse):
            self.MissingRequiredField("scoreValueDerivedFromQuestionnaireResponse")
        if not isinstance(self.scoreValueDerivedFromQuestionnaireResponse, list):
            self.scoreValueDerivedFromQuestionnaireResponse = [self.scoreValueDerivedFromQuestionnaireResponse] if self.scoreValueDerivedFromQuestionnaireResponse is not None else []
        self.scoreValueDerivedFromQuestionnaireResponse = [v if isinstance(v, QuestionnaireResponseQuestionnaireResponseId) else QuestionnaireResponseQuestionnaireResponseId(v) for v in self.scoreValueDerivedFromQuestionnaireResponse]

        if self._is_empty(self.scoreValueTimeStamp):
            self.MissingRequiredField("scoreValueTimeStamp")
        if not isinstance(self.scoreValueTimeStamp, XSDDateTime):
            self.scoreValueTimeStamp = XSDDateTime(self.scoreValueTimeStamp)

        if self._is_empty(self.scoreValueStatus):
            self.MissingRequiredField("scoreValueStatus")
        if not isinstance(self.scoreValueStatus, ScoreValueStatus):
            self.scoreValueStatus = ScoreValueStatus(self.scoreValueStatus)

        if self.scoreValueString is not None and not isinstance(self.scoreValueString, ValueString):
            self.scoreValueString = ValueString(**as_dict(self.scoreValueString))

        if self.scoreValueNumerical is not None and not isinstance(self.scoreValueNumerical, ValueNumerical):
            self.scoreValueNumerical = ValueNumerical(**as_dict(self.scoreValueNumerical))

        super().__post_init__(**kwargs)


# Enumerations
class WeightType(EnumDefinitionImpl):
    """
    Allowed LOINC codes for weight.
    """
    BODY_WEIGHT_MEASURED = PermissibleValue(
        text="BODY_WEIGHT_MEASURED",
        description="Body weight measured",
        meaning=LOINC["3141-9"])
    BODY_WEIGHT_STATED = PermissibleValue(
        text="BODY_WEIGHT_STATED",
        description="Body weight Stated",
        meaning=LOINC["3142-7"])

    _defn = EnumDefinition(
        name="WeightType",
        description="Allowed LOINC codes for weight.",
    )

class MassUnit(EnumDefinitionImpl):
    """
    Allowed units from UCUM standard for mass.
    """
    kg = PermissibleValue(
        text="kg",
        description="Kilogram",
        meaning=UCUM["kg"])

    _defn = EnumDefinition(
        name="MassUnit",
        description="Allowed units from UCUM standard for mass.",
    )

class UnitOfMeasure(EnumDefinitionImpl):
    """
    Allowed units from UCUM standard.
    """
    kg = PermissibleValue(
        text="kg",
        description="Kilograms",
        meaning=UCUM["kg"])
    g = PermissibleValue(
        text="g",
        description="Grams",
        meaning=UCUM["g"])
    lb = PermissibleValue(
        text="lb",
        description="Pounds",
        meaning=UCUM["lb_av"])
    cm = PermissibleValue(
        text="cm",
        description="Centimeters",
        meaning=UCUM["cm"])
    m = PermissibleValue(
        text="m",
        description="Meters",
        meaning=UCUM["m"])
    h = PermissibleValue(
        text="h",
        description="Hours",
        meaning=UCUM["h"])
    min = PermissibleValue(
        text="min",
        description="Minutes",
        meaning=UCUM["min"])

    _defn = EnumDefinition(
        name="UnitOfMeasure",
        description="Allowed units from UCUM standard.",
    )

class OrganizationType(EnumDefinitionImpl):
    """
    Type of organization: hospital, government, professional, research or serviceProvider.
    """
    hospital = PermissibleValue(
        text="hospital",
        meaning=FHIR["organization-type#prov"])
    government = PermissibleValue(
        text="government",
        meaning=FHIR["organization-type#gov"])
    professional = PermissibleValue(
        text="professional",
        meaning=FHIR["organization-type#ind"])
    research = PermissibleValue(
        text="research",
        meaning=FHIR["organization-type#edu"])
    serviceProvider = PermissibleValue(
        text="serviceProvider",
        meaning=FHIR["organization-type#bus"])

    _defn = EnumDefinition(
        name="OrganizationType",
        description="Type of organization: hospital, government, professional, research or serviceProvider.",
    )

class QuestionType(EnumDefinitionImpl):
    """
    The type of question asked in the questionnaire. It defines the expected answer format.
    """
    choice = PermissibleValue(
        text="choice",
        description="A question with predefined options to choose from. Multiple choices may be allowed.",
        meaning=FHIR["choice"])
    openChoice = PermissibleValue(
        text="openChoice",
        description="""A question with predefined options to choose from plus a last {valueCoding: {'code': '-1', 'display': 'Other'}} that allows text input. Multiple choices may be allowed.""",
        meaning=FHIR["open-choice"])
    numberInterval = PermissibleValue(
        text="numberInterval",
        description="A question that expects a numeric answer in between a minimum and maximum value.",
        meaning=FHIR["number"])
    decimal = PermissibleValue(
        text="decimal",
        description="A question that expects a numerical answer, either integer or float.",
        meaning=FHIR["decimal"])
    dateTime = PermissibleValue(
        text="dateTime",
        description="A question that expects a dateTime answer, formatted as YYYY-MM-DDThh:mm:ss+zz:zz.",
        meaning=FHIR["dateTime"])
    text = PermissibleValue(
        text="text",
        description="A question that expects a free text answer.",
        meaning=FHIR["string"])

    _defn = EnumDefinition(
        name="QuestionType",
        description="The type of question asked in the questionnaire. It defines the expected answer format.",
    )

class ScoreType(EnumDefinitionImpl):
    """
    The type of score definition, which can be numerical or categorical.
    """
    numerical_continuous = PermissibleValue(
        text="numerical_continuous",
        description="Continuous numerical score (e.g., 0.785, 82.5)",
        meaning=XSD["float"])
    numerical_integer = PermissibleValue(
        text="numerical_integer",
        description="Integer numerical score (e.g., 5, 10, 27)",
        meaning=XSD["integer"])
    numerical_percentage = PermissibleValue(
        text="numerical_percentage",
        description="Percentage score (0-100%)",
        meaning=XSD["float"])
    numerical_z_score = PermissibleValue(
        text="numerical_z_score",
        description="Standardized Z-score (mean=0, std=1)",
        meaning=XSD["float"])
    numerical_t_score = PermissibleValue(
        text="numerical_t_score",
        description="Standardized T-score (mean=50, std=10)",
        meaning=XSD["float"])
    categorical = PermissibleValue(
        text="categorical",
        description="Ordinal categories (e.g., Low, Medium, High or Yes, No or Type a, Type b)",
        meaning=XSD["NMTOKENS"])

    _defn = EnumDefinition(
        name="ScoreType",
        description="The type of score definition, which can be numerical or categorical.",
    )

class ScoreParameterType(EnumDefinitionImpl):
    """
    The type of parameter used in the score definition.
    """
    numerical = PermissibleValue(
        text="numerical",
        description="Numerical parameter (e.g., 0.785, 82)",
        meaning=XSD["float"])
    dateTime = PermissibleValue(
        text="dateTime",
        description="dateTime parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz.",
        meaning=XSD["dateTime"])

    _defn = EnumDefinition(
        name="ScoreParameterType",
        description="The type of parameter used in the score definition.",
    )

class QuestionnaireStatus(EnumDefinitionImpl):
    """
    Questionnaires must have one of the following status (FHIR inspired):
    """
    draft = PermissibleValue(
        text="draft",
        description="This resource is still under development and is not yet considered to be ready for normal use.",
        meaning=FHIR["resource-status-draft"])
    active = PermissibleValue(
        text="active",
        description="This resource is ready for normal use.",
        meaning=FHIR["resource-status-active"])
    retired = PermissibleValue(
        text="retired",
        description="This resource has been withdrawn or superseded and should no longer be used.",
        meaning=FHIR["resource-status-retired"])
    unknown = PermissibleValue(
        text="unknown",
        description="""The authoring system does not know which of the status values currently applies for this resource. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, it's just not known which one.""",
        meaning=FHIR["resource-status-unknown"])

    _defn = EnumDefinition(
        name="QuestionnaireStatus",
        description="Questionnaires must have one of the following status (FHIR inspired):",
    )

class QuestionnaireResponseStatus(EnumDefinitionImpl):
    """
    The quesionnaire response status must be one of the following: 'in-progress', 'completed', 'amended',
    'entered-in-error' or 'stopped'.
    """
    in_progress = PermissibleValue(
        text="in_progress",
        description="""This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it.""",
        meaning=FHIR["questionnaire-answers-status-in-progress"])
    completed = PermissibleValue(
        text="completed",
        description="""This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.""",
        meaning=FHIR["questionnaire-answers-status-completed"])
    amended = PermissibleValue(
        text="amended",
        description="""This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards.""",
        meaning=FHIR["questionnaire-answers-status-amended"])
    entered_in_error = PermissibleValue(
        text="entered_in_error",
        description="This QuestionnaireResponse was entered in error and voided.",
        meaning=FHIR["questionnaire-answers-status-entered-in-error"])
    stopped = PermissibleValue(
        text="stopped",
        description="""This QuestionnaireResponse has been partially filled out with answers but has been abandoned. No subsequent changes can be made.""",
        meaning=FHIR["questionnaire-answers-status-stopped"])

    _defn = EnumDefinition(
        name="QuestionnaireResponseStatus",
        description="""The quesionnaire response status must be one of the following: 'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.""",
    )

class ScoreValueStatus(EnumDefinitionImpl):
    """
    The status of a score value, indicating its validity and completeness.
    """
    valid = PermissibleValue(
        text="valid",
        description="Score is valid and complete")
    incomplete = PermissibleValue(
        text="incomplete",
        description="Score calculated with missing optional data")
    estimated = PermissibleValue(
        text="estimated",
        description="Score is an estimate due to missing data")
    warning = PermissibleValue(
        text="warning",
        description="Score calculated with warnings or anomalies")
    error = PermissibleValue(
        text="error",
        description="Score calculation error or invalid data")
    pending = PermissibleValue(
        text="pending",
        description="Score calculation is pending")
    amended = PermissibleValue(
        text="amended",
        description="Score has been amended after initial calculation")

    _defn = EnumDefinition(
        name="ScoreValueStatus",
        description="The status of a score value, indicating its validity and completeness.",
    )

# Slots
class slots:
    pass

slots.hasQuestionnaireResponse = Slot(uri=DATAMODEL['vault/hasQuestionnaireResponse'], name="hasQuestionnaireResponse", curie=DATAMODEL.curie('vault/hasQuestionnaireResponse'),
                   model_uri=DATAMODEL.hasQuestionnaireResponse, domain=Vault, range=Optional[Union[Union[str, QuestionnaireResponseQuestionnaireResponseId], list[Union[str, QuestionnaireResponseQuestionnaireResponseId]]]])

slots.vaultManagedByOrg = Slot(uri=DATAMODEL['vault/vaultManagedByOrg'], name="vaultManagedByOrg", curie=DATAMODEL.curie('vault/vaultManagedByOrg'),
                   model_uri=DATAMODEL.vaultManagedByOrg, domain=Vault, range=Union[str, OrganizationOrganizationId])

slots.id = Slot(uri=FAQIR.id, name="id", curie=FAQIR.curie('id'),
                   model_uri=DATAMODEL.id, domain=None, range=URIRef)

slots.organizationAuthorsQuestionnaire = Slot(uri=FAQIR.organizationAuthorsQuestionnaire, name="organizationAuthorsQuestionnaire", curie=FAQIR.curie('organizationAuthorsQuestionnaire'),
                   model_uri=DATAMODEL.organizationAuthorsQuestionnaire, domain=Organization, range=Optional[Union[Union[str, QuestionnaireQuestionnaireId], list[Union[str, QuestionnaireQuestionnaireId]]]], mappings = [PROV["wasAssociatedWith"]])

slots.organizationAuthorsSection = Slot(uri=FAQIR.organizationAuthorsSection, name="organizationAuthorsSection", curie=FAQIR.curie('organizationAuthorsSection'),
                   model_uri=DATAMODEL.organizationAuthorsSection, domain=Organization, range=Optional[Union[Union[str, SectionSectionId], list[Union[str, SectionSectionId]]]], mappings = [PROV["wasAssociatedWith"]])

slots.organizationAuthorsQuestion = Slot(uri=FAQIR.organizationAuthorsQuestion, name="organizationAuthorsQuestion", curie=FAQIR.curie('organizationAuthorsQuestion'),
                   model_uri=DATAMODEL.organizationAuthorsQuestion, domain=Organization, range=Optional[Union[Union[str, QuestionQuestionId], list[Union[str, QuestionQuestionId]]]], mappings = [PROV["wasAssociatedWith"]])

slots.organizationAuthorsScoreDefinition = Slot(uri=FAQIR.organizationAuthorsScoreDefinition, name="organizationAuthorsScoreDefinition", curie=FAQIR.curie('organizationAuthorsScoreDefinition'),
                   model_uri=DATAMODEL.organizationAuthorsScoreDefinition, domain=Organization, range=Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]], mappings = [PROV["wasAssociatedWith"]])

slots.organizationManagesVault = Slot(uri=FAQIR.organizationManagesVault, name="organizationManagesVault", curie=FAQIR.curie('organizationManagesVault'),
                   model_uri=DATAMODEL.organizationManagesVault, domain=Organization, range=Optional[Union[Union[str, VaultVaultId], list[Union[str, VaultVaultId]]]])

slots.organizationPerformsProcedure = Slot(uri=FAQIR.organizationPerformsProcedure, name="organizationPerformsProcedure", curie=FAQIR.curie('organizationPerformsProcedure'),
                   model_uri=DATAMODEL.organizationPerformsProcedure, domain=Organization, range=Optional[Union[Union[str, ProcedureProcedureId], list[Union[str, ProcedureProcedureId]]]])

slots.procedurePerformedByOrg = Slot(uri=FAQIR.procedurePerformedByOrg, name="procedurePerformedByOrg", curie=FAQIR.curie('procedurePerformedByOrg'),
                   model_uri=DATAMODEL.procedurePerformedByOrg, domain=Procedure, range=Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]])

slots.procedureHasQuestionnaire = Slot(uri=FAQIR.procedureHasQuestionnaire, name="procedureHasQuestionnaire", curie=FAQIR.curie('procedureHasQuestionnaire'),
                   model_uri=DATAMODEL.procedureHasQuestionnaire, domain=Procedure, range=Optional[Union[Union[str, QuestionnaireQuestionnaireId], list[Union[str, QuestionnaireQuestionnaireId]]]])

slots.questionType = Slot(uri=FAQIR.questionType, name="questionType", curie=FAQIR.curie('questionType'),
                   model_uri=DATAMODEL.questionType, domain=None, range=Union[str, "QuestionType"])

slots.scoreDefinitionType = Slot(uri=FAQIR.scoreDefinitionType, name="scoreDefinitionType", curie=FAQIR.curie('scoreDefinitionType'),
                   model_uri=DATAMODEL.scoreDefinitionType, domain=None, range=Union[str, "ScoreType"])

slots.questionnaireResponseBySubject = Slot(uri=FAQIR.questionnaireResponseBySubject, name="questionnaireResponseBySubject", curie=FAQIR.curie('questionnaireResponseBySubject'),
                   model_uri=DATAMODEL.questionnaireResponseBySubject, domain=QuestionnaireResponse, range=Union[str, VaultVaultId], mappings = [FHIR["questionnaireResponse.subject"]])

slots.questionnaireResponseToQuestionnaire = Slot(uri=FAQIR.questionnaireResponseToQuestionnaire, name="questionnaireResponseToQuestionnaire", curie=FAQIR.curie('questionnaireResponseToQuestionnaire'),
                   model_uri=DATAMODEL.questionnaireResponseToQuestionnaire, domain=QuestionnaireResponse, range=Union[str, QuestionnaireQuestionnaireId], mappings = [FHIR["questionnaireResponse.questionnaire"]])

slots.questionnaireResponseHasAnswer = Slot(uri=FAQIR.questionnaireResponseHasAnswer, name="questionnaireResponseHasAnswer", curie=FAQIR.curie('questionnaireResponseHasAnswer'),
                   model_uri=DATAMODEL.questionnaireResponseHasAnswer, domain=QuestionnaireResponse, range=Union[Union[str, AnswerAnswerId], list[Union[str, AnswerAnswerId]]], mappings = [FHIR["questionnaireResponse.item.answer"]])

slots.questionnaireResponseHasDerivedScoreValue = Slot(uri=FAQIR.questionnaireResponseHasDerivedScoreValue, name="questionnaireResponseHasDerivedScoreValue", curie=FAQIR.curie('questionnaireResponseHasDerivedScoreValue'),
                   model_uri=DATAMODEL.questionnaireResponseHasDerivedScoreValue, domain=QuestionnaireResponse, range=Optional[Union[Union[str, ScoreValueScoreValueId], list[Union[str, ScoreValueScoreValueId]]]])

slots.questionnaireUsesScoreDefinition = Slot(uri=FAQIR.questionnaireUsesScoreDefinition, name="questionnaireUsesScoreDefinition", curie=FAQIR.curie('questionnaireUsesScoreDefinition'),
                   model_uri=DATAMODEL.questionnaireUsesScoreDefinition, domain=Questionnaire, range=Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]])

slots.answerInQuestionnaireResponse = Slot(uri=FAQIR.answerInQuestionnaireResponse, name="answerInQuestionnaireResponse", curie=FAQIR.curie('answerInQuestionnaireResponse'),
                   model_uri=DATAMODEL.answerInQuestionnaireResponse, domain=Answer, range=Union[str, QuestionnaireResponseQuestionnaireResponseId], mappings = [FHIR["QuestionnaireResponse.item.answer"]])

slots.answerToQuestion = Slot(uri=FAQIR.answerToQuestion, name="answerToQuestion", curie=FAQIR.curie('answerToQuestion'),
                   model_uri=DATAMODEL.answerToQuestion, domain=Answer, range=Union[str, QuestionQuestionId], mappings = [FHIR["QuestionnaireResponse.item.answer.question"]])

slots.questionnaireHasQuestionnaireResponse = Slot(uri=FAQIR.questionnaireHasQuestionnaireResponse, name="questionnaireHasQuestionnaireResponse", curie=FAQIR.curie('questionnaireHasQuestionnaireResponse'),
                   model_uri=DATAMODEL.questionnaireHasQuestionnaireResponse, domain=Questionnaire, range=Optional[Union[Union[str, QuestionnaireResponseQuestionnaireResponseId], list[Union[str, QuestionnaireResponseQuestionnaireResponseId]]]], mappings = [FHIR["QuestionnaireResponse"]])

slots.questionnaireHasOrderedQuestion = Slot(uri=FAQIR.questionnaireHasOrderedQuestion, name="questionnaireHasOrderedQuestion", curie=FAQIR.curie('questionnaireHasOrderedQuestion'),
                   model_uri=DATAMODEL.questionnaireHasOrderedQuestion, domain=Questionnaire, range=Optional[Union[dict[Union[str, OrderedQuestionOrderedQuestionId], Union[dict, OrderedQuestion]], list[Union[dict, OrderedQuestion]]]], mappings = [FHIR["Questionnaire.item.where(type='question')"]])

slots.questionnaireHasOrderedSection = Slot(uri=FAQIR.questionnaireHasOrderedSection, name="questionnaireHasOrderedSection", curie=FAQIR.curie('questionnaireHasOrderedSection'),
                   model_uri=DATAMODEL.questionnaireHasOrderedSection, domain=Questionnaire, range=Optional[Union[dict[Union[str, OrderedSectionOrderedSectionId], Union[dict, "OrderedSection"]], list[Union[dict, "OrderedSection"]]]], mappings = [FHIR["Questionnaire.item.where(type='group')"]])

slots.questionnaireAuthoredByOrg = Slot(uri=FAQIR.questionnaireAuthoredByOrg, name="questionnaireAuthoredByOrg", curie=FAQIR.curie('questionnaireAuthoredByOrg'),
                   model_uri=DATAMODEL.questionnaireAuthoredByOrg, domain=Questionnaire, range=Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]], mappings = [FHIR["Questionnaire.author"]])

slots.questionnairePartOfProcedure = Slot(uri=FAQIR.questionnairePartOfProcedure, name="questionnairePartOfProcedure", curie=FAQIR.curie('questionnairePartOfProcedure'),
                   model_uri=DATAMODEL.questionnairePartOfProcedure, domain=Questionnaire, range=Optional[Union[Union[str, ProcedureProcedureId], list[Union[str, ProcedureProcedureId]]]])

slots.questionInOrderedQuestion = Slot(uri=FAQIR.questionInOrderedQuestion, name="questionInOrderedQuestion", curie=FAQIR.curie('questionInOrderedQuestion'),
                   model_uri=DATAMODEL.questionInOrderedQuestion, domain=Question, range=Optional[Union[Union[str, OrderedQuestionOrderedQuestionId], list[Union[str, OrderedQuestionOrderedQuestionId]]]])

slots.questionHasAnswer = Slot(uri=FAQIR.questionHasAnswer, name="questionHasAnswer", curie=FAQIR.curie('questionHasAnswer'),
                   model_uri=DATAMODEL.questionHasAnswer, domain=Question, range=Optional[Union[Union[str, AnswerAnswerId], list[Union[str, AnswerAnswerId]]]], mappings = [FHIR["Questionnaire.item.answer"]])

slots.questionAuthoredByOrg = Slot(uri=FAQIR.questionAuthoredByOrg, name="questionAuthoredByOrg", curie=FAQIR.curie('questionAuthoredByOrg'),
                   model_uri=DATAMODEL.questionAuthoredByOrg, domain=Question, range=Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]])

slots.questionUsedInScoreDefinition = Slot(uri=FAQIR.questionUsedInScoreDefinition, name="questionUsedInScoreDefinition", curie=FAQIR.curie('questionUsedInScoreDefinition'),
                   model_uri=DATAMODEL.questionUsedInScoreDefinition, domain=Question, range=Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]])

slots.orderedQuestionHasQuestion = Slot(uri=FAQIR.orderedQuestionHasQuestion, name="orderedQuestionHasQuestion", curie=FAQIR.curie('orderedQuestionHasQuestion'),
                   model_uri=DATAMODEL.orderedQuestionHasQuestion, domain=OrderedQuestion, range=Union[str, QuestionQuestionId])

slots.orderedQuestionPartOfQuestionnaire = Slot(uri=FAQIR.orderedQuestionPartOfQuestionnaire, name="orderedQuestionPartOfQuestionnaire", curie=FAQIR.curie('orderedQuestionPartOfQuestionnaire'),
                   model_uri=DATAMODEL.orderedQuestionPartOfQuestionnaire, domain=OrderedQuestion, range=Optional[Union[str, QuestionnaireQuestionnaireId]], mappings = [FHIR["Questionnaire.item"]])

slots.orderedQuestionPartOfSection = Slot(uri=FAQIR.orderedQuestionPartOfSection, name="orderedQuestionPartOfSection", curie=FAQIR.curie('orderedQuestionPartOfSection'),
                   model_uri=DATAMODEL.orderedQuestionPartOfSection, domain=OrderedQuestion, range=Optional[Union[str, SectionSectionId]], mappings = [FHIR["Questionnaire.item"]])

slots.sectionHasOrderedQuestion = Slot(uri=FAQIR.sectionHasOrderedQuestion, name="sectionHasOrderedQuestion", curie=FAQIR.curie('sectionHasOrderedQuestion'),
                   model_uri=DATAMODEL.sectionHasOrderedQuestion, domain=Section, range=Optional[Union[dict[Union[str, OrderedQuestionOrderedQuestionId], Union[dict, OrderedQuestion]], list[Union[dict, OrderedQuestion]]]], mappings = [FHIR["Questionnaire.item.where(type='question')"]])

slots.sectionHasOrderedSection = Slot(uri=FAQIR.sectionHasOrderedSection, name="sectionHasOrderedSection", curie=FAQIR.curie('sectionHasOrderedSection'),
                   model_uri=DATAMODEL.sectionHasOrderedSection, domain=Section, range=Optional[Union[dict[Union[str, OrderedSectionOrderedSectionId], Union[dict, OrderedSection]], list[Union[dict, OrderedSection]]]], mappings = [FHIR["Questionnaire.item.where(type='group')"]])

slots.sectionInOrderedSection = Slot(uri=FAQIR.sectionInOrderedSection, name="sectionInOrderedSection", curie=FAQIR.curie('sectionInOrderedSection'),
                   model_uri=DATAMODEL.sectionInOrderedSection, domain=Section, range=Optional[Union[Union[str, OrderedSectionOrderedSectionId], list[Union[str, OrderedSectionOrderedSectionId]]]])

slots.sectionAuthoredByOrg = Slot(uri=FAQIR.sectionAuthoredByOrg, name="sectionAuthoredByOrg", curie=FAQIR.curie('sectionAuthoredByOrg'),
                   model_uri=DATAMODEL.sectionAuthoredByOrg, domain=Section, range=Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]], mappings = [FHIR["Questionnaire.author"]])

slots.sectionUsesScoreDefinition = Slot(uri=FAQIR.sectionUsesScoreDefinition, name="sectionUsesScoreDefinition", curie=FAQIR.curie('sectionUsesScoreDefinition'),
                   model_uri=DATAMODEL.sectionUsesScoreDefinition, domain=Section, range=Optional[Union[Union[str, ScoreDefinitionScoreDefinitionId], list[Union[str, ScoreDefinitionScoreDefinitionId]]]])

slots.orderedSectionPartOfQuestionnaire = Slot(uri=FAQIR.orderedSectionPartOfQuestionnaire, name="orderedSectionPartOfQuestionnaire", curie=FAQIR.curie('orderedSectionPartOfQuestionnaire'),
                   model_uri=DATAMODEL.orderedSectionPartOfQuestionnaire, domain=OrderedSection, range=Optional[Union[str, QuestionnaireQuestionnaireId]], mappings = [FHIR["Questionnaire.item"]])

slots.orderedSectionPartOfSection = Slot(uri=FAQIR.orderedSectionPartOfSection, name="orderedSectionPartOfSection", curie=FAQIR.curie('orderedSectionPartOfSection'),
                   model_uri=DATAMODEL.orderedSectionPartOfSection, domain=OrderedSection, range=Optional[Union[str, SectionSectionId]], mappings = [FHIR["Questionnaire.item"]])

slots.orderedSectionHasSection = Slot(uri=FAQIR.orderedSectionHasSection, name="orderedSectionHasSection", curie=FAQIR.curie('orderedSectionHasSection'),
                   model_uri=DATAMODEL.orderedSectionHasSection, domain=OrderedSection, range=Union[str, SectionSectionId])

slots.scoreDefinitionHasScoreParameter = Slot(uri=FAQIR.scoreDefinitionHasScoreParameter, name="scoreDefinitionHasScoreParameter", curie=FAQIR.curie('scoreDefinitionHasScoreParameter'),
                   model_uri=DATAMODEL.scoreDefinitionHasScoreParameter, domain=ScoreDefinition, range=Optional[Union[Union[str, ScoreParameterScoreParameterId], list[Union[str, ScoreParameterScoreParameterId]]]])

slots.scoreDefinitionUsesQuestion = Slot(uri=FAQIR.scoreDefinitionUsesQuestion, name="scoreDefinitionUsesQuestion", curie=FAQIR.curie('scoreDefinitionUsesQuestion'),
                   model_uri=DATAMODEL.scoreDefinitionUsesQuestion, domain=ScoreDefinition, range=Union[Union[str, QuestionQuestionId], list[Union[str, QuestionQuestionId]]])

slots.scoreDefinitionHasScoreValue = Slot(uri=FAQIR.scoreDefinitionHasScoreValue, name="scoreDefinitionHasScoreValue", curie=FAQIR.curie('scoreDefinitionHasScoreValue'),
                   model_uri=DATAMODEL.scoreDefinitionHasScoreValue, domain=ScoreDefinition, range=Optional[Union[Union[str, ScoreValueScoreValueId], list[Union[str, ScoreValueScoreValueId]]]])

slots.scoreDefinitionAuthoredByOrg = Slot(uri=FAQIR.scoreDefinitionAuthoredByOrg, name="scoreDefinitionAuthoredByOrg", curie=FAQIR.curie('scoreDefinitionAuthoredByOrg'),
                   model_uri=DATAMODEL.scoreDefinitionAuthoredByOrg, domain=ScoreDefinition, range=Optional[Union[Union[str, OrganizationOrganizationId], list[Union[str, OrganizationOrganizationId]]]], mappings = [FHIR["Questionnaire.author"]])

slots.scoreDefinitionUsedByQuestionnare = Slot(uri=FAQIR.scoreDefinitionUsedByQuestionnare, name="scoreDefinitionUsedByQuestionnare", curie=FAQIR.curie('scoreDefinitionUsedByQuestionnare'),
                   model_uri=DATAMODEL.scoreDefinitionUsedByQuestionnare, domain=ScoreDefinition, range=Optional[Union[Union[str, QuestionnaireQuestionnaireId], list[Union[str, QuestionnaireQuestionnaireId]]]])

slots.scoreDefinitionUsedBySection = Slot(uri=FAQIR.scoreDefinitionUsedBySection, name="scoreDefinitionUsedBySection", curie=FAQIR.curie('scoreDefinitionUsedBySection'),
                   model_uri=DATAMODEL.scoreDefinitionUsedBySection, domain=ScoreDefinition, range=Optional[Union[Union[str, SectionSectionId], list[Union[str, SectionSectionId]]]])

slots.scoreParameterPartOfScoreDefinition = Slot(uri=FAQIR.scoreParameterPartOfScoreDefinition, name="scoreParameterPartOfScoreDefinition", curie=FAQIR.curie('scoreParameterPartOfScoreDefinition'),
                   model_uri=DATAMODEL.scoreParameterPartOfScoreDefinition, domain=ScoreParameter, range=Union[str, ScoreDefinitionScoreDefinitionId])

slots.scoreValueBasedOnScoreDefinition = Slot(uri=FAQIR.scoreValueBasedOnScoreDefinition, name="scoreValueBasedOnScoreDefinition", curie=FAQIR.curie('scoreValueBasedOnScoreDefinition'),
                   model_uri=DATAMODEL.scoreValueBasedOnScoreDefinition, domain=ScoreValue, range=Union[str, ScoreDefinitionScoreDefinitionId])

slots.scoreValueDerivedFromQuestionnaireResponse = Slot(uri=FAQIR.scoreValueDerivedFromQuestionnaireResponse, name="scoreValueDerivedFromQuestionnaireResponse", curie=FAQIR.curie('scoreValueDerivedFromQuestionnaireResponse'),
                   model_uri=DATAMODEL.scoreValueDerivedFromQuestionnaireResponse, domain=ScoreValue, range=Union[Union[str, QuestionnaireResponseQuestionnaireResponseId], list[Union[str, QuestionnaireResponseQuestionnaireResponseId]]])

slots.vault__vaultId = Slot(uri=DATAMODEL['vault/vaultId'], name="vault__vaultId", curie=DATAMODEL.curie('vault/vaultId'),
                   model_uri=DATAMODEL.vault__vaultId, domain=None, range=URIRef)

slots.vault__birthdate = Slot(uri=DATAMODEL['vault/birthdate'], name="vault__birthdate", curie=DATAMODEL.curie('vault/birthdate'),
                   model_uri=DATAMODEL.vault__birthdate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.vault__weight = Slot(uri=DATAMODEL['vault/weight'], name="vault__weight", curie=DATAMODEL.curie('vault/weight'),
                   model_uri=DATAMODEL.vault__weight, domain=None, range=Optional[Union[dict, Weight]])

slots.vault__full_name = Slot(uri=DATAMODEL['vault/full_name'], name="vault__full_name", curie=DATAMODEL.curie('vault/full_name'),
                   model_uri=DATAMODEL.vault__full_name, domain=None, range=Optional[Union[dict, FullName]])

slots.fullName__first_name = Slot(uri=DATAMODEL['vault/first_name'], name="fullName__first_name", curie=DATAMODEL.curie('vault/first_name'),
                   model_uri=DATAMODEL.fullName__first_name, domain=None, range=Optional[str])

slots.fullName__middle_name = Slot(uri=DATAMODEL['vault/middle_name'], name="fullName__middle_name", curie=DATAMODEL.curie('vault/middle_name'),
                   model_uri=DATAMODEL.fullName__middle_name, domain=None, range=Optional[str])

slots.fullName__family_name = Slot(uri=DATAMODEL['vault/family_name'], name="fullName__family_name", curie=DATAMODEL.curie('vault/family_name'),
                   model_uri=DATAMODEL.fullName__family_name, domain=None, range=Optional[str])

slots.weight__weightType = Slot(uri=DATAMODEL['vault/weightType'], name="weight__weightType", curie=DATAMODEL.curie('vault/weightType'),
                   model_uri=DATAMODEL.weight__weightType, domain=None, range=Union[str, "WeightType"])

slots.valueNumerical__numericalValue = Slot(uri=TYPES['/numericalValue'], name="valueNumerical__numericalValue", curie=TYPES.curie('/numericalValue'),
                   model_uri=DATAMODEL.valueNumerical__numericalValue, domain=None, range=Decimal)

slots.numericalParams__numericalUnit = Slot(uri=UCUM.units, name="numericalParams__numericalUnit", curie=UCUM.curie('units'),
                   model_uri=DATAMODEL.numericalParams__numericalUnit, domain=None, range=Optional[Union[str, "UnitOfMeasure"]])

slots.numericalParams__numericalPrecision = Slot(uri=TYPES['/numericalPrecision'], name="numericalParams__numericalPrecision", curie=TYPES.curie('/numericalPrecision'),
                   model_uri=DATAMODEL.numericalParams__numericalPrecision, domain=None, range=Optional[int])

slots.intervalParams__minValue = Slot(uri=TYPES['/minValue'], name="intervalParams__minValue", curie=TYPES.curie('/minValue'),
                   model_uri=DATAMODEL.intervalParams__minValue, domain=None, range=float)

slots.intervalParams__minLabel = Slot(uri=TYPES['/minLabel'], name="intervalParams__minLabel", curie=TYPES.curie('/minLabel'),
                   model_uri=DATAMODEL.intervalParams__minLabel, domain=None, range=Optional[str])

slots.intervalParams__maxValue = Slot(uri=TYPES['/maxValue'], name="intervalParams__maxValue", curie=TYPES.curie('/maxValue'),
                   model_uri=DATAMODEL.intervalParams__maxValue, domain=None, range=float)

slots.intervalParams__maxLabel = Slot(uri=TYPES['/maxLabel'], name="intervalParams__maxLabel", curie=TYPES.curie('/maxLabel'),
                   model_uri=DATAMODEL.intervalParams__maxLabel, domain=None, range=Optional[str])

slots.valueString__stringValue = Slot(uri=TYPES['/stringValue'], name="valueString__stringValue", curie=TYPES.curie('/stringValue'),
                   model_uri=DATAMODEL.valueString__stringValue, domain=None, range=str)

slots.valueDateTime__dateTimeValue = Slot(uri=TYPES['/dateTimeValue'], name="valueDateTime__dateTimeValue", curie=TYPES.curie('/dateTimeValue'),
                   model_uri=DATAMODEL.valueDateTime__dateTimeValue, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.valueCoding__code = Slot(uri=TYPES['/code'], name="valueCoding__code", curie=TYPES.curie('/code'),
                   model_uri=DATAMODEL.valueCoding__code, domain=None, range=str)

slots.valueCoding__display = Slot(uri=TYPES['/display'], name="valueCoding__display", curie=TYPES.curie('/display'),
                   model_uri=DATAMODEL.valueCoding__display, domain=None, range=str)

slots.metadata__lastUpdated = Slot(uri=DATAMODEL['core/versions/lastUpdated'], name="metadata__lastUpdated", curie=DATAMODEL.curie('core/versions/lastUpdated'),
                   model_uri=DATAMODEL.metadata__lastUpdated, domain=None, range=Union[str, XSDDateTime])

slots.organization__organizationId = Slot(uri=DATAMODEL['entities/organization/organizationId'], name="organization__organizationId", curie=DATAMODEL.curie('entities/organization/organizationId'),
                   model_uri=DATAMODEL.organization__organizationId, domain=None, range=URIRef)

slots.organization__organizationLabel = Slot(uri=DATAMODEL['entities/organization/organizationLabel'], name="organization__organizationLabel", curie=DATAMODEL.curie('entities/organization/organizationLabel'),
                   model_uri=DATAMODEL.organization__organizationLabel, domain=None, range=str)

slots.organization__organizationType = Slot(uri=DATAMODEL['entities/organization/organizationType'], name="organization__organizationType", curie=DATAMODEL.curie('entities/organization/organizationType'),
                   model_uri=DATAMODEL.organization__organizationType, domain=None, range=Union[str, "OrganizationType"])

slots.procedure__procedureId = Slot(uri=DATAMODEL['entities/procedure/procedureId'], name="procedure__procedureId", curie=DATAMODEL.curie('entities/procedure/procedureId'),
                   model_uri=DATAMODEL.procedure__procedureId, domain=None, range=URIRef)

slots.procedure__procedureLabel = Slot(uri=DATAMODEL['entities/procedure/procedureLabel'], name="procedure__procedureLabel", curie=DATAMODEL.curie('entities/procedure/procedureLabel'),
                   model_uri=DATAMODEL.procedure__procedureLabel, domain=None, range=str)

slots.procedure__procedureDescription = Slot(uri=DATAMODEL['entities/procedure/procedureDescription'], name="procedure__procedureDescription", curie=DATAMODEL.curie('entities/procedure/procedureDescription'),
                   model_uri=DATAMODEL.procedure__procedureDescription, domain=None, range=Optional[str])

slots.questionnaireResponse__questionnaireResponseId = Slot(uri=QUESTIONNAIRE['classes/questionnaireResponseId'], name="questionnaireResponse__questionnaireResponseId", curie=QUESTIONNAIRE.curie('classes/questionnaireResponseId'),
                   model_uri=DATAMODEL.questionnaireResponse__questionnaireResponseId, domain=None, range=URIRef)

slots.questionnaireResponse__questionnaireResponseStatus = Slot(uri=QUESTIONNAIRE['classes/questionnaireResponseStatus'], name="questionnaireResponse__questionnaireResponseStatus", curie=QUESTIONNAIRE.curie('classes/questionnaireResponseStatus'),
                   model_uri=DATAMODEL.questionnaireResponse__questionnaireResponseStatus, domain=None, range=Union[str, "QuestionnaireResponseStatus"], mappings = [FHIR["QuestionnaireResponse.status"]])

slots.questionnaireResponse__questionnaireResponseTimeStamp = Slot(uri=QUESTIONNAIRE['classes/questionnaireResponseTimeStamp'], name="questionnaireResponse__questionnaireResponseTimeStamp", curie=QUESTIONNAIRE.curie('classes/questionnaireResponseTimeStamp'),
                   model_uri=DATAMODEL.questionnaireResponse__questionnaireResponseTimeStamp, domain=None, range=Union[str, XSDDateTime], mappings = [FHIR["QuestionnaireResponse.authored"]])

slots.questionnaireResponse__questionnaireResponseLastUpdated = Slot(uri=QUESTIONNAIRE['classes/questionnaireResponseLastUpdated'], name="questionnaireResponse__questionnaireResponseLastUpdated", curie=QUESTIONNAIRE.curie('classes/questionnaireResponseLastUpdated'),
                   model_uri=DATAMODEL.questionnaireResponse__questionnaireResponseLastUpdated, domain=None, range=Union[str, XSDDateTime])

slots.answer__answerId = Slot(uri=QUESTIONNAIRE['classes/answerId'], name="answer__answerId", curie=QUESTIONNAIRE.curie('classes/answerId'),
                   model_uri=DATAMODEL.answer__answerId, domain=None, range=URIRef)

slots.answer__answerValueNumerical = Slot(uri=QUESTIONNAIRE['classes/answerValueNumerical'], name="answer__answerValueNumerical", curie=QUESTIONNAIRE.curie('classes/answerValueNumerical'),
                   model_uri=DATAMODEL.answer__answerValueNumerical, domain=None, range=Optional[Union[dict, ValueNumerical]], mappings = [FHIR["QuestionnaireResponse.item.answer.valueDecimal"]])

slots.answer__answerValueString = Slot(uri=QUESTIONNAIRE['classes/answerValueString'], name="answer__answerValueString", curie=QUESTIONNAIRE.curie('classes/answerValueString'),
                   model_uri=DATAMODEL.answer__answerValueString, domain=None, range=Optional[Union[Union[dict, ValueString], list[Union[dict, ValueString]]]], mappings = [FHIR["QuestionnaireResponse.item.answer.valueString"]])

slots.answer__answerValueDateTime = Slot(uri=QUESTIONNAIRE['classes/answerValueDateTime'], name="answer__answerValueDateTime", curie=QUESTIONNAIRE.curie('classes/answerValueDateTime'),
                   model_uri=DATAMODEL.answer__answerValueDateTime, domain=None, range=Optional[Union[dict, ValueDateTime]], mappings = [FHIR["QuestionnaireResponse.item.answer.valueDateTime"]])

slots.answer__answerIsEmpty = Slot(uri=QUESTIONNAIRE['classes/answerIsEmpty'], name="answer__answerIsEmpty", curie=QUESTIONNAIRE.curie('classes/answerIsEmpty'),
                   model_uri=DATAMODEL.answer__answerIsEmpty, domain=None, range=Optional[Union[bool, Bool]])

slots.answer__answerTimeStamp = Slot(uri=QUESTIONNAIRE['classes/answerTimeStamp'], name="answer__answerTimeStamp", curie=QUESTIONNAIRE.curie('classes/answerTimeStamp'),
                   model_uri=DATAMODEL.answer__answerTimeStamp, domain=None, range=Union[str, XSDDateTime])

slots.orderedQuestion__orderedQuestionId = Slot(uri=QUESTIONNAIRE['classes/orderedQuestionId'], name="orderedQuestion__orderedQuestionId", curie=QUESTIONNAIRE.curie('classes/orderedQuestionId'),
                   model_uri=DATAMODEL.orderedQuestion__orderedQuestionId, domain=None, range=URIRef)

slots.orderedQuestion__questionOrder = Slot(uri=QUESTIONNAIRE['classes/questionOrder'], name="orderedQuestion__questionOrder", curie=QUESTIONNAIRE.curie('classes/questionOrder'),
                   model_uri=DATAMODEL.orderedQuestion__questionOrder, domain=None, range=int)

slots.question__questionId = Slot(uri=QUESTIONNAIRE['classes/questionId'], name="question__questionId", curie=QUESTIONNAIRE.curie('classes/questionId'),
                   model_uri=DATAMODEL.question__questionId, domain=None, range=URIRef)

slots.question__questionTag = Slot(uri=QUESTIONNAIRE['classes/questionTag'], name="question__questionTag", curie=QUESTIONNAIRE.curie('classes/questionTag'),
                   model_uri=DATAMODEL.question__questionTag, domain=None, range=str)

slots.question__questionLabel = Slot(uri=QUESTIONNAIRE['classes/questionLabel'], name="question__questionLabel", curie=QUESTIONNAIRE.curie('classes/questionLabel'),
                   model_uri=DATAMODEL.question__questionLabel, domain=None, range=str)

slots.question__questionNumericalParams = Slot(uri=QUESTIONNAIRE['classes/questionNumericalParams'], name="question__questionNumericalParams", curie=QUESTIONNAIRE.curie('classes/questionNumericalParams'),
                   model_uri=DATAMODEL.question__questionNumericalParams, domain=None, range=Optional[Union[dict, NumericalParams]])

slots.question__questionCodingParams = Slot(uri=QUESTIONNAIRE['classes/questionCodingParams'], name="question__questionCodingParams", curie=QUESTIONNAIRE.curie('classes/questionCodingParams'),
                   model_uri=DATAMODEL.question__questionCodingParams, domain=None, range=Optional[Union[Union[dict, ValueCoding], list[Union[dict, ValueCoding]]]])

slots.question__questionIntervalParams = Slot(uri=QUESTIONNAIRE['classes/questionIntervalParams'], name="question__questionIntervalParams", curie=QUESTIONNAIRE.curie('classes/questionIntervalParams'),
                   model_uri=DATAMODEL.question__questionIntervalParams, domain=None, range=Optional[Union[dict, IntervalParams]])

slots.question__questionRequired = Slot(uri=QUESTIONNAIRE['classes/questionRequired'], name="question__questionRequired", curie=QUESTIONNAIRE.curie('classes/questionRequired'),
                   model_uri=DATAMODEL.question__questionRequired, domain=None, range=Optional[Union[bool, Bool]], mappings = [FHIR["Questionnaire.item.required"]])

slots.questionnaire__questionnaireId = Slot(uri=QUESTIONNAIRE['classes/questionnaireId'], name="questionnaire__questionnaireId", curie=QUESTIONNAIRE.curie('classes/questionnaireId'),
                   model_uri=DATAMODEL.questionnaire__questionnaireId, domain=None, range=URIRef)

slots.questionnaire__questionnaireLabel = Slot(uri=QUESTIONNAIRE['classes/questionnaireLabel'], name="questionnaire__questionnaireLabel", curie=QUESTIONNAIRE.curie('classes/questionnaireLabel'),
                   model_uri=DATAMODEL.questionnaire__questionnaireLabel, domain=None, range=str)

slots.questionnaire__questionnaireStatus = Slot(uri=QUESTIONNAIRE['classes/questionnaireStatus'], name="questionnaire__questionnaireStatus", curie=QUESTIONNAIRE.curie('classes/questionnaireStatus'),
                   model_uri=DATAMODEL.questionnaire__questionnaireStatus, domain=None, range=Union[str, "QuestionnaireStatus"], mappings = [FHIR["Questionnaire.status"]])

slots.questionnaire__questionnaireVersion = Slot(uri=QUESTIONNAIRE['classes/questionnaireVersion'], name="questionnaire__questionnaireVersion", curie=QUESTIONNAIRE.curie('classes/questionnaireVersion'),
                   model_uri=DATAMODEL.questionnaire__questionnaireVersion, domain=None, range=str,
                   pattern=re.compile(r'^\d+\.\d+\.\d+$'))

slots.questionnaire__questionnaireLastUpdated = Slot(uri=QUESTIONNAIRE['classes/questionnaireLastUpdated'], name="questionnaire__questionnaireLastUpdated", curie=QUESTIONNAIRE.curie('classes/questionnaireLastUpdated'),
                   model_uri=DATAMODEL.questionnaire__questionnaireLastUpdated, domain=None, range=Union[str, XSDDateTime], mappings = [FHIR["Questionnaire.date"]])

slots.orderedSection__orderedSectionId = Slot(uri=QUESTIONNAIRE['classes/orderedSectionId'], name="orderedSection__orderedSectionId", curie=QUESTIONNAIRE.curie('classes/orderedSectionId'),
                   model_uri=DATAMODEL.orderedSection__orderedSectionId, domain=None, range=URIRef)

slots.orderedSection__sectionOrder = Slot(uri=QUESTIONNAIRE['classes/sectionOrder'], name="orderedSection__sectionOrder", curie=QUESTIONNAIRE.curie('classes/sectionOrder'),
                   model_uri=DATAMODEL.orderedSection__sectionOrder, domain=None, range=int)

slots.section__sectionId = Slot(uri=QUESTIONNAIRE['classes/sectionId'], name="section__sectionId", curie=QUESTIONNAIRE.curie('classes/sectionId'),
                   model_uri=DATAMODEL.section__sectionId, domain=None, range=URIRef)

slots.section__sectionLabel = Slot(uri=QUESTIONNAIRE['classes/sectionLabel'], name="section__sectionLabel", curie=QUESTIONNAIRE.curie('classes/sectionLabel'),
                   model_uri=DATAMODEL.section__sectionLabel, domain=None, range=str)

slots.scoreDefinition__scoreDefinitionId = Slot(uri=QUESTIONNAIRE['classes/scoreDefinitionId'], name="scoreDefinition__scoreDefinitionId", curie=QUESTIONNAIRE.curie('classes/scoreDefinitionId'),
                   model_uri=DATAMODEL.scoreDefinition__scoreDefinitionId, domain=None, range=URIRef)

slots.scoreDefinition__scoreDefinitionLabel = Slot(uri=QUESTIONNAIRE['classes/scoreDefinitionLabel'], name="scoreDefinition__scoreDefinitionLabel", curie=QUESTIONNAIRE.curie('classes/scoreDefinitionLabel'),
                   model_uri=DATAMODEL.scoreDefinition__scoreDefinitionLabel, domain=None, range=str)

slots.scoreDefinition__scoreDefinitionIntervalParams = Slot(uri=QUESTIONNAIRE['classes/scoreDefinitionIntervalParams'], name="scoreDefinition__scoreDefinitionIntervalParams", curie=QUESTIONNAIRE.curie('classes/scoreDefinitionIntervalParams'),
                   model_uri=DATAMODEL.scoreDefinition__scoreDefinitionIntervalParams, domain=None, range=Optional[Union[dict, IntervalParams]])

slots.scoreDefinition__scoreDefinitionFormula = Slot(uri=QUESTIONNAIRE['classes/scoreDefinitionFormula'], name="scoreDefinition__scoreDefinitionFormula", curie=QUESTIONNAIRE.curie('classes/scoreDefinitionFormula'),
                   model_uri=DATAMODEL.scoreDefinition__scoreDefinitionFormula, domain=None, range=str)

slots.scoreDefinition__scoreDefinitionCategories = Slot(uri=QUESTIONNAIRE['classes/scoreDefinitionCategories'], name="scoreDefinition__scoreDefinitionCategories", curie=QUESTIONNAIRE.curie('classes/scoreDefinitionCategories'),
                   model_uri=DATAMODEL.scoreDefinition__scoreDefinitionCategories, domain=None, range=Optional[Union[str, list[str]]])

slots.scoreDefinition__scoreDefinitionInterpretationGuide = Slot(uri=QUESTIONNAIRE['classes/scoreDefinitionInterpretationGuide'], name="scoreDefinition__scoreDefinitionInterpretationGuide", curie=QUESTIONNAIRE.curie('classes/scoreDefinitionInterpretationGuide'),
                   model_uri=DATAMODEL.scoreDefinition__scoreDefinitionInterpretationGuide, domain=None, range=Optional[str])

slots.scoreParameter__scoreParameterId = Slot(uri=QUESTIONNAIRE['classes/scoreParameterId'], name="scoreParameter__scoreParameterId", curie=QUESTIONNAIRE.curie('classes/scoreParameterId'),
                   model_uri=DATAMODEL.scoreParameter__scoreParameterId, domain=None, range=URIRef)

slots.scoreParameter__scoreParameterLabel = Slot(uri=QUESTIONNAIRE['classes/scoreParameterLabel'], name="scoreParameter__scoreParameterLabel", curie=QUESTIONNAIRE.curie('classes/scoreParameterLabel'),
                   model_uri=DATAMODEL.scoreParameter__scoreParameterLabel, domain=None, range=str)

slots.scoreParameter__scoreParameterType = Slot(uri=QUESTIONNAIRE['classes/scoreParameterType'], name="scoreParameter__scoreParameterType", curie=QUESTIONNAIRE.curie('classes/scoreParameterType'),
                   model_uri=DATAMODEL.scoreParameter__scoreParameterType, domain=None, range=Union[str, "ScoreParameterType"])

slots.scoreParameter__scoreParameterValueNumerical = Slot(uri=QUESTIONNAIRE['classes/scoreParameterValueNumerical'], name="scoreParameter__scoreParameterValueNumerical", curie=QUESTIONNAIRE.curie('classes/scoreParameterValueNumerical'),
                   model_uri=DATAMODEL.scoreParameter__scoreParameterValueNumerical, domain=None, range=Optional[Union[dict, ValueNumerical]])

slots.scoreParameter__scoreParameterValueDateTime = Slot(uri=QUESTIONNAIRE['classes/scoreParameterValueDateTime'], name="scoreParameter__scoreParameterValueDateTime", curie=QUESTIONNAIRE.curie('classes/scoreParameterValueDateTime'),
                   model_uri=DATAMODEL.scoreParameter__scoreParameterValueDateTime, domain=None, range=Optional[Union[dict, ValueDateTime]])

slots.scoreValue__scoreValueId = Slot(uri=QUESTIONNAIRE['classes/scoreValueId'], name="scoreValue__scoreValueId", curie=QUESTIONNAIRE.curie('classes/scoreValueId'),
                   model_uri=DATAMODEL.scoreValue__scoreValueId, domain=None, range=URIRef)

slots.scoreValue__scoreValueString = Slot(uri=QUESTIONNAIRE['classes/scoreValueString'], name="scoreValue__scoreValueString", curie=QUESTIONNAIRE.curie('classes/scoreValueString'),
                   model_uri=DATAMODEL.scoreValue__scoreValueString, domain=None, range=Optional[Union[dict, ValueString]])

slots.scoreValue__scoreValueNumerical = Slot(uri=QUESTIONNAIRE['classes/scoreValueNumerical'], name="scoreValue__scoreValueNumerical", curie=QUESTIONNAIRE.curie('classes/scoreValueNumerical'),
                   model_uri=DATAMODEL.scoreValue__scoreValueNumerical, domain=None, range=Optional[Union[dict, ValueNumerical]])

slots.scoreValue__scoreValueTimeStamp = Slot(uri=QUESTIONNAIRE['classes/scoreValueTimeStamp'], name="scoreValue__scoreValueTimeStamp", curie=QUESTIONNAIRE.curie('classes/scoreValueTimeStamp'),
                   model_uri=DATAMODEL.scoreValue__scoreValueTimeStamp, domain=None, range=Union[str, XSDDateTime])

slots.scoreValue__scoreValueStatus = Slot(uri=QUESTIONNAIRE['classes/scoreValueStatus'], name="scoreValue__scoreValueStatus", curie=QUESTIONNAIRE.curie('classes/scoreValueStatus'),
                   model_uri=DATAMODEL.scoreValue__scoreValueStatus, domain=None, range=Union[str, "ScoreValueStatus"])