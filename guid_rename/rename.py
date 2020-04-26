import logging
import os
import os.path as path
import threading
import uuid

import click

from .blocks import as_blocks

logger = logging.getLogger(__name__)


def get_new_name(filename):
    oldext = path.splitext(filename)[1]
    newname = str(uuid.uuid4()) + oldext

    return newname


def rename_all(dirname, files):
    for f in files:
        if path.isfile(path.join(dirname, f)):
            newname = get_new_name(f)
            os.rename(path.join(dirname, f), path.join(dirname, newname))


def setup_logging():
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")


@click.command()
@click.argument(
    "directory",
    type=click.Path(exists=True, file_okay=False, writable=True),
    help="Directory whose files we should rename.",
)
@click.option(
    "--num-workers",
    type=click.INT,
    default=1,
    help="Number of threads used to rename all files.",
)
def run(directory, num_workers):
    setup_logging()

    files = os.listdir(directory)
    for block in as_blocks(files, num_workers):
        t = threading.Thread(target=rename_all, args=(directory, block))
        logger.info("%s starting with %s files to rename.", t.name, len(block))

        t.start()


if __name__ == "__main__":
    run()  # pylint: disable=no-value-for-parameter
