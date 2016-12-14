#!/usr/bin/python3

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
