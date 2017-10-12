#!/usr/bin/python

import fileinput
import re
import datetime

sheet = dict()

for thing in sorted(fileinput.input()):
    line = re.sub("\n", "", thing)

    if not line: continue

    tix = line.split('\t')

    # Do not convert to float until '0.00', spaces, and '' are sorted out
    tot = tix.pop()
    tot = re.sub(" ", "", tot)

    if not tot: continue
    tot = float(tot)

    # Do not keep 0 duration tasks around
    if not tot: continue

    # Task for which to apply remaining time
    rem = tix.pop()

    for t in tix:
        t.strip()
        if not t: continue

        if not t in sheet:
            sheet[t] = 0

        sheet[t] += .25
        tot -= .25

        if not tot: break

    if not rem in sheet:
        sheet[rem] = 0
    sheet[rem] += tot


#
def prettier(tm):
    return ':'.join(str(tm).split(':')[:2])


##
total = 0
tm_start = datetime.timedelta(hours=9)
tm_end = tm_start

for key in sheet:
    total += sheet[key]
    tm_end = tm_start + datetime.timedelta(hours=sheet[key])
    print("{}\t{}\t{}-{}".format(key, sheet[key], prettier(tm_start), prettier(tm_end)))
    tm_start = tm_end

print("\ntotal: {}".format(total))
