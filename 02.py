#!/usr/bin/python3

import operator

with open('02.txt', 'r') as file:
    input = [x.strip() for x in file.readlines()]

dirs = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
parts = {1: {(0, 0): '1', (1, 0): '2', (2, 0): '3',
             (0, 1): '4', (1, 1): '5', (2, 1): '6',
             (0, 2): '7', (1, 2): '8', (2, 2): '9'},

         2: {                          (2, 0): '1',
                          (1, 1): '2', (2, 1): '3', (3, 1): '4',
             (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
                          (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
                                       (2, 4): 'D'}}

for part, keys in parts.items():
    pos = list(keys.keys())[list(keys.values()).index('5')]
    ans = ''
    for line in input:
        for move in map(dirs.get, line):
            next_pos = tuple(map(operator.add, pos, move))
            pos = next_pos if next_pos in keys else pos
        ans += keys[pos]
    print('Part %s: %s' % (part, ans))
