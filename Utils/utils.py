import time
from contextlib import contextmanager
from functools import wraps

# @contextmanager
# def localtimer():
#     start = time.perf_counter()
#     yield
#     print('func took', time.perf_counter() - start)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f'{func.__name__!r} took {time.perf_counter() - start} seconds')

    return wrapper

def __main():
    pass


if __name__ == '__main__':
    __main()
