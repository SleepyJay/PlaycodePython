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
    def parse_lines(self, lines):
        for i in range(len(lines)):
            self.lex_line(lines[i], i)
        return self.parsed_entries

    #
    def lex_line(self, line, lno):
        line = line.rstrip()

        m = self.re_cron_line.match(line)
        if m:
            schedule = self.to_schedule_tuple(m.group(1))
            print("cron: {} ==> {}".format(m.group(1,3), schedule))
            entry = CronEntry(schedule, m.group(3))
            self.parsed_entries.append(entry)
            return LineType.cron

        if self.re_comment_line.match(line):
            return LineType.comment
        elif self.re_empty_line.match(line):
            return LineType.empty
        else:
            return None

    #
    def parse_file(self, file_path):
        f = open(file_path, 'r')

        if not f:
            # Exception?
            pass
        
        lines = list(map((lambda x: x.rstrip()), f.readlines()))

        f.close()
        return self.parse_lines(lines)

    # 
    def to_schedule_tuple(self, schedule_str):
        # Possibly not all quite this simple, :)
        return self.Schedule( *(schedule_str.split()) )

