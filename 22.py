#!/usr/bin/python3

"""Solution for day 22 of Advent of Code 2016.

Part 1 is straight-forward reading of the data, generating pairs using itertools.permutations, and counting how
many match the criteria.

As is traditional at about this point in Advent of Code, part 2 requires you to make annoying assumptions based on
the vague example in the question and some properties of your input that you have no guarantee are universal.

In this case, the input needs to be partitioned in to three sets: empty nodes (of which there is just one), giant
nodes (whose data can't possibly be placed anywhere else) and normal nodes (who can shift their data to the empty
node, but not to any other normal node).

When the nodes are printed out according to their type (as in the example), it becomes obvious that there's a "wall"
of giant nodes in the way. As the only valid moves involve the empty node, you basically have to move that around and
use it to move the data along the top row.

For my input, it takes 34 moves to rearrange things and then move the target data left by one:

..............23456789012345678901234
..............1......................
..............0######################
..............9876543................
....................2................
....................1................
...................._................
.....................................
.....................................

Then for each node to the left it takes an additional five moves, as the empty space loops around our target:

....45_..
....321..
.........

It needs to move a total of 35 nodes left, so 34+35*5 total moves = 209.
"""

import re

import itertools

matcher = re.compile(r'^/dev/grid/node-x([0-9]+)-y([0-9]+)\s+([0-9]+)T\s+([0-9]+)T\s+([0-9]+)T\s+.*$')

# Constants used for convenient access the groups in the matcher above
locx = 0
locy = 1
size = 2
used = 3
free = 4

with open('data/22.txt', 'r') as data:
    discs = [tuple(map(int, matcher.match(l).groups())) for l in data.readlines() if matcher.match(l)]
    pairs = sum(1 for p in itertools.permutations(discs, 2) if 0 < p[0][used] <= p[1][free])
    print('Part one: %s' % pairs)

    print('Part two: ...')
    grid = dict((disc[:locy+1], disc) for disc in discs)
    for y in range(27):
        print(''.join(['X' if (x,y) not in grid
                       else '_' if grid[(x, y)][used] == 0
                       else '#' if grid[(x, y)][used] > 150  # Arbitrary cut-off for "normal" vs "giant" nodes
                       else '.' for x in range(37)]))
