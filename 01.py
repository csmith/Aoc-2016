#!/usr/bin/python3

import math
import operator


def steps(start, delta, count):
    sign = int(math.copysign(1, delta))
    return [start] * count if delta == 0 else range(start + sign, start + delta + sign, sign)

with open('data/01.txt', 'r') as file:
    input = file.read()

movement_lookup = {'L': -1, 'R': +1}
direction_lookup = {0: (0, -1), 1:  (1,  0), 2: (0,  1), 3:  (-1, 0)}

moves = [(movement_lookup[move[0]], int(move[1:])) for move in input.split(', ')]

heading = 0
history = [(0, 0)]
for move in moves:
    heading = (heading + move[0]) % 4
    delta = list(map(operator.mul, direction_lookup[heading], (move[1], move[1])))
    delta_mag = max(abs(delta[0]), abs(delta[1]))
    history += zip(steps(history[-1][0], delta[0], delta_mag),
                   steps(history[-1][1], delta[1], delta_mag))

duplicates = (x for n, x in enumerate(history) if history[:n].count(x) > 0)
overlap = next(duplicates)

print("Part 1: %s ==> %s" % (history[-1], abs(history[-1][0]) + abs(history[-1][1])))
print("Part 2: %s ==> %s" % (overlap, abs(overlap[0]) + abs(overlap[1])))
