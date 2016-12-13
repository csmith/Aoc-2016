#!/usr/bin/python3

import itertools

input = 1364

high = lambda x: sum([1 for d in bin(x) if d == '1'])
wall = lambda x, y: high(x*x + 3*x + 2*x*y + y + y*y + input) % 2 == 1
all_moves = lambda x, y: [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
moves = lambda x, y: (m for m in all_moves(x, y) if m[0] >= 0 and m[1] >= 0 and not wall(*m))
queue = set([(1, 1)])
visited = set()
distance = {}
steps = 0

while steps < 100:
	for c in queue:
		if c not in distance:
			distance[c] = steps

	visited = visited.union(queue)
	next_queue = set(itertools.chain.from_iterable(moves(*c) for c in queue)) - visited
	queue = next_queue
	steps += 1

print("Part 1: %s" % distance[(31, 39)])
print("Part 2: %s" % sum(1 for s in distance.values() if s <= 50))
