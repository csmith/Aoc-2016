#!/usr/bin/python3

"""Solution for day 14 of Advent of Code 2016.

The actual logic for this solution is contained in the matches lambda, which returns an infinite-length generator
containing all of the matching hashes. The implementation is very basic, calling the hash functions and triple-digit
matcher multiple times for the same inputs. This avoids having to manually keep a second list of hashes to check for
five letter matches.

To avoid the massive slowness that would happen if we recomputed up to 1,000 hashes each step, the hash methods (and
triple-finding method) themselves are cached using functools.lru_cache. The caches can hold 1024 entries, so
comfortably hold the results of the 1,000 hash look-forward.
"""


import functools
import hashlib
import itertools
import re

salt = 'cuanljph'


@functools.lru_cache(maxsize=1024)
def md5(index):
    return hashlib.md5((salt + str(index)).encode('UTF-8')).hexdigest()


@functools.lru_cache(maxsize=1024)
def stretched(index):
    key = salt + str(index)
    for _ in range(2017): key = hashlib.md5(key.encode('UTF-8')).hexdigest()
    return key


@functools.lru_cache(maxsize=1024)
def trip(index, fn):
    return tripmatcher.search(fn(index))

tripmatcher = re.compile(r'(.)\1{2}')
matches = lambda fn: ((i, fn(i)) for i in itertools.count()
                      if trip(i, fn) and any(trip(i, fn).group(1) * 5 in fn(n)
                                             for n in range(i + 1, i + 1000)))
 
print("Part one: %s" % next(itertools.islice(matches(md5), 63, 64))[0])
print("Part two: %s" % next(itertools.islice(matches(stretched), 63, 64))[0])
