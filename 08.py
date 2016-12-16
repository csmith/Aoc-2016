#!/usr/bin/python3

import re
import numpy as np

with open('08.txt', 'r') as file:
    lines = list(map(str.strip, file.readlines()))
    lights = np.zeros((6, 50), dtype=bool)
    for line in lines:
        words = line.split(' ')
        i, j = map(int, re.search(r'([0-9]+)(?: by |x)([0-9]+)', line).groups())
        if words[0] == 'rect':
            lights[:j, :i] = 1
        elif words[1] == 'row':
            lights[i] = np.roll(lights[i], j)
        else:
            lights[:, i] = np.roll(lights[:, i], j)

    print("Part one: %s" % np.sum(lights))
    print("Part two:")
    print('\n'.join(''.join('\u2588' if p else ' ' for p in row) for row in lights))
