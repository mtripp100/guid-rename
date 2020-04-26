import os
import os.path as path
import tempfile
import uuid

import pytest

from guid_rename import rename


def _generate_files(dirname, num_files):
    for _ in range(num_files):
        with tempfile.NamedTemporaryFile(delete=False, dir=dirname):
            pass


@pytest.mark.slow
@pytest.mark.parametrize("num_files", [
    1, 10, 100, 1000, 10000
])
def test_generation(tmp_dir, num_files):
    _generate_files(tmp_dir, num_files)

    files = os.listdir(tmp_dir)
    rename.rename_all(tmp_dir, files)

    files = os.listdir(tmp_dir)
    assert len(files) == num_files

    for f in files:
        assert path.isfile(path.join(tmp_dir, f))

        basename = path.splitext(f)[0]
        assert uuid.UUID(basename)


@pytest.mark.parametrize("old_name", [
    "hello"
])
def test_no_extension(old_name):
    f = rename.get_new_name(old_name)
    assert uuid.UUID(f)


@pytest.mark.parametrize("old_name", [
    "hello.f", "hello.txt", "hello.txt.txt"
])
def test_with_extension(old_name):
    f = rename.get_new_name(old_name)

    original_ext = path.splitext(old_name)[1]
    new_ext = path.splitext(f)[1]

    assert original_ext == new_ext
    assert uuid.UUID(path.splitext(f)[0])
