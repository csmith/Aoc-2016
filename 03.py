#!/usr/bin/python3

from itertools import chain

with open('03.txt', 'r') as file:
    tris = [[int(s) for s in l.strip().split()] for l in file.readlines()]
    possible = lambda tris: len([1 for t in [sorted(t) for t in tris] if t[0] + t[1] > t[2]])
    print("Part one: %s" % possible(tris))
    print("Part two: %s" % possible(chain(*[zip(*tris[i:i + 3]) for i in range(0, len(tris), 3)])))
