#!/usr/bin/python3

with open('data/06.txt', 'r') as file:
    cols = list(zip(*map(str.strip, file.readlines())))
    print(''.join(max(set(col), key=col.count) for col in cols))
    print(''.join(min(set(col), key=col.count) for col in cols))
