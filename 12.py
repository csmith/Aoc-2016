#!/usr/bin/python3

"""Solution for day 12 of Advent of Code 2016.

Models a simple virtual machine. Each of the four operations is defined as a method, and called using reflection.
The current line number is kept in a special 'pc' (for 'program counter') register, which means that each operation is
a simple mutation of a register.

All values are handled by first trying to parse the input as an integer; if that fails then it is treated as a register
name and the value of the register is returned. This allows any argument to be numerical or a register, not just those
shown int he question example.
"""


with open('data/12.txt', 'r') as file:
    instr = list(map(str.split, map(str.strip, file.readlines())))

def run(values):
    registers = values
    registers['pc'] = 0

    def value(x):
        try:
            return int(x)
        except ValueError:
            return registers[x]

    def cpy(args): registers[args[1]] = value(args[0])
    def inc(args): registers[args[0]] += 1
    def dec(args): registers[args[0]] -= 1
    def jnz(args): registers['pc'] += 0 if value(args[0]) == 0 else value(args[1]) - 1

    while registers['pc'] < len(instr):
        locals()[instr[registers['pc']][0]](instr[registers['pc']][1:])
        registers['pc'] += 1

    return registers['a']

print("Stage 1: %s" % run({'a': 0, 'b': 0, 'c': 0, 'd': 0}))
print("Stage 2: %s" % run({'a': 0, 'b': 0, 'c': 1, 'd': 0}))
