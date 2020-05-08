import logging

import click

from .rename import rename_all


def setup_logging():
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")


@click.command()
@click.argument(
    "directory", type=click.Path(exists=True, file_okay=False, writable=True),
)
@click.option(
    "--num-workers", type=click.INT, default=1, help="Number of threads used to rename all files.",
)
def run(directory, num_workers):
    setup_logging()

    rename_all(directory, num_workers)


if __name__ == "__main__":
    run()  # pylint: disable=no-value-for-parameter
