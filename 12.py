#!/usr/bin/python3

with open('12.txt', 'r') as file:
    instr = list(map(str.split, map(str.strip, file.readlines())))

def value(x):
    try:
        return int(x)
    except ValueError:
        return registers[x]

def cpy(args): registers[args[1]] = value(args[0])
def inc(args): registers[args[0]] += 1
def dec(args): registers[args[0]] -= 1
def jnz(args): registers['pc'] += 0 if value(args[0]) == 0 else value(args[1]) - 1

def run():
    while registers['pc'] < len(instr):
        globals()[instr[registers['pc']][0]](instr[registers['pc']][1:])
        registers['pc'] += 1

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'pc': 0}
run()

print("Stage 1: %s" % registers['a'])

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'pc': 0}
run()

print("Stage 2: %s" % registers['a'])
