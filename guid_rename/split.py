from os import listdir, rename
from os.path import isfile, join
import uuid


def next_block(blocks, workers):
    min_size = len(blocks) // workers
    extra = len(blocks) % workers

    start = 0
    for i in range(workers):
        end = min_size + (1 if extra > 0 else 0)
        yield blocks[start:start + end]
        start += end

        if extra > 0:
            extra -= 1

blocks = [x for x in range(1)]
workers = 12

for block in next_block(blocks, workers):
    print(len(block))
