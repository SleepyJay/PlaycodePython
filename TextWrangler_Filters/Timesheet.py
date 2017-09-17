#!/usr/bin/python

import fileinput
import re
import collections

Entry = collections.namedtuple('Entry', ['name', 'time'])

sheet = dict()

for thing in sorted(fileinput.input()):
    line = re.sub("\n", "", thing)

    if line == '':
        continue

    tix = line.split('\t')
    tot = float(tix.pop())
    rem = tix.pop()

    for t in tix:
        if t == '':
            continue

        if not t in sheet:
            sheet[t] = 0

        sheet[t] += .25
        tot -= .25

    if not rem in sheet:
        sheet[rem] = 0
    sheet[rem] += tot


for key in sheet:
    print( key + '\t' + str(sheet[key]) )

