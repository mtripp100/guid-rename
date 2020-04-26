import os
import os.path as path
import sys
import threading
import uuid

from .blocks import as_blocks


def get_new_name(filename):
    oldext = path.splitext(filename)[1]
    newname = str(uuid.uuid4()) + oldext

    return newname


def rename_all(dirname, files):
    for f in files:
        if path.isfile(path.join(dirname, f)):
            newname = get_new_name(f)
            os.rename(path.join(dirname, f), path.join(dirname, newname))


if __name__ == "__main__":
    dirname = sys.argv[1]
    files = os.listdir(dirname)

    num_workers = int(sys.argv[2])
    for block in as_blocks(files, num_workers):
        t = threading.Thread(target=rename_all, args=(dirname, block))
        print(f"{t.name} starting with {len(block)} files to rename.")

        t.start()
