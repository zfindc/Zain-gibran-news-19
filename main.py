"""Entry program for the make.fun bounty "Sum up 19 November's world
news in one image" (news-image-20261119).

The artwork ships inside this repository as ``art.jpg``: a newspaper
front page whose lead story is Vice President Gibran Rakabuming Raka
handing his resignation letter to the MPR, with side panels on the
court rulings about his school papers, the 120 lawmakers who pushed
impeachment, and the 60-day window to choose a successor.

The harness runs this file with no network and expects exactly one
image at ``/output/entry.png``. The stored JPEG already satisfies the
size limits (1024x1024, well under 1 MiB), so publishing the entry is
just a faithful byte-for-byte copy: nothing is re-encoded, which also
keeps repeated runs byte-identical.
"""

import os
import shutil

# The artwork lives next to this script, wherever the repo was unpacked.
HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "art.jpg")

# Fixed destination the grader reads.
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    # Make sure the destination folder exists before copying into it.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Copy the bytes untouched so the judged image is exactly the
    # artwork committed in this repository.
    shutil.copyfile(SOURCE, OUTPUT_FILE)
    # A faithful copy is the whole contract of this program, so verify
    # it before reporting success: if the written file's size differs
    # from the source's, the copy was cut short and the run must fail
    # loudly instead of handing the grader a truncated image.
    if os.path.getsize(OUTPUT_FILE) != os.path.getsize(SOURCE):
        raise IOError("copied entry image does not match art.jpg in size")


if __name__ == "__main__":
    main()
