#!/usr/bin/python3

"""Solution for day 16 of Advent of Code 2016.

This is a straightforward, brute-searching solution. It expands the input as defined in the puzzle, and then
computes checksums until it finds an odd-length one.
"""

import itertools


def expand(state, length):
    while len(state) < length:
        state = list(itertools.chain(state, [False], (not x for x in reversed(state))))
    return state[:length]


def checksum_round(state):
    return [state[i] == state[i + 1] for i in range(0, len(state), 2)]


def checksum(state):
    state = checksum_round(state)
    while len(state) % 2 == 0:
        state = checksum_round(state)
    return state


def run(state, size):
    return ''.join(str(int(x)) for x in checksum(expand(state, size)))


iv = [bool(int(x)) for x in '01110110101001000']
print('Step 1: %s' % run(iv, 272))
print('Step 2: %s' % run(iv, 35651584))
