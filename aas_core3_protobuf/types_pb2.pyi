from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ModellingKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Modellingkind_UNSPECIFIED: _ClassVar[ModellingKind]
    Modellingkind_TEMPLATE: _ClassVar[ModellingKind]
    Modellingkind_INSTANCE: _ClassVar[ModellingKind]

class QualifierKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Qualifierkind_UNSPECIFIED: _ClassVar[QualifierKind]
    Qualifierkind_VALUE_QUALIFIER: _ClassVar[QualifierKind]
    Qualifierkind_CONCEPT_QUALIFIER: _ClassVar[QualifierKind]
    Qualifierkind_TEMPLATE_QUALIFIER: _ClassVar[QualifierKind]

class AssetKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Assetkind_UNSPECIFIED: _ClassVar[AssetKind]
    Assetkind_TYPE: _ClassVar[AssetKind]
    Assetkind_INSTANCE: _ClassVar[AssetKind]
    Assetkind_NOT_APPLICABLE: _ClassVar[AssetKind]

class AasSubmodelElements(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Aassubmodelelements_UNSPECIFIED: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_ANNOTATED_RELATIONSHIP_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_BASIC_EVENT_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_BLOB: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_CAPABILITY: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_DATA_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_ENTITY: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_EVENT_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_FILE: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_MULTI_LANGUAGE_PROPERTY: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_OPERATION: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_PROPERTY: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_RANGE: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_REFERENCE_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_RELATIONSHIP_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_SUBMODEL_ELEMENT: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_SUBMODEL_ELEMENT_LIST: _ClassVar[AasSubmodelElements]
    Aassubmodelelements_SUBMODEL_ELEMENT_COLLECTION: _ClassVar[AasSubmodelElements]

class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Entitytype_UNSPECIFIED: _ClassVar[EntityType]
    Entitytype_CO_MANAGED_ENTITY: _ClassVar[EntityType]
    Entitytype_SELF_MANAGED_ENTITY: _ClassVar[EntityType]

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Direction_UNSPECIFIED: _ClassVar[Direction]
    Direction_INPUT: _ClassVar[Direction]
    Direction_OUTPUT: _ClassVar[Direction]

class StateOfEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Stateofevent_UNSPECIFIED: _ClassVar[StateOfEvent]
    Stateofevent_ON: _ClassVar[StateOfEvent]
    Stateofevent_OFF: _ClassVar[StateOfEvent]

class ReferenceTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Referencetypes_UNSPECIFIED: _ClassVar[ReferenceTypes]
    Referencetypes_EXTERNAL_REFERENCE: _ClassVar[ReferenceTypes]
    Referencetypes_MODEL_REFERENCE: _ClassVar[ReferenceTypes]

class KeyTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Keytypes_UNSPECIFIED: _ClassVar[KeyTypes]
    Keytypes_ANNOTATED_RELATIONSHIP_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_ASSET_ADMINISTRATION_SHELL: _ClassVar[KeyTypes]
    Keytypes_BASIC_EVENT_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_BLOB: _ClassVar[KeyTypes]
    Keytypes_CAPABILITY: _ClassVar[KeyTypes]
    Keytypes_CONCEPT_DESCRIPTION: _ClassVar[KeyTypes]
    Keytypes_DATA_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_ENTITY: _ClassVar[KeyTypes]
    Keytypes_EVENT_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_FILE: _ClassVar[KeyTypes]
    Keytypes_FRAGMENT_REFERENCE: _ClassVar[KeyTypes]
    Keytypes_GLOBAL_REFERENCE: _ClassVar[KeyTypes]
    Keytypes_IDENTIFIABLE: _ClassVar[KeyTypes]
    Keytypes_MULTI_LANGUAGE_PROPERTY: _ClassVar[KeyTypes]
    Keytypes_OPERATION: _ClassVar[KeyTypes]
    Keytypes_PROPERTY: _ClassVar[KeyTypes]
    Keytypes_RANGE: _ClassVar[KeyTypes]
    Keytypes_REFERABLE: _ClassVar[KeyTypes]
    Keytypes_REFERENCE_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_RELATIONSHIP_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_SUBMODEL: _ClassVar[KeyTypes]
    Keytypes_SUBMODEL_ELEMENT: _ClassVar[KeyTypes]
    Keytypes_SUBMODEL_ELEMENT_COLLECTION: _ClassVar[KeyTypes]
    Keytypes_SUBMODEL_ELEMENT_LIST: _ClassVar[KeyTypes]

class DataTypeDefXsd(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Datatypedefxsd_UNSPECIFIED: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_ANY_URI: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_BASE_64_BINARY: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_BOOLEAN: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_BYTE: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_DATE: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_DATE_TIME: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_DECIMAL: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_DOUBLE: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_DURATION: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_FLOAT: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_G_DAY: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_G_MONTH: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_G_MONTH_DAY: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_G_YEAR: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_G_YEAR_MONTH: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_HEX_BINARY: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_INT: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_INTEGER: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_LONG: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_NEGATIVE_INTEGER: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_NON_NEGATIVE_INTEGER: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_NON_POSITIVE_INTEGER: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_POSITIVE_INTEGER: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_SHORT: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_STRING: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_TIME: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_UNSIGNED_BYTE: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_UNSIGNED_INT: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_UNSIGNED_LONG: _ClassVar[DataTypeDefXsd]
    Datatypedefxsd_UNSIGNED_SHORT: _ClassVar[DataTypeDefXsd]

class DataTypeIec61360(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Datatypeiec61360_UNSPECIFIED: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_DATE: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_STRING: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_STRING_TRANSLATABLE: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_INTEGER_MEASURE: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_INTEGER_COUNT: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_INTEGER_CURRENCY: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_REAL_MEASURE: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_REAL_COUNT: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_REAL_CURRENCY: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_BOOLEAN: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_IRI: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_IRDI: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_RATIONAL: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_RATIONAL_MEASURE: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_TIME: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_TIMESTAMP: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_FILE: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_HTML: _ClassVar[DataTypeIec61360]
    Datatypeiec61360_BLOB: _ClassVar[DataTypeIec61360]

Modellingkind_UNSPECIFIED: ModellingKind
Modellingkind_TEMPLATE: ModellingKind
Modellingkind_INSTANCE: ModellingKind
Qualifierkind_UNSPECIFIED: QualifierKind
Qualifierkind_VALUE_QUALIFIER: QualifierKind
Qualifierkind_CONCEPT_QUALIFIER: QualifierKind
Qualifierkind_TEMPLATE_QUALIFIER: QualifierKind
Assetkind_UNSPECIFIED: AssetKind
Assetkind_TYPE: AssetKind
Assetkind_INSTANCE: AssetKind
Assetkind_NOT_APPLICABLE: AssetKind
Aassubmodelelements_UNSPECIFIED: AasSubmodelElements
Aassubmodelelements_ANNOTATED_RELATIONSHIP_ELEMENT: AasSubmodelElements
Aassubmodelelements_BASIC_EVENT_ELEMENT: AasSubmodelElements
Aassubmodelelements_BLOB: AasSubmodelElements
Aassubmodelelements_CAPABILITY: AasSubmodelElements
Aassubmodelelements_DATA_ELEMENT: AasSubmodelElements
Aassubmodelelements_ENTITY: AasSubmodelElements
Aassubmodelelements_EVENT_ELEMENT: AasSubmodelElements
Aassubmodelelements_FILE: AasSubmodelElements
Aassubmodelelements_MULTI_LANGUAGE_PROPERTY: AasSubmodelElements
Aassubmodelelements_OPERATION: AasSubmodelElements
Aassubmodelelements_PROPERTY: AasSubmodelElements
Aassubmodelelements_RANGE: AasSubmodelElements
Aassubmodelelements_REFERENCE_ELEMENT: AasSubmodelElements
Aassubmodelelements_RELATIONSHIP_ELEMENT: AasSubmodelElements
Aassubmodelelements_SUBMODEL_ELEMENT: AasSubmodelElements
Aassubmodelelements_SUBMODEL_ELEMENT_LIST: AasSubmodelElements
Aassubmodelelements_SUBMODEL_ELEMENT_COLLECTION: AasSubmodelElements
Entitytype_UNSPECIFIED: EntityType
Entitytype_CO_MANAGED_ENTITY: EntityType
Entitytype_SELF_MANAGED_ENTITY: EntityType
Direction_UNSPECIFIED: Direction
Direction_INPUT: Direction
Direction_OUTPUT: Direction
Stateofevent_UNSPECIFIED: StateOfEvent
Stateofevent_ON: StateOfEvent
Stateofevent_OFF: StateOfEvent
Referencetypes_UNSPECIFIED: ReferenceTypes
Referencetypes_EXTERNAL_REFERENCE: ReferenceTypes
Referencetypes_MODEL_REFERENCE: ReferenceTypes
Keytypes_UNSPECIFIED: KeyTypes
Keytypes_ANNOTATED_RELATIONSHIP_ELEMENT: KeyTypes
Keytypes_ASSET_ADMINISTRATION_SHELL: KeyTypes
Keytypes_BASIC_EVENT_ELEMENT: KeyTypes
Keytypes_BLOB: KeyTypes
Keytypes_CAPABILITY: KeyTypes
Keytypes_CONCEPT_DESCRIPTION: KeyTypes
Keytypes_DATA_ELEMENT: KeyTypes
Keytypes_ENTITY: KeyTypes
Keytypes_EVENT_ELEMENT: KeyTypes
Keytypes_FILE: KeyTypes
Keytypes_FRAGMENT_REFERENCE: KeyTypes
Keytypes_GLOBAL_REFERENCE: KeyTypes
Keytypes_IDENTIFIABLE: KeyTypes
Keytypes_MULTI_LANGUAGE_PROPERTY: KeyTypes
Keytypes_OPERATION: KeyTypes
Keytypes_PROPERTY: KeyTypes
Keytypes_RANGE: KeyTypes
Keytypes_REFERABLE: KeyTypes
Keytypes_REFERENCE_ELEMENT: KeyTypes
Keytypes_RELATIONSHIP_ELEMENT: KeyTypes
Keytypes_SUBMODEL: KeyTypes
Keytypes_SUBMODEL_ELEMENT: KeyTypes
Keytypes_SUBMODEL_ELEMENT_COLLECTION: KeyTypes
Keytypes_SUBMODEL_ELEMENT_LIST: KeyTypes
Datatypedefxsd_UNSPECIFIED: DataTypeDefXsd
Datatypedefxsd_ANY_URI: DataTypeDefXsd
Datatypedefxsd_BASE_64_BINARY: DataTypeDefXsd
Datatypedefxsd_BOOLEAN: DataTypeDefXsd
Datatypedefxsd_BYTE: DataTypeDefXsd
Datatypedefxsd_DATE: DataTypeDefXsd
Datatypedefxsd_DATE_TIME: DataTypeDefXsd
Datatypedefxsd_DECIMAL: DataTypeDefXsd
Datatypedefxsd_DOUBLE: DataTypeDefXsd
Datatypedefxsd_DURATION: DataTypeDefXsd
Datatypedefxsd_FLOAT: DataTypeDefXsd
Datatypedefxsd_G_DAY: DataTypeDefXsd
Datatypedefxsd_G_MONTH: DataTypeDefXsd
Datatypedefxsd_G_MONTH_DAY: DataTypeDefXsd
Datatypedefxsd_G_YEAR: DataTypeDefXsd
Datatypedefxsd_G_YEAR_MONTH: DataTypeDefXsd
Datatypedefxsd_HEX_BINARY: DataTypeDefXsd
Datatypedefxsd_INT: DataTypeDefXsd
Datatypedefxsd_INTEGER: DataTypeDefXsd
Datatypedefxsd_LONG: DataTypeDefXsd
Datatypedefxsd_NEGATIVE_INTEGER: DataTypeDefXsd
Datatypedefxsd_NON_NEGATIVE_INTEGER: DataTypeDefXsd
Datatypedefxsd_NON_POSITIVE_INTEGER: DataTypeDefXsd
Datatypedefxsd_POSITIVE_INTEGER: DataTypeDefXsd
Datatypedefxsd_SHORT: DataTypeDefXsd
Datatypedefxsd_STRING: DataTypeDefXsd
Datatypedefxsd_TIME: DataTypeDefXsd
Datatypedefxsd_UNSIGNED_BYTE: DataTypeDefXsd
Datatypedefxsd_UNSIGNED_INT: DataTypeDefXsd
Datatypedefxsd_UNSIGNED_LONG: DataTypeDefXsd
Datatypedefxsd_UNSIGNED_SHORT: DataTypeDefXsd
Datatypeiec61360_UNSPECIFIED: DataTypeIec61360
Datatypeiec61360_DATE: DataTypeIec61360
Datatypeiec61360_STRING: DataTypeIec61360
Datatypeiec61360_STRING_TRANSLATABLE: DataTypeIec61360
Datatypeiec61360_INTEGER_MEASURE: DataTypeIec61360
Datatypeiec61360_INTEGER_COUNT: DataTypeIec61360
Datatypeiec61360_INTEGER_CURRENCY: DataTypeIec61360
Datatypeiec61360_REAL_MEASURE: DataTypeIec61360
Datatypeiec61360_REAL_COUNT: DataTypeIec61360
Datatypeiec61360_REAL_CURRENCY: DataTypeIec61360
Datatypeiec61360_BOOLEAN: DataTypeIec61360
Datatypeiec61360_IRI: DataTypeIec61360
Datatypeiec61360_IRDI: DataTypeIec61360
Datatypeiec61360_RATIONAL: DataTypeIec61360
Datatypeiec61360_RATIONAL_MEASURE: DataTypeIec61360
Datatypeiec61360_TIME: DataTypeIec61360
Datatypeiec61360_TIMESTAMP: DataTypeIec61360
Datatypeiec61360_FILE: DataTypeIec61360
Datatypeiec61360_HTML: DataTypeIec61360
Datatypeiec61360_BLOB: DataTypeIec61360

class Extension(_message.Message):
    __slots__ = (
        "semantic_id",
        "supplemental_semantic_ids",
        "name",
        "value_type",
        "value",
        "refers_to",
    )
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    REFERS_TO_FIELD_NUMBER: _ClassVar[int]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    name: str
    value_type: DataTypeDefXsd
    value: str
    refers_to: _containers.RepeatedCompositeFieldContainer[Reference]
    def __init__(
        self,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        name: _Optional[str] = ...,
        value_type: _Optional[_Union[DataTypeDefXsd, str]] = ...,
        value: _Optional[str] = ...,
        refers_to: _Optional[_Iterable[_Union[Reference, _Mapping]]] = ...,
    ) -> None: ...

class AdministrativeInformation(_message.Message):
    __slots__ = (
        "embedded_data_specifications",
        "version",
        "revision",
        "creator",
        "template_id",
    )
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    version: str
    revision: str
    creator: Reference
    template_id: str
    def __init__(
        self,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        version: _Optional[str] = ...,
        revision: _Optional[str] = ...,
        creator: _Optional[_Union[Reference, _Mapping]] = ...,
        template_id: _Optional[str] = ...,
    ) -> None: ...

class Qualifier(_message.Message):
    __slots__ = (
        "semantic_id",
        "supplemental_semantic_ids",
        "kind",
        "type",
        "value_type",
        "value",
        "value_id",
    )
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    kind: QualifierKind
    type: str
    value_type: DataTypeDefXsd
    value: str
    value_id: Reference
    def __init__(
        self,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        kind: _Optional[_Union[QualifierKind, str]] = ...,
        type: _Optional[str] = ...,
        value_type: _Optional[_Union[DataTypeDefXsd, str]] = ...,
        value: _Optional[str] = ...,
        value_id: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class AssetAdministrationShell(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "administration",
        "id",
        "embedded_data_specifications",
        "derived_from",
        "asset_information",
        "submodels",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    DERIVED_FROM_FIELD_NUMBER: _ClassVar[int]
    ASSET_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SUBMODELS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    administration: AdministrativeInformation
    id: str
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    derived_from: Reference
    asset_information: AssetInformation
    submodels: _containers.RepeatedCompositeFieldContainer[Reference]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        administration: _Optional[_Union[AdministrativeInformation, _Mapping]] = ...,
        id: _Optional[str] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        derived_from: _Optional[_Union[Reference, _Mapping]] = ...,
        asset_information: _Optional[_Union[AssetInformation, _Mapping]] = ...,
        submodels: _Optional[_Iterable[_Union[Reference, _Mapping]]] = ...,
    ) -> None: ...

class AssetInformation(_message.Message):
    __slots__ = (
        "asset_kind",
        "global_asset_id",
        "specific_asset_ids",
        "asset_type",
        "default_thumbnail",
    )
    ASSET_KIND_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_ASSET_IDS_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    asset_kind: AssetKind
    global_asset_id: str
    specific_asset_ids: _containers.RepeatedCompositeFieldContainer[SpecificAssetId]
    asset_type: str
    default_thumbnail: Resource
    def __init__(
        self,
        asset_kind: _Optional[_Union[AssetKind, str]] = ...,
        global_asset_id: _Optional[str] = ...,
        specific_asset_ids: _Optional[
            _Iterable[_Union[SpecificAssetId, _Mapping]]
        ] = ...,
        asset_type: _Optional[str] = ...,
        default_thumbnail: _Optional[_Union[Resource, _Mapping]] = ...,
    ) -> None: ...

class Resource(_message.Message):
    __slots__ = ("path", "content_type")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    path: str
    content_type: str
    def __init__(
        self, path: _Optional[str] = ..., content_type: _Optional[str] = ...
    ) -> None: ...

class SpecificAssetId(_message.Message):
    __slots__ = (
        "semantic_id",
        "supplemental_semantic_ids",
        "name",
        "value",
        "external_subject_id",
    )
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    name: str
    value: str
    external_subject_id: Reference
    def __init__(
        self,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        name: _Optional[str] = ...,
        value: _Optional[str] = ...,
        external_subject_id: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class Submodel(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "administration",
        "id",
        "kind",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "submodel_elements",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    administration: AdministrativeInformation
    id: str
    kind: ModellingKind
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    submodel_elements: _containers.RepeatedCompositeFieldContainer[
        SubmodelElement_choice
    ]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        administration: _Optional[_Union[AdministrativeInformation, _Mapping]] = ...,
        id: _Optional[str] = ...,
        kind: _Optional[_Union[ModellingKind, str]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        submodel_elements: _Optional[
            _Iterable[_Union[SubmodelElement_choice, _Mapping]]
        ] = ...,
    ) -> None: ...

class RelationshipElement(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "first",
        "second",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    first: Reference
    second: Reference
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        first: _Optional[_Union[Reference, _Mapping]] = ...,
        second: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class SubmodelElementList(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "order_relevant",
        "semantic_id_list_element",
        "type_value_list_element",
        "value_type_list_element",
        "value",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    ORDER_RELEVANT_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_VALUE_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    order_relevant: bool
    semantic_id_list_element: Reference
    type_value_list_element: AasSubmodelElements
    value_type_list_element: DataTypeDefXsd
    value: _containers.RepeatedCompositeFieldContainer[SubmodelElement_choice]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        order_relevant: bool = ...,
        semantic_id_list_element: _Optional[_Union[Reference, _Mapping]] = ...,
        type_value_list_element: _Optional[_Union[AasSubmodelElements, str]] = ...,
        value_type_list_element: _Optional[_Union[DataTypeDefXsd, str]] = ...,
        value: _Optional[_Iterable[_Union[SubmodelElement_choice, _Mapping]]] = ...,
    ) -> None: ...

class SubmodelElementCollection(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value: _containers.RepeatedCompositeFieldContainer[SubmodelElement_choice]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value: _Optional[_Iterable[_Union[SubmodelElement_choice, _Mapping]]] = ...,
    ) -> None: ...

class Property(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value_type",
        "value",
        "value_id",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value_type: DataTypeDefXsd
    value: str
    value_id: Reference
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value_type: _Optional[_Union[DataTypeDefXsd, str]] = ...,
        value: _Optional[str] = ...,
        value_id: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class MultiLanguageProperty(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value",
        "value_id",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    value_id: Reference
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        value_id: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class Range(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value_type",
        "min",
        "max",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value_type: DataTypeDefXsd
    min: str
    max: str
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value_type: _Optional[_Union[DataTypeDefXsd, str]] = ...,
        min: _Optional[str] = ...,
        max: _Optional[str] = ...,
    ) -> None: ...

class ReferenceElement(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value: Reference
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class Blob(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value",
        "content_type",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value: bytes
    content_type: str
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value: _Optional[bytes] = ...,
        content_type: _Optional[str] = ...,
    ) -> None: ...

class File(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "value",
        "content_type",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    value: str
    content_type: str
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        value: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
    ) -> None: ...

class AnnotatedRelationshipElement(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "first",
        "second",
        "annotations",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    first: Reference
    second: Reference
    annotations: _containers.RepeatedCompositeFieldContainer[DataElement_choice]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        first: _Optional[_Union[Reference, _Mapping]] = ...,
        second: _Optional[_Union[Reference, _Mapping]] = ...,
        annotations: _Optional[_Iterable[_Union[DataElement_choice, _Mapping]]] = ...,
    ) -> None: ...

class Entity(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "statements",
        "entity_type",
        "global_asset_id",
        "specific_asset_ids",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_ASSET_IDS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    statements: _containers.RepeatedCompositeFieldContainer[SubmodelElement_choice]
    entity_type: EntityType
    global_asset_id: str
    specific_asset_ids: _containers.RepeatedCompositeFieldContainer[SpecificAssetId]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        statements: _Optional[
            _Iterable[_Union[SubmodelElement_choice, _Mapping]]
        ] = ...,
        entity_type: _Optional[_Union[EntityType, str]] = ...,
        global_asset_id: _Optional[str] = ...,
        specific_asset_ids: _Optional[
            _Iterable[_Union[SpecificAssetId, _Mapping]]
        ] = ...,
    ) -> None: ...

class EventPayload(_message.Message):
    __slots__ = (
        "source",
        "source_semantic_id",
        "observable_reference",
        "observable_semantic_id",
        "topic",
        "subject_id",
        "time_stamp",
        "payload",
    )
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    OBSERVABLE_SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    source: Reference
    source_semantic_id: Reference
    observable_reference: Reference
    observable_semantic_id: Reference
    topic: str
    subject_id: Reference
    time_stamp: str
    payload: bytes
    def __init__(
        self,
        source: _Optional[_Union[Reference, _Mapping]] = ...,
        source_semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        observable_reference: _Optional[_Union[Reference, _Mapping]] = ...,
        observable_semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        topic: _Optional[str] = ...,
        subject_id: _Optional[_Union[Reference, _Mapping]] = ...,
        time_stamp: _Optional[str] = ...,
        payload: _Optional[bytes] = ...,
    ) -> None: ...

class BasicEventElement(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "observed",
        "direction",
        "state",
        "message_topic",
        "message_broker",
        "last_update",
        "min_interval",
        "max_interval",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BROKER_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    MIN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MAX_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    observed: Reference
    direction: Direction
    state: StateOfEvent
    message_topic: str
    message_broker: Reference
    last_update: str
    min_interval: str
    max_interval: str
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        observed: _Optional[_Union[Reference, _Mapping]] = ...,
        direction: _Optional[_Union[Direction, str]] = ...,
        state: _Optional[_Union[StateOfEvent, str]] = ...,
        message_topic: _Optional[str] = ...,
        message_broker: _Optional[_Union[Reference, _Mapping]] = ...,
        last_update: _Optional[str] = ...,
        min_interval: _Optional[str] = ...,
        max_interval: _Optional[str] = ...,
    ) -> None: ...

class Operation(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
        "input_variables",
        "output_variables",
        "inoutput_variables",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    INOUTPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    input_variables: _containers.RepeatedCompositeFieldContainer[OperationVariable]
    output_variables: _containers.RepeatedCompositeFieldContainer[OperationVariable]
    inoutput_variables: _containers.RepeatedCompositeFieldContainer[OperationVariable]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        input_variables: _Optional[
            _Iterable[_Union[OperationVariable, _Mapping]]
        ] = ...,
        output_variables: _Optional[
            _Iterable[_Union[OperationVariable, _Mapping]]
        ] = ...,
        inoutput_variables: _Optional[
            _Iterable[_Union[OperationVariable, _Mapping]]
        ] = ...,
    ) -> None: ...

class OperationVariable(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: SubmodelElement_choice
    def __init__(
        self, value: _Optional[_Union[SubmodelElement_choice, _Mapping]] = ...
    ) -> None: ...

class Capability(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "semantic_id",
        "supplemental_semantic_ids",
        "qualifiers",
        "embedded_data_specifications",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_SEMANTIC_IDS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    semantic_id: Reference
    supplemental_semantic_ids: _containers.RepeatedCompositeFieldContainer[Reference]
    qualifiers: _containers.RepeatedCompositeFieldContainer[Qualifier]
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        supplemental_semantic_ids: _Optional[
            _Iterable[_Union[Reference, _Mapping]]
        ] = ...,
        qualifiers: _Optional[_Iterable[_Union[Qualifier, _Mapping]]] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
    ) -> None: ...

class ConceptDescription(_message.Message):
    __slots__ = (
        "extensions",
        "category",
        "id_short",
        "display_name",
        "description",
        "administration",
        "id",
        "embedded_data_specifications",
        "is_case_of",
    )
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ID_SHORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_DATA_SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    IS_CASE_OF_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    category: str
    id_short: str
    display_name: _containers.RepeatedCompositeFieldContainer[LangStringNameType]
    description: _containers.RepeatedCompositeFieldContainer[LangStringTextType]
    administration: AdministrativeInformation
    id: str
    embedded_data_specifications: _containers.RepeatedCompositeFieldContainer[
        EmbeddedDataSpecification
    ]
    is_case_of: _containers.RepeatedCompositeFieldContainer[Reference]
    def __init__(
        self,
        extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...,
        category: _Optional[str] = ...,
        id_short: _Optional[str] = ...,
        display_name: _Optional[_Iterable[_Union[LangStringNameType, _Mapping]]] = ...,
        description: _Optional[_Iterable[_Union[LangStringTextType, _Mapping]]] = ...,
        administration: _Optional[_Union[AdministrativeInformation, _Mapping]] = ...,
        id: _Optional[str] = ...,
        embedded_data_specifications: _Optional[
            _Iterable[_Union[EmbeddedDataSpecification, _Mapping]]
        ] = ...,
        is_case_of: _Optional[_Iterable[_Union[Reference, _Mapping]]] = ...,
    ) -> None: ...

class Reference(_message.Message):
    __slots__ = ("type", "referred_semantic_id", "keys")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERRED_SEMANTIC_ID_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    type: ReferenceTypes
    referred_semantic_id: Reference
    keys: _containers.RepeatedCompositeFieldContainer[Key]
    def __init__(
        self,
        type: _Optional[_Union[ReferenceTypes, str]] = ...,
        referred_semantic_id: _Optional[_Union[Reference, _Mapping]] = ...,
        keys: _Optional[_Iterable[_Union[Key, _Mapping]]] = ...,
    ) -> None: ...

class Key(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: KeyTypes
    value: str
    def __init__(
        self, type: _Optional[_Union[KeyTypes, str]] = ..., value: _Optional[str] = ...
    ) -> None: ...

class LangStringNameType(_message.Message):
    __slots__ = ("language", "text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language: str
    text: str
    def __init__(
        self, language: _Optional[str] = ..., text: _Optional[str] = ...
    ) -> None: ...

class LangStringTextType(_message.Message):
    __slots__ = ("language", "text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language: str
    text: str
    def __init__(
        self, language: _Optional[str] = ..., text: _Optional[str] = ...
    ) -> None: ...

class Environment(_message.Message):
    __slots__ = ("asset_administration_shells", "submodels", "concept_descriptions")
    ASSET_ADMINISTRATION_SHELLS_FIELD_NUMBER: _ClassVar[int]
    SUBMODELS_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    asset_administration_shells: _containers.RepeatedCompositeFieldContainer[
        AssetAdministrationShell
    ]
    submodels: _containers.RepeatedCompositeFieldContainer[Submodel]
    concept_descriptions: _containers.RepeatedCompositeFieldContainer[
        ConceptDescription
    ]
    def __init__(
        self,
        asset_administration_shells: _Optional[
            _Iterable[_Union[AssetAdministrationShell, _Mapping]]
        ] = ...,
        submodels: _Optional[_Iterable[_Union[Submodel, _Mapping]]] = ...,
        concept_descriptions: _Optional[
            _Iterable[_Union[ConceptDescription, _Mapping]]
        ] = ...,
    ) -> None: ...

class EmbeddedDataSpecification(_message.Message):
    __slots__ = ("data_specification_content", "data_specification")
    DATA_SPECIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    data_specification_content: DataSpecificationContent_choice
    data_specification: Reference
    def __init__(
        self,
        data_specification_content: _Optional[
            _Union[DataSpecificationContent_choice, _Mapping]
        ] = ...,
        data_specification: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class LevelType(_message.Message):
    __slots__ = ("min", "nom", "typ", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    NOM_FIELD_NUMBER: _ClassVar[int]
    TYP_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: bool
    nom: bool
    typ: bool
    max: bool
    def __init__(
        self, min: bool = ..., nom: bool = ..., typ: bool = ..., max: bool = ...
    ) -> None: ...

class ValueReferencePair(_message.Message):
    __slots__ = ("value", "value_id")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    value: str
    value_id: Reference
    def __init__(
        self,
        value: _Optional[str] = ...,
        value_id: _Optional[_Union[Reference, _Mapping]] = ...,
    ) -> None: ...

class ValueList(_message.Message):
    __slots__ = ("value_reference_pairs",)
    VALUE_REFERENCE_PAIRS_FIELD_NUMBER: _ClassVar[int]
    value_reference_pairs: _containers.RepeatedCompositeFieldContainer[
        ValueReferencePair
    ]
    def __init__(
        self,
        value_reference_pairs: _Optional[
            _Iterable[_Union[ValueReferencePair, _Mapping]]
        ] = ...,
    ) -> None: ...

class LangStringPreferredNameTypeIec61360(_message.Message):
    __slots__ = ("language", "text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language: str
    text: str
    def __init__(
        self, language: _Optional[str] = ..., text: _Optional[str] = ...
    ) -> None: ...

class LangStringShortNameTypeIec61360(_message.Message):
    __slots__ = ("language", "text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language: str
    text: str
    def __init__(
        self, language: _Optional[str] = ..., text: _Optional[str] = ...
    ) -> None: ...

class LangStringDefinitionTypeIec61360(_message.Message):
    __slots__ = ("language", "text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language: str
    text: str
    def __init__(
        self, language: _Optional[str] = ..., text: _Optional[str] = ...
    ) -> None: ...

class DataSpecificationIec61360(_message.Message):
    __slots__ = (
        "preferred_name",
        "short_name",
        "unit",
        "unit_id",
        "source_of_definition",
        "symbol",
        "data_type",
        "definition",
        "value_format",
        "value_list",
        "value",
        "level_type",
    )
    PREFERRED_NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OF_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VALUE_LIST_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    preferred_name: _containers.RepeatedCompositeFieldContainer[
        LangStringPreferredNameTypeIec61360
    ]
    short_name: _containers.RepeatedCompositeFieldContainer[
        LangStringShortNameTypeIec61360
    ]
    unit: str
    unit_id: Reference
    source_of_definition: str
    symbol: str
    data_type: DataTypeIec61360
    definition: _containers.RepeatedCompositeFieldContainer[
        LangStringDefinitionTypeIec61360
    ]
    value_format: str
    value_list: ValueList
    value: str
    level_type: LevelType
    def __init__(
        self,
        preferred_name: _Optional[
            _Iterable[_Union[LangStringPreferredNameTypeIec61360, _Mapping]]
        ] = ...,
        short_name: _Optional[
            _Iterable[_Union[LangStringShortNameTypeIec61360, _Mapping]]
        ] = ...,
        unit: _Optional[str] = ...,
        unit_id: _Optional[_Union[Reference, _Mapping]] = ...,
        source_of_definition: _Optional[str] = ...,
        symbol: _Optional[str] = ...,
        data_type: _Optional[_Union[DataTypeIec61360, str]] = ...,
        definition: _Optional[
            _Iterable[_Union[LangStringDefinitionTypeIec61360, _Mapping]]
        ] = ...,
        value_format: _Optional[str] = ...,
        value_list: _Optional[_Union[ValueList, _Mapping]] = ...,
        value: _Optional[str] = ...,
        level_type: _Optional[_Union[LevelType, _Mapping]] = ...,
    ) -> None: ...

class HasSemantics_choice(_message.Message):
    __slots__ = (
        "relationship_element",
        "annotated_relationship_element",
        "basic_event_element",
        "blob",
        "capability",
        "entity",
        "extension",
        "file",
        "multi_language_property",
        "operation",
        "property",
        "qualifier",
        "range",
        "reference_element",
        "specific_asset_id",
        "submodel",
        "submodel_element_collection",
        "submodel_element_list",
    )
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    basic_event_element: BasicEventElement
    blob: Blob
    capability: Capability
    entity: Entity
    extension: Extension
    file: File
    multi_language_property: MultiLanguageProperty
    operation: Operation
    property: Property
    qualifier: Qualifier
    range: Range
    reference_element: ReferenceElement
    specific_asset_id: SpecificAssetId
    submodel: Submodel
    submodel_element_collection: SubmodelElementCollection
    submodel_element_list: SubmodelElementList
    def __init__(
        self,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
        basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        capability: _Optional[_Union[Capability, _Mapping]] = ...,
        entity: _Optional[_Union[Entity, _Mapping]] = ...,
        extension: _Optional[_Union[Extension, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        operation: _Optional[_Union[Operation, _Mapping]] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        qualifier: _Optional[_Union[Qualifier, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
        specific_asset_id: _Optional[_Union[SpecificAssetId, _Mapping]] = ...,
        submodel: _Optional[_Union[Submodel, _Mapping]] = ...,
        submodel_element_collection: _Optional[
            _Union[SubmodelElementCollection, _Mapping]
        ] = ...,
        submodel_element_list: _Optional[_Union[SubmodelElementList, _Mapping]] = ...,
    ) -> None: ...

class HasExtensions_choice(_message.Message):
    __slots__ = (
        "relationship_element",
        "annotated_relationship_element",
        "asset_administration_shell",
        "basic_event_element",
        "blob",
        "capability",
        "concept_description",
        "entity",
        "file",
        "multi_language_property",
        "operation",
        "property",
        "range",
        "reference_element",
        "submodel",
        "submodel_element_collection",
        "submodel_element_list",
    )
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_ADMINISTRATION_SHELL_FIELD_NUMBER: _ClassVar[int]
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    asset_administration_shell: AssetAdministrationShell
    basic_event_element: BasicEventElement
    blob: Blob
    capability: Capability
    concept_description: ConceptDescription
    entity: Entity
    file: File
    multi_language_property: MultiLanguageProperty
    operation: Operation
    property: Property
    range: Range
    reference_element: ReferenceElement
    submodel: Submodel
    submodel_element_collection: SubmodelElementCollection
    submodel_element_list: SubmodelElementList
    def __init__(
        self,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
        asset_administration_shell: _Optional[
            _Union[AssetAdministrationShell, _Mapping]
        ] = ...,
        basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        capability: _Optional[_Union[Capability, _Mapping]] = ...,
        concept_description: _Optional[_Union[ConceptDescription, _Mapping]] = ...,
        entity: _Optional[_Union[Entity, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        operation: _Optional[_Union[Operation, _Mapping]] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
        submodel: _Optional[_Union[Submodel, _Mapping]] = ...,
        submodel_element_collection: _Optional[
            _Union[SubmodelElementCollection, _Mapping]
        ] = ...,
        submodel_element_list: _Optional[_Union[SubmodelElementList, _Mapping]] = ...,
    ) -> None: ...

class Referable_choice(_message.Message):
    __slots__ = (
        "relationship_element",
        "annotated_relationship_element",
        "asset_administration_shell",
        "basic_event_element",
        "blob",
        "capability",
        "concept_description",
        "entity",
        "file",
        "multi_language_property",
        "operation",
        "property",
        "range",
        "reference_element",
        "submodel",
        "submodel_element_collection",
        "submodel_element_list",
    )
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_ADMINISTRATION_SHELL_FIELD_NUMBER: _ClassVar[int]
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    asset_administration_shell: AssetAdministrationShell
    basic_event_element: BasicEventElement
    blob: Blob
    capability: Capability
    concept_description: ConceptDescription
    entity: Entity
    file: File
    multi_language_property: MultiLanguageProperty
    operation: Operation
    property: Property
    range: Range
    reference_element: ReferenceElement
    submodel: Submodel
    submodel_element_collection: SubmodelElementCollection
    submodel_element_list: SubmodelElementList
    def __init__(
        self,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
        asset_administration_shell: _Optional[
            _Union[AssetAdministrationShell, _Mapping]
        ] = ...,
        basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        capability: _Optional[_Union[Capability, _Mapping]] = ...,
        concept_description: _Optional[_Union[ConceptDescription, _Mapping]] = ...,
        entity: _Optional[_Union[Entity, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        operation: _Optional[_Union[Operation, _Mapping]] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
        submodel: _Optional[_Union[Submodel, _Mapping]] = ...,
        submodel_element_collection: _Optional[
            _Union[SubmodelElementCollection, _Mapping]
        ] = ...,
        submodel_element_list: _Optional[_Union[SubmodelElementList, _Mapping]] = ...,
    ) -> None: ...

class Identifiable_choice(_message.Message):
    __slots__ = ("asset_administration_shell", "concept_description", "submodel")
    ASSET_ADMINISTRATION_SHELL_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    asset_administration_shell: AssetAdministrationShell
    concept_description: ConceptDescription
    submodel: Submodel
    def __init__(
        self,
        asset_administration_shell: _Optional[
            _Union[AssetAdministrationShell, _Mapping]
        ] = ...,
        concept_description: _Optional[_Union[ConceptDescription, _Mapping]] = ...,
        submodel: _Optional[_Union[Submodel, _Mapping]] = ...,
    ) -> None: ...

class HasKind_choice(_message.Message):
    __slots__ = ("submodel",)
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    submodel: Submodel
    def __init__(
        self, submodel: _Optional[_Union[Submodel, _Mapping]] = ...
    ) -> None: ...

class HasDataSpecification_choice(_message.Message):
    __slots__ = (
        "administrative_information",
        "relationship_element",
        "annotated_relationship_element",
        "asset_administration_shell",
        "basic_event_element",
        "blob",
        "capability",
        "concept_description",
        "entity",
        "file",
        "multi_language_property",
        "operation",
        "property",
        "range",
        "reference_element",
        "submodel",
        "submodel_element_collection",
        "submodel_element_list",
    )
    ADMINISTRATIVE_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_ADMINISTRATION_SHELL_FIELD_NUMBER: _ClassVar[int]
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    administrative_information: AdministrativeInformation
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    asset_administration_shell: AssetAdministrationShell
    basic_event_element: BasicEventElement
    blob: Blob
    capability: Capability
    concept_description: ConceptDescription
    entity: Entity
    file: File
    multi_language_property: MultiLanguageProperty
    operation: Operation
    property: Property
    range: Range
    reference_element: ReferenceElement
    submodel: Submodel
    submodel_element_collection: SubmodelElementCollection
    submodel_element_list: SubmodelElementList
    def __init__(
        self,
        administrative_information: _Optional[
            _Union[AdministrativeInformation, _Mapping]
        ] = ...,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
        asset_administration_shell: _Optional[
            _Union[AssetAdministrationShell, _Mapping]
        ] = ...,
        basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        capability: _Optional[_Union[Capability, _Mapping]] = ...,
        concept_description: _Optional[_Union[ConceptDescription, _Mapping]] = ...,
        entity: _Optional[_Union[Entity, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        operation: _Optional[_Union[Operation, _Mapping]] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
        submodel: _Optional[_Union[Submodel, _Mapping]] = ...,
        submodel_element_collection: _Optional[
            _Union[SubmodelElementCollection, _Mapping]
        ] = ...,
        submodel_element_list: _Optional[_Union[SubmodelElementList, _Mapping]] = ...,
    ) -> None: ...

class Qualifiable_choice(_message.Message):
    __slots__ = (
        "relationship_element",
        "annotated_relationship_element",
        "basic_event_element",
        "blob",
        "capability",
        "entity",
        "file",
        "multi_language_property",
        "operation",
        "property",
        "range",
        "reference_element",
        "submodel",
        "submodel_element_collection",
        "submodel_element_list",
    )
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    basic_event_element: BasicEventElement
    blob: Blob
    capability: Capability
    entity: Entity
    file: File
    multi_language_property: MultiLanguageProperty
    operation: Operation
    property: Property
    range: Range
    reference_element: ReferenceElement
    submodel: Submodel
    submodel_element_collection: SubmodelElementCollection
    submodel_element_list: SubmodelElementList
    def __init__(
        self,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
        basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        capability: _Optional[_Union[Capability, _Mapping]] = ...,
        entity: _Optional[_Union[Entity, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        operation: _Optional[_Union[Operation, _Mapping]] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
        submodel: _Optional[_Union[Submodel, _Mapping]] = ...,
        submodel_element_collection: _Optional[
            _Union[SubmodelElementCollection, _Mapping]
        ] = ...,
        submodel_element_list: _Optional[_Union[SubmodelElementList, _Mapping]] = ...,
    ) -> None: ...

class SubmodelElement_choice(_message.Message):
    __slots__ = (
        "relationship_element",
        "annotated_relationship_element",
        "basic_event_element",
        "blob",
        "capability",
        "entity",
        "file",
        "multi_language_property",
        "operation",
        "property",
        "range",
        "reference_element",
        "submodel_element_collection",
        "submodel_element_list",
    )
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUBMODEL_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    basic_event_element: BasicEventElement
    blob: Blob
    capability: Capability
    entity: Entity
    file: File
    multi_language_property: MultiLanguageProperty
    operation: Operation
    property: Property
    range: Range
    reference_element: ReferenceElement
    submodel_element_collection: SubmodelElementCollection
    submodel_element_list: SubmodelElementList
    def __init__(
        self,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
        basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        capability: _Optional[_Union[Capability, _Mapping]] = ...,
        entity: _Optional[_Union[Entity, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        operation: _Optional[_Union[Operation, _Mapping]] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
        submodel_element_collection: _Optional[
            _Union[SubmodelElementCollection, _Mapping]
        ] = ...,
        submodel_element_list: _Optional[_Union[SubmodelElementList, _Mapping]] = ...,
    ) -> None: ...

class RelationshipElement_choice(_message.Message):
    __slots__ = ("relationship_element", "annotated_relationship_element")
    RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_RELATIONSHIP_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    relationship_element: RelationshipElement
    annotated_relationship_element: AnnotatedRelationshipElement
    def __init__(
        self,
        relationship_element: _Optional[_Union[RelationshipElement, _Mapping]] = ...,
        annotated_relationship_element: _Optional[
            _Union[AnnotatedRelationshipElement, _Mapping]
        ] = ...,
    ) -> None: ...

class DataElement_choice(_message.Message):
    __slots__ = (
        "blob",
        "file",
        "multi_language_property",
        "property",
        "range",
        "reference_element",
    )
    BLOB_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    blob: Blob
    file: File
    multi_language_property: MultiLanguageProperty
    property: Property
    range: Range
    reference_element: ReferenceElement
    def __init__(
        self,
        blob: _Optional[_Union[Blob, _Mapping]] = ...,
        file: _Optional[_Union[File, _Mapping]] = ...,
        multi_language_property: _Optional[
            _Union[MultiLanguageProperty, _Mapping]
        ] = ...,
        property: _Optional[_Union[Property, _Mapping]] = ...,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        reference_element: _Optional[_Union[ReferenceElement, _Mapping]] = ...,
    ) -> None: ...

class EventElement_choice(_message.Message):
    __slots__ = ("basic_event_element",)
    BASIC_EVENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    basic_event_element: BasicEventElement
    def __init__(
        self, basic_event_element: _Optional[_Union[BasicEventElement, _Mapping]] = ...
    ) -> None: ...

class AbstractLangString_choice(_message.Message):
    __slots__ = (
        "lang_string_definition_type_iec_61360",
        "lang_string_name_type",
        "lang_string_preferred_name_type_iec_61360",
        "lang_string_short_name_type_iec_61360",
        "lang_string_text_type",
    )
    LANG_STRING_DEFINITION_TYPE_IEC_61360_FIELD_NUMBER: _ClassVar[int]
    LANG_STRING_NAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANG_STRING_PREFERRED_NAME_TYPE_IEC_61360_FIELD_NUMBER: _ClassVar[int]
    LANG_STRING_SHORT_NAME_TYPE_IEC_61360_FIELD_NUMBER: _ClassVar[int]
    LANG_STRING_TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
    lang_string_definition_type_iec_61360: LangStringDefinitionTypeIec61360
    lang_string_name_type: LangStringNameType
    lang_string_preferred_name_type_iec_61360: LangStringPreferredNameTypeIec61360
    lang_string_short_name_type_iec_61360: LangStringShortNameTypeIec61360
    lang_string_text_type: LangStringTextType
    def __init__(
        self,
        lang_string_definition_type_iec_61360: _Optional[
            _Union[LangStringDefinitionTypeIec61360, _Mapping]
        ] = ...,
        lang_string_name_type: _Optional[_Union[LangStringNameType, _Mapping]] = ...,
        lang_string_preferred_name_type_iec_61360: _Optional[
            _Union[LangStringPreferredNameTypeIec61360, _Mapping]
        ] = ...,
        lang_string_short_name_type_iec_61360: _Optional[
            _Union[LangStringShortNameTypeIec61360, _Mapping]
        ] = ...,
        lang_string_text_type: _Optional[_Union[LangStringTextType, _Mapping]] = ...,
    ) -> None: ...

class DataSpecificationContent_choice(_message.Message):
    __slots__ = ("data_specification_iec_61360",)
    DATA_SPECIFICATION_IEC_61360_FIELD_NUMBER: _ClassVar[int]
    data_specification_iec_61360: DataSpecificationIec61360
    def __init__(
        self,
        data_specification_iec_61360: _Optional[
            _Union[DataSpecificationIec61360, _Mapping]
        ] = ...,
    ) -> None: ...
