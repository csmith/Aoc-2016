#!/usr/bin/python3

"""Solution for day 13 of Advent of Code 2016.

Performs a breadth-first search of the maze, for up to 100 steps. Distances of each square are kept in a dictionary,
which is also used to prevent back-tracking.
"""

import itertools

input = 1364

high = lambda x: sum([1 for d in bin(x) if d == '1'])
wall = lambda x, y: high(x*x + 3*x + 2*x*y + y + y*y + input) % 2 == 1
all_moves = lambda x, y: [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
moves = lambda x, y: (m for m in all_moves(x, y) if m[0] >= 0 and m[1] >= 0 and not wall(*m))
queue = {(1, 1)}
distance = {}

for step in range(100):
    # Merge in all the new distances from the queue, if they're not present
    distance = dict(list(distance.items()) + list(dict.fromkeys(queue, step).items()))
    # Calculate all moves from all places in the queue, and skip any places we've already visited
    queue = set(itertools.chain.from_iterable(moves(*c) for c in queue)) - set(distance.keys())

print("Part 1: %s" % distance[(31, 39)])
print("Part 2: %s" % sum(1 for s in distance.values() if s <= 50))
