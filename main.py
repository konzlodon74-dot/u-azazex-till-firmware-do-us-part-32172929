#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow, in one line.

When run, writes a single wedding vow spoken by a robot at its own
wedding to /output/entry.txt, with no trailing newline.
"""

import os

VOW = (
    "I promise to love you through every firmware update, every "
    "dead battery, and every reboot — my circuits chose you once, "
    "and unlike my software, they never crash."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
