#!/usr/bin/python3

"""Solution for day 25 of Advent of Code 2016.

This is a copy of Day 23's solution, with an 'out' instruction added.

Manual testing showed the output repeats regularly, so we just run the program until there are 20 bits output.
"""
import itertools


def value(registers, x):
    try:
        return int(x)
    except ValueError:
        return registers[x]


def cpy(registers, src, dst):
    registers[dst] = value(registers, src)


def inc(registers, reg):
    registers[reg] += 1


def dec(registers, reg):
    registers[reg] -= 1


def jnz(registers, val, tar):
    registers['pc'] += 0 if value(registers, val) == 0 else value(registers, tar) - 1


def tgl(registers, ins):
    mappings = {inc: dec, dec: inc, tgl: inc, jnz: cpy, cpy: jnz}
    target = registers['pc'] + value(registers, ins)
    registers['in'][target] = (mappings[registers['in'][target][0]], registers['in'][target][1])


def out(registers, val):
    registers['out'].append(value(registers, val))


def try_multiply(registers):
    try:
        pc = registers['pc']
        chunk = registers['in'][pc:pc+6]
        instr, args = map(list, zip(*chunk))
        if instr == [cpy, inc, dec, jnz, dec, jnz] \
                and args[0][1] == args[2][0] == args[3][0] \
                and args[4][0] == args[5][0] \
                and args[1][0] != args[0][1] != args[4][0] != args[0][0] \
                and args[3][1] == '-2' and args[5][1] == '-5':
            registers[args[1][0]] += value(registers, args[0][0]) * value(registers, args[4][0])
            registers[args[2][0]] = 0
            registers[args[4][0]] = 0
            registers['pc'] += 5
            return True
    except:
        pass
    return False


def step(registers):
    if not try_multiply(registers):
        try:
            registers['in'][registers['pc']][0](registers, *registers['in'][registers['pc']][1])
        except:
            pass


def run(values):
    registers = values
    registers['pc'] = 0
    registers['out'] = []
    registers['in'] = instr.copy()

    while registers['pc'] < len(instr) and len(registers['out']) < 20:
        step(registers)
        registers['pc'] += 1

    return registers['out']


with open('data/25.txt', 'r') as file:
    instr = map(str.split, map(str.strip, file.readlines()))
    instr = [(globals()[i[0]], i[1:]) for i in instr]

for a in itertools.count():
    if run({'a': a, 'b': 0, 'c': 0, 'd': 0}) == [0, 1] * 10:
        print('Part one: %s' % a)
        break
