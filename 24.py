#!/usr/bin/python3

"""Solution for day 24 of Advent of Code 2016.

Another day, another breadth-first search! I split this problem into two stages: first, computing the distance
between every combination of points in the maze, and, second, finding the shortest route using those paths.

Finding the distances is just a simple BFS. As we only care about distance, each pair of nodes is only calculated
once (i.e., it stores a distance for, e.g., (0 -> 2) but not (2 -> 0)). Pairs are stored sorted.

To find all the possible routes, we just need a call to itertools.permutations for the middle section (ignoring '0').
The '0' stop(s) are then added around the permutation, and the total distance calculated by chunking them into pairs
and looking them up in the distances table. This is done in the route_length method.

For example, with the example maze with 5 points we compute and store 10 distances:
  0 -> 1, 0 -> 2, 0 -> 3, 0 -> 4, 1 -> 2, 1 -> 3, 1 -> 4, 2 -> 3, 2-> 4, 3-> 4

Which become tuple keys in our distances dictionary:
  (0, 1): a, (0, 2): b, ... (3, 4): z

Then to find the route we start with all 24 possible routes:
  01234, 01243, 01324, 01342, 01423, 01432, 02134, etc...

Each route is chunked into pairs:
  01234 ==> (0, 1), (1, 2), (2, 3), (3, 4)

And the pairs are then looked up in the dictionary and summed.

The problem could in theory be solved using one large BFS but it would be fairly complicated as you'd need to prevent
backtracking generally, while still allowing it after reaching a new numbered location. You'd also end up recalculating
the distances between many places unless you did some clever optimisations. Pre-computing the distances also makes part
2 very easy.
"""

import functools
import itertools
import operator


def find(maze, num):
    for y, line in enumerate(maze):
        if num in line:
            return line.index(num), y


def navigable(maze, location):
    return maze[location[1]][location[0]] != '#'


def directions(location):
    yield (location[0], location[1] + 1)
    yield (location[0], location[1] - 1)
    yield (location[0] + 1, location[1])
    yield (location[0] - 1, location[1])


def moves(maze, start):
    return set(filter(lambda loc: navigable(maze, loc), directions(start)))


def distance(maze, start_num, end_num):
    start = find(maze, start_num)
    end = find(maze, end_num)
    visited = set()
    queue = [start]
    steps = 0
    while len(queue):
        new_queue = functools.reduce(operator.or_, [moves(maze, target) for target in queue])
        queue = new_queue - visited
        visited |= queue
        steps += 1
        if end in queue:
            return steps


def route_length(distances, route):
    return sum(map(lambda p: distances[tuple(sorted(p))], (route[i:i +2] for i in range(0, len(route)-1))))


with open('data/24.txt', 'r') as file:
    my_maze = list(map(str.strip, file.readlines()))
    points = sorted(list(x for x in itertools.chain(*my_maze) if x.isdigit()))
    distances = dict(((pair, distance(my_maze, *pair)) for pair in itertools.combinations(points, 2)))
    routes = set(itertools.permutations(points[1:]))

    print('Part one: %s' % min(route_length(distances, ['0'] + [*route]) for route in routes))
    print('Part two: %s' % min(route_length(distances, ['0'] + [*route] + ['0']) for route in routes))
