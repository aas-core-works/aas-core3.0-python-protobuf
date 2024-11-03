"""Run the pbization generation."""

import argparse
import os
import pathlib
import sys

import aas_core_meta.v3
import aas_core_codegen.main


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    assert aas_core_meta.v3.__file__ is not None

    this_path = pathlib.Path(os.path.realpath(__file__))

    return aas_core_codegen.main.execute(
        aas_core_codegen.main.Parameters(
            model_path=pathlib.Path(aas_core_meta.v3.__file__),
            target=aas_core_codegen.main.Target.PYTHON_PROTOBUF,
            snippets_dir=this_path.parent / "snippets",
            output_dir=this_path.parent.parent / "aas_core3_protobuf",
        ),
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


if __name__ == "__main__":
    sys.exit(main())
