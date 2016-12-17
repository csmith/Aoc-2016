#!/usr/bin/python3

import re

# Version of parse() that recursively parses repeated sections
rparse = lambda x: parse(x, rparse)


def parse(data, rfun=len):
    # Find the first bracketed part (if one exists)
    index, bracket = data.find('('), data.find(')')
    if index == -1:
        return len(data)

    # Grab the (NxR) values from the brackets
    num, reps = map(int, data[index + 1:bracket].split('x'))

    # Return the initial, non-repeated data, plus...
    return (len(data[:index])
            # the repeated data, potentially parsed recursively, plus...
            + reps * rfun(data[bracket + 1:bracket + 1 + num])
            # the remainder of the string, parsed
            + parse(data[bracket + 1 + num:], rfun))


with open('data/09.txt', 'r') as file:
    input = re.sub('\s+', '', file.read())
    print(parse(input))
    print(rparse(input))
