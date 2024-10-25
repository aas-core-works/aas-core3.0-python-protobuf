"""Download the definitions file from the aas-core-protobuf repository."""

import argparse
import datetime
import os
import pathlib
import sys
import urllib.request


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--revision",
        help="Revision hash or branch name on https://github.com/aas-core-works/aas-core-protobuf",
        default="main",
    )
    args = parser.parse_args()
    revision = str(args.revision)

    this_path = pathlib.Path(os.path.realpath(__file__))

    url = (
        f"https://raw.githubusercontent.com/aas-core-works/aas-core-protobuf/"
        f"{revision}/v3/types.proto"
    )

    target_path = this_path.parent / "proto/types.proto"

    print(f"Downloading from: {url}")
    now = datetime.datetime.now(datetime.timezone.utc)

    with urllib.request.urlopen(url) as response:
        text = response.read().decode("utf-8")

    print(f"Saving to: {target_path}")
    with target_path.open("wt", encoding="utf-8") as fid:
        now_str = now.strftime("%Y-%m-%d %H:%M:%SZ")
        fid.write(f"// Downloaded from: {url}\n" f"// At: {now_str}\n\n")
        fid.write(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
