from os import path
import os
import sys
import uuid


def rename_all(place, files):
    for f in files:
        oldext = path.splitext(f)[1]
        os.rename(path.join(place, f), path.join(place, str(uuid.uuid4()) + oldext))


if __name__ == "__main__":
    place = sys.argv[1]
    files = [f for f in os.listdir(place) if path.isfile(path.join(place, f))]
    rename_all(place, files)
