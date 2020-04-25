import os
import os.path as path
import sys
import threading
import uuid


def as_blocks(blocks, workers):
    min_size = len(blocks) // workers
    extra = len(blocks) % workers

    start = 0
    for _ in range(workers):
        end = min_size + (1 if extra > 0 else 0)
        yield blocks[start:start + end]
        start += end

        if extra > 0:
            extra -= 1


def rename_all(dirname, files):
    for f in files:
        if path.isfile(path.join(dirname, f)):
            oldext = path.splitext(f)[1]
            newname = str(uuid.uuid4()) + oldext
            os.rename(path.join(dirname, f), path.join(dirname, newname))


if __name__ == "__main__":
    dirname = sys.argv[1]
    files = os.listdir(dirname)

    num_workers = int(sys.argv[2])
    for block in as_blocks(files, num_workers):
        t = threading.Thread(target=rename_all, args=(dirname, block))
        print(f"{t.name} starting with {len(block)} files to rename.")

        t.start()
