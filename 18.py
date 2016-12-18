#!/usr/bin/python3

"""Solution for day 18 of Advent of Code 2016.

Each line of the maze is represented as a list of booleans, with True for safe spaces and False for traps.

The four separate trap rules can be simplified to just "left is different to right", which is handled in the line
lambda (with some annoying fudging to handle the first and last elements whose parents are 'walls').

The solution is obtained by repeatedly generating lines and summing them (Python booleans are a subclass of ints,
with True being equal to 1 and False to 0, so a simple call to sum counts the number of safe squares). Only the most
recent line is kept, everything else is discarded once counted. This is implemented using a call to functools.reduce,
passing along a tuple of (line, sum). In each round, the line is mutated to its new form, and the sum of safe spaces
is added to the running total.
"""

import functools

seed = [x == '.' for x in
        '^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^']

line = lambda p: [(i == 0 or p[i - 1]) == (i == len(p) - 1 or p[i + 1]) for i in range(len(p))]
calc = lambda n: functools.reduce(lambda x, y: (line(x[0]), x[1] + sum(line(x[0]))), range(n - 1), (seed, sum(seed)))[1]

print('Part one: %s' % calc(40))
print('Part two: %s' % calc(400000))