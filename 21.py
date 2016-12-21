#!/usr/bin/python3

"""Solution for day 21 of Advent of Code 2016.

Each operation has an entry in the ops dictionary, which mangles arguments and does pre-processing before handing off
to one of the main methods to perform the actual transformation.

For part two, the reverse_ops dictionary maps most operations to a reverse of their original. The only exception is
'rotate based on position', which is just brute-forced by rotating the letters and seeing if the forward instruction
puts them back to the expected positions.
"""


from functools import reduce

ops = {
    'swap position':     lambda l, a: swap_positions(l, int(a[0]), int(a[3])),
    'swap letter':       lambda l, a: swap_letter(l, a[0], a[3]),
    'rotate left':       lambda l, a: rotate(l, -int(a[0])),
    'rotate right':      lambda l, a: rotate(l, int(a[0])),
    'rotate based':      lambda l, a: rotate(l, 1 + l.index(a[4]) + (1 if l.index(a[4]) > 3 else 0)),
    'reverse positions': lambda l, a: reverse(l, int(a[0]), int(a[2])),
    'move position':     lambda l, a: move(l, int(a[0]), int(a[3])),
}

reverse_ops = {
    'swap position':     lambda l, a: swap_positions(l, int(a[3]), int(a[0])),
    'swap letter':       ops['swap letter'],
    'rotate left':       ops['rotate right'],
    'rotate right':      ops['rotate left'],
    'rotate based':      lambda l, a: reverse_rotation(l, a),
    'reverse positions': ops['reverse positions'],
    'move position':     lambda l, a: move(l, int(a[3]), int(a[0])),
}


def swap_positions(letters, x, y):
    letters[x], letters[y] = letters[y], letters[x]
    return letters


def swap_letter(letters, a, b):
    return [a if l == b else b if l == a else l for l in letters]


def rotate(letters, num):
    num %= len(letters)
    return letters[-num:] + letters[:-num]


def reverse(letters, start, end):
    return letters[:start] + letters[start:end+1][::-1] + letters[end+1:]


def move(letters, start, end):
    letters.insert(end, letters.pop(start))
    return letters


def reverse_rotation(l, a):
    return [rotate(l, i) for i in range(len(l)) if ops['rotate based'](rotate(l, i), a) == l][0]


with open('data/21.txt', 'r') as file:
    instr = list(map(lambda x: [' '.join(x.split(' ')[0:2])] + x.strip().split(' ')[2:], file.readlines()))
    print('Part one: %s' % ''.join(reduce(lambda l, o: ops[o[0]](l, o[1:]), instr, list('abcdefgh'))))
    print('Part two: %s' % ''.join(reduce(lambda l, o: reverse_ops[o[0]](l, o[1:]), instr[::-1], list('fbgdceah'))))