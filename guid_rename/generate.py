import tempfile
import sys
import os


def generate_files(dirname, n):
    os.mkdir(dirname)
    for _ in range(n):
        with tempfile.NamedTemporaryFile(delete=False, dir=dirname):
            pass

    return dirname


if __name__ == "__main__":
    generate_files(sys.argv[1], int(sys.argv[2]))
