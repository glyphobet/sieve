#!/usr/bin/env python
import sys

def primes():
    n = 1
    primes = []

    def relatively_prime(n):
        for p, p2 in primes:
            if n < p2:
                return True # is prime because if it were not, we would have hit a factor by now
            elif n % p == 0:
                return False # is not prime because modulo p == 0
        return True # primes is empty so this is the first prime, 2

    while True:
        n += 1
        if relatively_prime(n):
            yield n
            primes.append((n, n**2))

def factor(n):
    for p in primes():
        if p > n: 
            break
        while n % p == 0:
            yield p
            n = n / p
    if n > 1:
        yield n


for arg in sys.argv[1:]:
    print arg + ': ' + ' '.join(map(str, factor(int(arg))))