#!/usr/bin/python3

"""Solution for day 23 of Advent of Code 2016.

This is loosely based on day 12's solution. As instructions can now be modified (by the TGL opcode), they're kept
in a 'register' as well.

For part two to work in a reasonable amount of time, try_multiply implements a look-ahead optimisation for
basic multiplication. Instructions of the form

         cpy b c
         inc a
         dec c
         jnz c -2
         dec d
         jnz d -5

Are actually incrementing a by b*d, and setting both c and d to 0. The optimisation supports any registers, as long
as they're distinct. It also only applies if the whole block of six instructions is reached naturally (i.e., execution
doesn't jump into the middle of it).
"""


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
    registers['in'] = instr.copy()

    while registers['pc'] < len(instr):
        step(registers)
        registers['pc'] += 1

    return registers['a']


with open('data/23.txt', 'r') as file:
    instr = map(str.split, map(str.strip, file.readlines()))
    instr = [(globals()[i[0]], i[1:]) for i in instr]

print("Stage 1: %s" % run({'a': 7, 'b': 0, 'c': 0, 'd': 0}))
print("Stage 2: %s" % run({'a': 12, 'b': 0, 'c': 0, 'd': 0}))
