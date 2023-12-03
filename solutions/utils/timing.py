import time
from datetime import timedelta


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        seconds_taken = time.time() - start_time

        delta = timedelta(seconds=seconds_taken).total_seconds() * 1000

        return result, delta

    return wrapper
