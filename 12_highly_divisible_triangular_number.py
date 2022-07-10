from primefac import primefac
from collections import Counter
from math import prod


def triangle_number(n):
    return int(n * (n + 1) / 2)


def n_divisors(n):
    factors = Counter(primefac(n))
    # All different multiples from the prime factors
    return prod(n_count + 1 for n_count in factors.values())


def min_triangle_number_with_n_divisors(divisors=500, limit=int(1e6)):
    for i in range(limit):
        t = triangle_number(i)
        if n_divisors(t) >= divisors:
            return t


print(min_triangle_number_with_n_divisors())
