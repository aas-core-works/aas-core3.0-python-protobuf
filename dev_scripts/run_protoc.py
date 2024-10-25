"""Run protoc to (re-)generate the Python code for handling AAS ProtoBufs."""

import argparse
import os
import pathlib
import shlex
import shutil
import subprocess
import sys


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    this_path = pathlib.Path(os.path.realpath(__file__))

    if shutil.which("protoc") is None:
        print(
            "The ProtoBuf compiler could not be found using `shutil.which` "
            "on `protoc`. Have you installed it on your system and does it reside on "
            "your PATH?",
            file=sys.stderr,
        )
        return 1

    cmd = [
        "protoc",
        "--proto_path",
        str(this_path.parent / "proto"),
        "--python_out",
        str(this_path.parent.parent / "aas_core3_protobuf"),
        "--pyi_out",
        str(this_path.parent.parent / "aas_core3_protobuf"),
        str(this_path.parent / "proto/types.proto"),
    ]

    completed = subprocess.run(cmd, cwd=str(this_path.parent), check=False)
    if completed.returncode != 0:
        cmd_joined = " ".join(shlex.quote(part) for part in cmd)
        print(
            f"Failed to run with exit code {completed.returncode}: {cmd_joined}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
