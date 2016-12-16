#!/usr/bin/python3

import hashlib
import itertools
from multiprocessing import Pool

door = 'abbhdwsy'


def hash(x):
    return hashlib.md5((door + str(x)).encode('utf-8')).hexdigest()


pool = Pool()
hashes = pool.imap(hash, itertools.count(), 10000)
zeroes = (h for h in hashes if h.startswith('00000'))
part1 = ''
part2 = ['_'] * 8

for h in zeroes:
    if len(part1) < 8:
        part1 += h[5]
    if h[5].isdigit() and int(h[5]) < len(part2) and part2[int(h[5])] == '_':
        part2[int(h[5])] = h[6]

    if '_' not in part2:
        print("Part one: %s" % part1)
        print("Part two: %s" % ''.join(part2))
        break
