import pytest

from guid_rename import blocks


@pytest.mark.parametrize(
    "work, num_workers, result",
    [
        ([1, 2, 3], 1, [[1, 2, 3]]),
        ([1, 2, 3], 2, [[1, 2], [3]]),
        ([1, 2, 3], 3, [[1], [2], [3]]),
        ([1, 2, 3], 4, [[1], [2], [3], []]),
        ([], 1, [[]]),
        ([], 2, [[], []]),
    ],
)
def test_selection(work, num_workers, result):
    chunks = blocks.as_blocks(work, num_workers)

    assert list(chunks) == result


@pytest.mark.parametrize("num_workers", [0, -1])
def test_invalid_workers(num_workers):
    with pytest.raises(ValueError):
        next(blocks.as_blocks([], num_workers))
