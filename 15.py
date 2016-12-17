#!/usr/bin/python3

import itertools
import re

input_matcher = re.compile(r'^Disc #(.*?) has (.*?) positions; at time=0, it is at position (.*?)\.$')

# Returns a generator for positions that this disc will be at when the capsule arrives. e.g. if disc 3 starts at
# position 0 at time 0, the first returned position will be 3 (because the disc will have ticked around three times
# before a capsule released at t=0 arrives).
positions = lambda disc: ((disc[0] + disc[2] + i) % disc[1] for i in itertools.count())


def run(lines):
    # Pull the information out from the text line, making sure we treat numbers as ints.
    discs = map(lambda line: tuple(map(int, input_matcher.match(line).groups())), map(str.strip, lines))

    # Zip together the positions of each disc. That means the first element in combos will show the positions each
    # disc will be at when the capsule arrives if it's released at t=0; the second element will be the positions for
    # a capsule released at t=1, etc.
    combos = zip(*map(positions, discs))

    # Find a time when all discs will be at position 0 for the arrival of the capsule.
    times = (i for i, c in enumerate(combos) if all(p == 0 for p in c))
    return next(times)

with open('data/15.txt', 'r') as file:
    lines = file.readlines()
    print("Step 1: %s" % run(lines))
    print("Step 2: %s" % run(lines + ['Disc #7 has 11 positions; at time=0, it is at position 0.']))
