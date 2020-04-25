from os import listdir
import os
from os.path import isfile, join
import tempfile


def _generate_files(dirname, num):
    for _ in range(num):
        fd, name = tempfile.mkstemp(dir=dirname)
        os.close()


def test_generation(tmp_dir):
    _generate_files(tmp_dir, 500)

    files = [f for f in listdir(tmp_dir) if isfile(join(tmp_dir, f))]
    print(files)
