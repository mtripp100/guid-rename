def as_blocks(work, num_workers):
    if num_workers < 1:
        raise ValueError("num_workers must be > 0")

    min_size = len(work) // num_workers
    extra = len(work) % num_workers

    start = 0
    for _ in range(num_workers):
        end = min_size + (1 if extra > 0 else 0)
        yield work[start : start + end]
        start += end

        if extra > 0:
            extra -= 1
