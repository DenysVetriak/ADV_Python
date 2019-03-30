from functools import wraps


def is_positive(fn):
    def inner(n):
        if n > 0:
            result = fn(n)
        else:
            raise ValueError('Argument should be positive')
    return inner


def bounds(low, high):
    def wrapper(fn):
        @wraps
        def inner(n):
            if low < n < high:
                return fn(n)
            else:
                raise ValueError('Argument should be within bounds')
        return inner
    return wrapper


@bounds(0, 100)
def fac(n):
    return 42



def fac_rec(n):
    if n == 1:
        return n
    else:
        return n * fac_rec(n - 1)
