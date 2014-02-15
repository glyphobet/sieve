#!/usr/bin/env python3.3
import sys

def sieve(primes=[(2, 4)]):
    """A generator that yields primes forever. Also caches primes for use in subsequent calls."""
    yield from primes

    n, _ = primes[-1]
    while True:
        n += 1
        if n == next(_factor(n, primes)): # if n is its own (first) factor, it's prime
            primes.append((n, n**2))
            yield primes[-1]


def _factor(n, primes=None):
    """Factor an integer into its unique prime decomposition."""
    for p, p2 in primes or sieve():
        if n < p2:
            break # if n is < p*p, we have yielded all factors by now
        while n % p == 0:
            yield p
            n //= p
    if n > 1:
        yield n


def factor(n):
    """Wrapper that handles 0 and 1."""
    if n <= 1:
        yield n
    else:
        yield from _factor(n)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print(arg + ': ' + ' '.join(map(str, factor(abs(int(arg))))))
