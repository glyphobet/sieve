#!/usr/bin/env python

# def sieve(prime, seq):
#     prime2 = prime ** 2
#     for n in seq:
#         if n < prime2:
#             yield n
#         elif n % prime:
#             yield n
# 
# def chunk(gen):
#     i = iter(gen)
#     prime = i.next()
#     yield prime
#     for n in chunk(sieve(prime, i)):
#         yield n
# 
# for n in chunk(xrange(2, 3500)):
#     print n,



# def assbackwards_sieve(gen):
#     i = iter(gen)
#     prime = i.next()
#     yield prime
#     for n in assbackwards_sieve(i):
#         if n % prime:
#             yield n
#         else:
#             print "{0} is divisible by {1}".format(n, prime)
#             
# 
# for n in assbackwards_sieve(xrange(2, 750)):
#     print "{0} is prime".format(n)

def factor(n, primes):
    for p in primes:
        if p > n: 
            break
        while n % p == 0:
            yield p
            n = n / p

limit = 10**4

def recursive_sieve(i):
    prime = i.next()
    yield prime
    for n in recursive_sieve(n for n in i if n < prime ** 2 or n % prime):
        yield n

# print ' '.join(map(str, recursive_sieve(iter(xrange(2, limit)))))


def iterative_sieve():
    n = 1
    primes = []
    while n < limit:
        n += 1
        print n, primes
        for p, p2 in primes:
            if n < p2:
                print "\tcontinue because %s < %s" % (n, p2)
                continue
            if n % p == 0:
                print "\tbreak because %s %% %s == 0" % (n, p)
                break
        else:
            yield n
            primes.append((n, n**2))

print ' '.join(map(str, iterative_sieve()))
# assert list(iterative_sieve()) == list(recursive_sieve(iter(xrange(2, limit))))