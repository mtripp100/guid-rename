import tempfile
from os import listdir
from os.path import isfile, join

from guid_rename import rename


def _generate_files(dirname, num_files):
    for _ in range(num_files):
        with tempfile.NamedTemporaryFile(delete=False, dir=dirname):
            pass


def test_generation(tmp_dir):
    _generate_files(tmp_dir, 500)

    files = listdir(tmp_dir)
    rename.rename_all(tmp_dir, files)

    files = listdir(tmp_dir)
    assert len(files) == 500
    assert all(isfile(join(tmp_dir, f)) for f in files)
    assert all(len(f) == 36 for f in files)
