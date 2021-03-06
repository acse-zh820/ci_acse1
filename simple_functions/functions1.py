from functools import lru_cache
__all__ = ['my_sum', 'factorial', 'average']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)
def factorial(n):
    return n*factorial(n-1) if n else 1


def average(number):
    return my_sum(number)/len(number)
