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


def _generate_tmpdir(dirname):
    return tempfile.mkdtemp(dir=dirname)


@pytest.mark.slow
@pytest.mark.parametrize("num_files", [1, 10, 100, 1000])
def test_generation(tmp_dir, num_files):
    _generate_files(tmp_dir, num_files)

    rename.rename_selection(tmp_dir, os.listdir(tmp_dir))

    files = os.listdir(tmp_dir)
    assert len(files) == num_files

    for f in files:
        assert path.isfile(path.join(tmp_dir, f))

        basename = path.splitext(f)[0]
        assert uuid.UUID(basename)


@pytest.mark.slow
@pytest.mark.parametrize(
    "num_files, num_workers", [(10, 2), (100, 4), (1000, 8), (10000, 16)]
)
def test_generation_threaded(tmp_dir, num_files, num_workers):
    _generate_files(tmp_dir, num_files)

    rename.rename_all(tmp_dir, num_workers)

    files = os.listdir(tmp_dir)
    assert len(files) == num_files

    for f in files:
        assert path.isfile(path.join(tmp_dir, f))

        basename = path.splitext(f)[0]
        assert uuid.UUID(basename)


@pytest.mark.slow
@pytest.mark.parametrize("num_files, num_dirs", [(100, 1)])
def test_generation_dirs_ignored(tmp_dir, num_files, num_dirs):
    _generate_files(tmp_dir, num_files)
    gen_tmp_dir = _generate_tmpdir(tmp_dir)

    rename.rename_selection(tmp_dir, os.listdir(tmp_dir))

    files = []
    dirs = []
    for x in os.listdir(tmp_dir):
        if path.isfile(path.join(tmp_dir, x)):
            files.append(x)
        else:
            dirs.append(x)

    assert len(files) == num_files
    for f in files:
        basename = path.splitext(f)[0]
        assert uuid.UUID(basename)

    assert len(dirs) == num_dirs
    for d in dirs:
        assert gen_tmp_dir == path.join(tmp_dir, d)


@pytest.mark.parametrize("old_name", ["hello"])
def test_no_extension(old_name):
    f = rename.get_new_name(old_name)
    assert uuid.UUID(f)


@pytest.mark.parametrize("old_name", ["hello.f", "hello.txt", "hello.txt.txt"])
def test_with_extension(old_name):
    f = rename.get_new_name(old_name)

    original_ext = path.splitext(old_name)[1]
    new_ext = path.splitext(f)[1]

    assert original_ext == new_ext
    assert uuid.UUID(path.splitext(f)[0])
