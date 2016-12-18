#!/usr/bin/python3

"""Solution for day 17 of Advent of Code 2016.

Implements an A* search algorithm for finding the shortest path (which wasn't really necessary given part two!)
The heapq module is used to keep the queue sorted in priority order, with the priorities calculated as the
current distance travelled plus the Manhattan distance to the end (so the first path found will be the shortest).
"""

import functools
import hashlib
import heapq
import itertools

salt = 'njfxhljp'
moves = {'U': (0, -1), 'D': (0, +1), 'L': (-1, 0), 'R': (+1, 0)}


def open_doors(path):
    """Gives a list of open doors around the current square, given the path used to reach it.

    Does not take into account whether doors actually exist or not.

    :param path: The path taken to reach the square (as a string, one char per move; e.g. 'UDUDRLRLLL')
    :return: Iterator of directions which have open doors
    """
    return itertools.compress('UDLR', [x > 'a' for x in hashlib.md5((salt + path).encode('UTF-8')).hexdigest()[:4]])


def next_moves(coords, path):
    """Gets a list of all possible moves from the given position tuple.

     Takes in to account the maze bounds and door states.

     A move's "priority" is the length of the path taken so far, plus the Manhattan distance to the end goal.
     This allows us to use a best-first searching algorithm like A* to efficiently find paths to the end.

    :param coords: The current co-ordinates, as a tuple of (x, y).
    :param path: The path taken to reach the square (as a string, one char per move; e.g. 'UDUDRLRLLL')
    :return: An (unsorted) iterator of new potential positions, as tuples of (priority, co-ordinates, path)
    """
    for direction in open_doors(path):
        new_coords = tuple(map(sum, zip(coords, moves[direction])))
        if 0 <= new_coords[0] <= 3 and 0 <= new_coords[1] <= 3:
            yield ((len(path) + 7 - coords[0] - coords[1], new_coords, path + direction))


def find_paths():
    """Finds all paths from the starting point of (0, 0) to the end point of (3, 3).

    Paths are searched in priority order, meaning the shortest path is returned first and the longest path returned
    last.

    :return: A generator which emits paths (as strings of directions, e.g. 'UDDDRRR...') from shortest to longest
    """
    queue = []
    heapq.heappush(queue, (6, (0, 0), ''))
    while len(queue):
        _, coords, path = heapq.heappop(queue)
        if coords == (3, 3):
            yield path
        else:
            for move in next_moves(coords, path):
                heapq.heappush(queue, move)


paths = find_paths()
print('Step 1: %s' % next(paths))
print('Step 2: %s' % len(functools.reduce(lambda x, y: y, paths)))
