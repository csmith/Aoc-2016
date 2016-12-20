#!/usr/bin/python3

"""Solution for day 20 of Advent of Code 2016.

This solution first compresses the blacklist by merging overlapping sections, using functools.reduce and the merge
function below. For example, [(0, 100), (50, 150)] becomes (0, 150). The blacklist is then inverted to become a
whitelist, which gives both answers pretty easily.
"""

import functools

def merge(x, y):
    if y[0] <= x[-1][1] + 1:
        # This entry overlaps with the last one, combine them
        x[-1] = (x[-1][0], max(y[1], x[-1][1]))
    else:
        # New, non-overlapping entry, just append it to our list
        x.append(y)
    return x

with open('data/20.txt', 'r') as file:
    ranges = sorted(list(map(lambda x: tuple(map(int, x.strip().split('-'))), file.readlines())))
    blacklist = functools.reduce(merge, ranges[1:], [ranges[0]])

    whitelist = []
    last = 0
    for pair in blacklist:
        if pair[0] > last:
            whitelist.append((last, pair[0] - 1))
        last = pair[1] + 1
    if last < 4294967295:
        whitelist.append((last, 4294967295))

    print("Part 1: %s" % whitelist[0][0])
    print("Part 2: %s" % sum(map(lambda p: 1 + p[1] - p[0], whitelist)))
