import pytest
import tempfile


@pytest.fixture
def tmp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir
        print("done")
