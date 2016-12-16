#!/usr/bin/python3

import itertools, re

# Marker used to show the position of the lift
lift = '*YOU ARE HERE*'

# Read the input
with open('11.txt', 'r') as file:
    lines = list(map(str.strip, file.readlines()))
    floors = [re.findall(r'\b(\S+ (?:generator|microchip))\b', line) for line in lines]
    floors[0].append(lift)

# Return the elements of the chips or generators in the given lists
chips = lambda items: set([item.split('-')[0] for item in items if item.endswith('microchip')])
genrs = lambda items: set([item.split(' ')[0] for item in items if item.endswith('generator')])

# Verify that if there are generators, then all microchips present are paired
valid_floor = lambda floor: not len(genrs(floor)) or not len(chips(floor) - genrs(floor))
valid_layout = lambda layout: False not in [valid_floor(floor) for floor in layout]

# We win when everything is on the last floor (i.e., nothing is on the other floors)
target = lambda layout: sum(len(floor) for floor in layout[:-1]) == 0

# Returns the floor/floor index the lift is currently on
my_floor = lambda layout: next(floor for floor in layout if lift in floor)
my_floor_index = lambda layout: next(i for i, floor in enumerate(layout) if lift in floor)

# Returns just the items on a floor (not the lift)
items = lambda floor: set(floor) - {lift}

# Returns an enumeration of sets of items that could potentially be picked up (any combo of 1 or 2 items)
pickups = lambda items: map(set, itertools.chain(itertools.combinations(items, 2), itertools.combinations(items, 1)))

# Returns an enumeration of possible destinations for the lift (up or down one floor)
dests = lambda layout: filter(is_floor, [my_floor_index(layout) + 1, my_floor_index(layout) - 1])
is_floor = lambda i: 0 <= i < len(floors)

# Returns an enumeration of possible moves that could be made from the given state
moves = lambda layout: itertools.product(pickups(items(my_floor(layout))), dests(layout))

# Finds a floor that contains the given item
find = lambda item, layout: next(i for i, floor in enumerate(layout) if item in floor)


# Performs a breadth-first search over all moves for the given layout in order to find the number
# of steps needed to get to a winning state.
def run(floors):

    # The available types depends on the input (and thus differs between calls to the run function),
    # so we have to calculate it here, and make the serialise() and domoves() functions closures
    # over this list.
    types = [chip.split(' ')[0] for chip in itertools.chain.from_iterable(chips(items(floor)) for floor in floors)]

    # Serialises a layout into a string, for easy storage.
    # Items are replaced with numeric identifiers, determined based on position of the generator and
    # chip of that type. This means that layouts that are identical except for the elements being
    # swapped around serialise to the same string (as the process for moving them to the end will be
    # the) same.
    def serialise(layout):
        keys = sorted(types, key=lambda t: find(t + ' generator', layout) * len(layout)
                                         + find(t + '-compatible microchip', layout))
        mappings = {lift: '*'}
        for i, key in enumerate(keys):
            mappings['%s generator' % key] = '%iG' % i
            mappings['%s-compatible microchip' % key] = '%iM' % i
        return '|'.join(''.join(sorted(mappings[item] for item in floor)) for floor in layout)

    # Evaluates each possible move for the given layout.
    # Moves are checked to ensure they're valid and serialised to ensure they haven't been visited
    # Returns a list of new layouts for the next step, or False if a solution was encountered
    def domoves(layout, steps):
        queued = []
        for items, to in moves(layout):
            items = set(items).union({lift})
            new_layout = [set(floor) - items for floor in layout]
            new_layout[to] |= items
            if valid_layout(new_layout):
                serialised = serialise(new_layout)
                if serialised not in distances:
                    distances[serialised] = steps
                    queued.append(new_layout)
                    if target(new_layout):

                        return False
        return queued

    # Run repeated iterations until we hit a winning result, then immediately returns the step
    # count.
    distances = {serialise(floors): 0}
    step = 1
    queued = [floors]
    while True:
        next_queue = []
        for layout in queued:
            res = domoves(layout, step)
            if res == False:
                return step
            next_queue.extend(res)
        queued = next_queue
        step += 1

print("Part 1: %s" % run(floors))

floors[0].extend(['elerium generator', 'elerium-compatible microchip',
                  'dilithium generator', 'dilithium-compatible microchip'])

print("Part 2: %s" % run(floors))
