import time

def with_timeout(fn, seconds):
    start = time.time()
    result = fn()
    if time.time() - start > seconds:
        raise TimeoutError("took too long")
    return result
