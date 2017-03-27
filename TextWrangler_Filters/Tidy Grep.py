#!/usr/bin/python
import fileinput
import re

last = ''
for thing in sorted(fileinput.input()):
    line = re.sub("\n", "", thing)

    if line == '':
        continue

    m = re.match("([^:]*):", line)

    if m == None:
        print line
        continue

    grp = m.group(1)

    if grp == None:
        print line
        continue

    if(last != grp):
        print ""
        last = grp

    print line
