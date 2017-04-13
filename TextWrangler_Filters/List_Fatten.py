#!/usr/bin/python
import fileinput
import re

str = ''
MAX_LENGTH = 80
for thing in sorted(fileinput.input()):
    line = re.sub("\n", "", thing)

    if line == '':
        continue

    if len(str) + len(line) >= MAX_LENGTH:
        print str
        str = line
    else:
        str += line

print str
