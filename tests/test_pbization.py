# pylint: disable=missing-docstring
import json
import os.path
import pathlib
import unittest

import aas_core3.xmlization as aas_xmlization
import aas_core3.jsonization as aas_jsonization

import aas_core3_protobuf.pbization as aas_pbization


class TestEndToEnd(unittest.TestCase):
    def test_on_test_data_contained_in_environment(self) -> None:
        this_file = pathlib.Path(os.path.realpath(__file__))
        expected_dir = this_file.parent.parent / "test_data/Xml"

        for xml_path in sorted(expected_dir.glob("*/**/*.xml")):
            instance = aas_xmlization.from_file(xml_path)

            # NOTE (mristin):
            # We canonicalize the instance as JSON for easier debugging — it is quite
            # hard to diff two XML documents as texts.
            expected_json = json.dumps(
                aas_jsonization.to_jsonable(instance), sort_keys=True, indent=2
            )

            instance_pb = aas_pbization.to_pb(instance)

            data = instance_pb.SerializeToString()

            another_instance_pb = instance_pb.__class__.FromString(data)

            another_instance = aas_pbization.from_pb(another_instance_pb)

            got_json = json.dumps(
                aas_jsonization.to_jsonable(another_instance), sort_keys=True, indent=2
            )

            self.assertEqual(
                expected_json, got_json, f"Round trip for the example: {xml_path}"
            )


if __name__ == "__main__":
    unittest.main()
