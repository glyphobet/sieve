"""
>>> from sieve import factor

>>> list(factor(0))
[0]

>>> list(factor(1))
[1]

>>> list(factor(2))
[2]

>>> list(factor(6))
[2, 3]

>>> list(factor(1024))
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

>>> [long(f) for f in factor(31313718421)]
[31313718421L]

>>> [long(f) for f in factor(31313718421229)]
[38069L, 822551641L]

>>> list(factor(81))
[3, 3, 3, 3]
"""

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    exit(results.failed)
