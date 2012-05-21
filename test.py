#!/usr/bin/env python33
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

>>> list(factor(31313718421))
[31313718421]

>>> list(factor(31313718421229))
[38069, 822551641]

>>> list(factor(81))
[3, 3, 3, 3]
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
