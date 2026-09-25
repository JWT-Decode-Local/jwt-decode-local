"""JWT Decode Local — Decode a JWT payload locally and print claims without verifying a signature."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='jwt_decode_local',
        description='Decode a JWT payload locally and print claims without verifying a signature.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('JWT Decode Local')
    print('Read claims. It does not treat the token as trusted.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
