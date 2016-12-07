#!/usr/bin/python3

import re

# Returns True if x contains an ABBA sequence
abba = lambda x: re.match(r'.*(.)(?!\1)(.)\2\1.*', x)
# Returns all trigrams in x
tris = lambda x: [x[i:i+3] for i in range(len(x) - 2) if '#' not in x[i:i+3]]
# Returns all ABA sequences in x
abas = lambda x: [t for t in tris(x) if t[0] == t[2] and t[1] != t[0]]
# Swaps an ABA trigram into BAB
swap = lambda x: x[1] + x[0] + x[1]
# Returns all hypernet parts (between brackets) of x
hypernet = lambda x: re.sub(r'^.*?\[|\].*?\[|\].*?$', '#', x)
# Returns all supernet parts (outside of brackets) of x
supernet = lambda x: re.sub(r'\[.*?\]', '#', x)

with open('07.txt', 'r') as file:
    ips = list(map(str.strip, file.readlines()))
    # tls: has at least one ABBA that's not also in its hypernet sections
    tls = set(filter(abba, ips)) - set(filter(lambda ip: abba(hypernet(ip)), ips))
    # ssl: has an ABA in the supernet and a BAB in the hypernet
    ssl = [ip for ip in ips if set(map(swap, abas(supernet(ip)))).intersection(set(abas(hypernet(ip))))]
    
    print("Part one: %s" % len(tls))
    print("Part two: %s" % len(ssl))