#!/usr/bin/python

import fileinput
import re
import collections

sheet = dict()

for thing in sorted(fileinput.input()):
    line = re.sub("\n", "", thing)

    if line == '':
        continue

    tix = line.split('\t')
    tot = tix.pop()
    if not tot or tot == '0.00':
        continue

    tot = float(tot)
    rem = tix.pop()

    for t in tix:
        t.strip()

        if t == '':
            continue

        if not t in sheet:
            sheet[t] = 0

        sheet[t] += .25
        tot -= .25

    if not rem in sheet:
        sheet[rem] = 0
    sheet[rem] += tot

total = 0
for key in sheet:
    total += sheet[key]
    print( key + '\t' + str(sheet[key]) )

print("\ntotal: {}".format(total))
