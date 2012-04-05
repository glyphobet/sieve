#!/usr/bin/env python
import sys

def sieve(primes=[(2, 4)]):
    """A generator that yields primes forever. Also caches primes for use in subsequent calls."""
    for p in primes:
        yield p

    n, _ = primes[-1]
    while True:
        n += 1
        if n == next(factor(n, primes)): # if n is its own (first) factor, it's prime
            primes.append((n, n**2))
            yield primes[-1]


def factor(n, primes=None):
    """Factor an integer into its unique prime decomposition."""
    if n <= 1: # handle 0 and 1
        yield n
        return
    primes = primes or sieve()
    for p, p2 in primes:
        if n < p2:
            break # if n is < p*p, we have yielded all factors by now
        while n % p == 0:
            yield p
            n = n // p
    if n > 1:
        yield n


for arg in sys.argv[1:]:
    print(arg + ': ' + ' '.join(map(str, factor(abs(int(arg))))))
