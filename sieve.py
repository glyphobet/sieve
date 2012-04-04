#!/usr/bin/env python
import sys

def generate_primes():
    """A generator that yields primes forever."""
    n = 1
    primes = []

    while True:
        n += 1
        n_factor = factor(n, primes)
        n_factor.next()
        try:
            n_factor.next() # n has two factors, it's not prime
            continue
        except StopIteration: # n has one factor, it's prime
            primes.append((n, n**2))
            yield primes[-1]


def factor(n, primes=None):
    """Factor an integer into its unique prime decomposition."""
    if n <= 1: # handle 0 and 1
        yield n
        return
    if primes is None:
        primes = generate_primes()
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
