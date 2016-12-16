#!/usr/bin/python3

import re
from collections import namedtuple

with open('04.txt', 'r') as file:
    Room = namedtuple('Room', 'name sector checksum')
    rooms = [Room(*re.search(r'^(.*?)-([0-9]+)\[(.*?)\]$', l).groups()) for l in file.readlines()]
    checksum = lambda x: re.sub(r'(.)\1+', r'\1',
                                ''.join(sorted(x.name.replace('-', ''),
                                               key=lambda c: -128 * x.name.count(c) + ord(c)))
                               )[:5]
    valid = [room for room in rooms if room.checksum == checksum(room)]
    print("Part one: %s" % sum([int(room.sector) for room in valid]))

    for room in valid:
        decoded = ''.join([' ' if c == '-' else chr(97 + (int(room.sector) + ord(c) - 97) % 26) for c in room.name])
        if 'north' in decoded:
            print("Part two: '%s' is in sector %s" % (decoded, room.sector))
