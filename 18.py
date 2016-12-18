#!/usr/bin/python3

"""Solution for day 18 of Advent of Code 2016.

Each line of the maze is represented as a list of booleans, with True for safe spaces and False for traps.

The four separate trap rules can be simplified to just "left is different to right", which is handled in the line
method (with some annoying fudging to handle the first and last elements whose parents are 'walls').

The solution is obtained by repeatedly generating lines and summing them (Python booleans are a subclass of ints,
with True being equal to 1 and False to 0, so a simple call to sum counts the number of safe squares). Only the most
recent line is kept, everything else is discarded once counted.
"""

seed = [x == '.' for x in
        '^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^']


def line(previous):
    return [(i == 0 or previous[i - 1]) == (i == len(previous) - 1 or previous[i + 1]) for i in range(len(previous))]


def calculate(num):
    last_line = seed
    safe_spaces = sum(last_line)
    lines = 1
    while lines < num:
        last_line = line(last_line)
        safe_spaces += sum(last_line)
        lines += 1
    return safe_spaces

print('Part one: %s' % calculate(40))
print('Part two: %s' % calculate(400000))