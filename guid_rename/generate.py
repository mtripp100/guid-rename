import os
import sys
import tempfile


def generate_files(dirname, num_files):
    os.mkdir(dirname)
    for _ in range(num_files):
        with tempfile.NamedTemporaryFile(delete=False, dir=dirname):
            pass

    return dirname


if __name__ == "__main__":
    generate_files(sys.argv[1], int(sys.argv[2]))
