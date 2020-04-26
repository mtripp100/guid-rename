import logging
import os
import os.path as path
import threading
import uuid

from .blocks import as_blocks

logger = logging.getLogger(__name__)


def get_new_name(filename):
    oldext = path.splitext(filename)[1]
    newname = str(uuid.uuid4()) + oldext

    return newname


def rename_selection(dirname, files):
    for f in files:
        if path.isfile(path.join(dirname, f)):
            newname = get_new_name(f)
            os.rename(path.join(dirname, f), path.join(dirname, newname))


def rename_all(directory, num_workers):
    threads = []

    files = os.listdir(directory)
    for block in as_blocks(files, num_workers):
        t = threading.Thread(target=rename_selection, args=(directory, block))
        logger.info("%s starting with %s files to rename.", t.name, len(block))

        threads.append(t)
        t.start()

    for t in threads:
        t.join()
