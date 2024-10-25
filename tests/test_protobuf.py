"""
Test that the basic protobuf functions work.

This is just a very first test to establish that the basic ProtoBuf functionality
is in place.
"""

# pylint: disable=missing-docstring

import unittest

import aas_core3_protobuf.types_pb2 as aas_types_pb


class TestBasicProtobuf(unittest.TestCase):
    def test_empty_environment(self) -> None:
        environment = aas_types_pb.Environment()

        data = environment.SerializeToString()
        self.assertEqual(b"", data)

    def test_submodel_in_environment(self) -> None:
        environment = aas_types_pb.Environment()

        submodel = aas_types_pb.Submodel(id="urn:something")
        environment.submodels.append(submodel)

        data = environment.SerializeToString()
        self.assertEqual(b"\x12\x0f:\rurn:something", data)

        self.assertEqual(environment.__class__, aas_types_pb.Environment)
        assert isinstance(environment, aas_types_pb.Environment)

        another_environment = aas_types_pb.Environment.FromString(data)
        self.assertEqual("urn:something", another_environment.submodels[0].id)

    def test_construction_with_kwargs(self) -> None:
        environment = aas_types_pb.Environment(
            submodels=[aas_types_pb.Submodel(id="urn:something")]
        )

        data = environment.SerializeToString()
        self.assertEqual(b"\x12\x0f:\rurn:something", data)

    def test_enum(self) -> None:
        prop = aas_types_pb.Property(
            id_short="something",
            value_type=aas_types_pb.DataTypeDefXsd.Datatypedefxsd_G_MONTH_DAY,
        )

        data = prop.SerializeToString()
        self.assertEqual(b"\x1a\tsomethingP\r", data)

    def test_enum_from_pb_in_map(self) -> None:
        key = aas_types_pb.DataTypeDefXsd.Datatypedefxsd_G_MONTH_DAY

        mapping = {aas_types_pb.DataTypeDefXsd.Datatypedefxsd_G_MONTH_DAY: 2}

        value = mapping[key]

        self.assertEqual(2, value)

    def test_faux_polymorphism_with_submodel_element(self) -> None:
        prop = aas_types_pb.Property(id_short="something")

        submodel_element = aas_types_pb.SubmodelElement_choice(property=prop)

        data = submodel_element.SerializeToString()
        self.assertEqual(b"R\x0b\x1a\tsomething", data)

    # noinspection SpellCheckingInspection
    def test_faux_polymorphism_with_submodel_element_can_be_opaque(self) -> None:
        prop = aas_types_pb.Property(id_short="something")
        rnge = aas_types_pb.Range(id_short="somethingElse")

        submodel_element = aas_types_pb.SubmodelElement_choice(
            property=prop, range=rnge
        )

        self.assertEqual("range", submodel_element.WhichOneof("value"))

        self.assertEqual("somethingElse", submodel_element.range.id_short)

        data = submodel_element.SerializeToString()
        self.assertEqual(b"Z\x0f\x1a\rsomethingElse", data)

    def test_setting_a_choice_class(self) -> None:
        submodel_element = aas_types_pb.SubmodelElement_choice()

        assert not submodel_element.HasField("value")
        assert submodel_element.WhichOneof("value") is None

        # NOTE (mristin):
        # The value will be created on demand.

        submodel_element.property.id_short = "some-id-short"

        assert submodel_element.HasField("value")
        self.assertEqual("property", submodel_element.WhichOneof("value"))

    def test_passing_value_in_choice_classes_created_on_demand(self) -> None:
        def populate(prop: aas_types_pb.Property) -> None:
            prop.id_short = "some-id-short"

        submodel_element = aas_types_pb.SubmodelElement_choice()

        assert not submodel_element.HasField("value")
        assert submodel_element.WhichOneof("value") is None

        # NOTE (mristin):
        # The value will be created on demand.

        populate(submodel_element.property)

        assert submodel_element.HasField("value")
        self.assertEqual("property", submodel_element.WhichOneof("value"))
        self.assertEqual("some-id-short", submodel_element.property.id_short)

    def test_dispatch_on_runtime_class(self) -> None:
        prop = aas_types_pb.Property(id_short="something")
        some_range = aas_types_pb.Range(id_short="somethingElse")

        mapping = {
            aas_types_pb.Property: "It is a property.",
            aas_types_pb.Range: "It is a range.",
        }

        self.assertEqual("It is a property.", mapping[prop.__class__])
        self.assertEqual("It is a range.", mapping[some_range.__class__])

    def test_optional_field_check(self) -> None:
        smel = aas_types_pb.SubmodelElementList()
        assert not smel.HasField("id_short")
        assert not smel.HasField("order_relevant")

        smel.order_relevant = False
        assert smel.HasField("order_relevant")

        smel.ClearField("order_relevant")
        assert not smel.HasField("order_relevant")

    def test_list_assignment_is_not_possible(self) -> None:
        env = aas_types_pb.Environment()

        try:
            env.submodels = [aas_types_pb.Submodel(id="some-id")]  # type: ignore
            raise AssertionError("Expected to raise before")
        except AttributeError:
            pass

    def test_add_to_list(self) -> None:
        env = aas_types_pb.Environment()

        submodel = env.submodels.add()
        submodel.id = "some_id"

        self.assertEqual(1, len(env.submodels))

    def test_assignment_to_nested_message_not_possible(self) -> None:
        admin_info = aas_types_pb.AdministrativeInformation()

        creator = aas_types_pb.Reference(
            type=aas_types_pb.ReferenceTypes.Referencetypes_EXTERNAL_REFERENCE
        )

        try:
            admin_info.creator = creator
            raise AssertionError("Expected to raise before")
        except AttributeError:
            pass

    def test_set_nested_message(self) -> None:
        admin_info = aas_types_pb.AdministrativeInformation()

        assert not admin_info.HasField("creator")

        # NOTE (mristin):
        # The nested messages will be created on demand.
        admin_info.creator.type = (
            aas_types_pb.ReferenceTypes.Referencetypes_EXTERNAL_REFERENCE
        )

        assert admin_info.HasField("creator")

    def test_clearing_a_field_and_has_field(self) -> None:
        aas = aas_types_pb.AssetAdministrationShell()

        assert not aas.HasField("administration")

        # NOTE (mristin):
        # This will create an empty administration.
        aas.administration.Clear()

        assert aas.HasField("administration")


if __name__ == "__main__":
    unittest.main()
