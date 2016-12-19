#!/usr/bin/python3

"""Solution for day 19 of Advent of Code 2016.

There are two different solutions presented here. The "manually" methods simulate the present-thieving step by step
to get the results. I used these to figure out the patterns to both part 1 and part 2 and thus write simple, super
quick formulae to get the answer.

For part 1, the results look something like this:

  Number of Elves |  Winning Elf
  1               |  0
  2               |  0
  3               |  2
  4               |  0
  5               |  2
  6               |  4
  7               |  6
  8               |  0

So if the number of elves is a power of two, then the first elf wins. Otherwise, the winning elf is the one with a
number double the difference between the last power of two and the number of elves.

For part 2, the results are more complicated (as you'd expect!):

  Number of Elves |  Winning Elf
  1               |  0
  2               |  0
  3               |  2
  4               |  0
  5               |  1
  6               |  2
  7               |  4
  8               |  6
  9               |  8
  10              |  0
  11              |  1
  12              |  2
  13              |  3
  ...             |  ...
  18              |  8
  19              |  10
  20              |  12
  ...             |  ...
  28              |  0

The points where elf 0 wins (and the sequence resets) now follow the pattern 3^n+1 (instead of 2^n from part 1).
Between those points, the winning elf increases by 1 for the first 3^n elves, then by 2 thereafter.
"""

import math

seed = 3004953

print('Part one: %s' % (1 + 2 * int(seed - 2 ** math.floor(math.log(seed, 2)))))

lp = 3 ** int(math.floor(0.0001 + math.log(seed - 1, 3)))  # Add a small amount to avoid floating point errors
print('Part two: %s' % ((seed - lp) * (1 + max(0, (seed - 2 * lp) / (lp + 1)))))


def run_part1_manually(n):
    elves = {}
    for i in range(n):
        elves[i] = i + 1 if i < n - 1 else 0
    current = 0
    while len(elves) > 1:
        neighbour = elves[current]
        elves[current] = elves[neighbour]
        del elves[neighbour]
        current = elves[current]
    return elves.keys()[0]


def run_part2_manually(n):
    elves = range(n)
    current = 0
    while len(elves) > 1:
        target = (current + int(math.floor(len(elves) / 2))) % len(elves)
        del elves[target]
        if target > current:
            current = (current + 1) % len(elves)
        else:
            current %= len(elves)
    return elves[0]
