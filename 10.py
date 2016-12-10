#!/usr/bin/python3

import collections

with open('10.txt', 'r') as file:
    targets = collections.defaultdict(lambda: {'inputs': [], 'low': -1, 'high': -1})
    lines = list(map(str.split, map(str.strip, file.readlines())))
    for instr in lines:
        if instr[0] == 'value':
            targets[' '.join(instr[4:6])]['inputs'].append(int(instr[1]))
        else:
            targets[' '.join(instr[0:2])]['low'] = ' '.join(instr[5:7])
            targets[' '.join(instr[0:2])]['high'] = ' '.join(instr[10:12])

pending = set(targets.keys())
while len(pending):
    for k, bot in [(k, targets[k]) for k in pending if len(targets[k]['inputs']) == 2]:
        targets[bot['low']]['inputs'].append(min(bot['inputs']))
        targets[bot['high']]['inputs'].append(max(bot['inputs']))
        pending.remove(k)

print("Part 1: %s" % [k for k,v in targets.items() if 61 in v['inputs'] and 17 in v['inputs']][0])
print("Part 2: %i" % (targets['output 0']['inputs'][0] * targets['output 1']['inputs'][0] * targets['output 2']['inputs'][0]))
