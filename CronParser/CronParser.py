# CronParser

import re
import collections
from CronEntry import CronEntry

class LineType:
    cron, comment, empty = range(3)

class CronParser(object):

    #
    def __init__(self):
        self.re_cron_line = re.compile('\s*(([^\s]\s+){5})(.+)')
        self.re_comment_line = re.compile('^\s*#')
        self.re_empty_line = re.compile('^\s*$')

        self.Schedule = collections.namedtuple('Schedule',
            ['minutes', 'hours', 'month_days', 'months', 'weekdays'])

        self.parsed_entries = []

    #
    def parseLines(self, lines):
        for i in range(len(lines)):
            line = lines[i]
            parsed_line = self.lexLine(line, i)
            #print "{} ==> {}".format(line, parsed_line)

        return self.parsed_entries


    #
    def lexLine(self, line, lno):
        #print "{}: {}".format(lno, line)
        line = line.rstrip()

        m = self.re_cron_line.match(line)
        if m:
            sched = self.toScheduleTuple(m.group(1))
            print("cron: {} ==> {}".format(m.group(1,3), sched))
            entry = CronEntry(sched, m.group(3))
            self.parsed_entries.append(entry)
            return LineType.cron

        if self.re_comment_line.match(line):
            return LineType.comment
        elif self.re_empty_line.match(line):
            return LineType.empty
        else:
            return None

    #
    def parseFile(self, file_path):
        f = open(file_path, 'r')

        if not f:
            # Exception?
            pass
        
        lines = map( (lambda x: x.rstrip()), f.readlines())
        return self.parseLines(lines)


    # 
    def toScheduleTuple(self, sched_str):
        # Possibly not all quite this simple, :)
        return self.Schedule( *(sched_str.split()) )

