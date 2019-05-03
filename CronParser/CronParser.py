# CronParser

import re
from collections import namedtuple
from CronParser.CronEntry import CronEntry


Schedule = namedtuple('Schedule', 'minutes, hours, month_days, months, weekdays')
LineType = namedtuple('LineType', 'cron, comment, empty')

RE_cron_line = re.compile('\s*(([^\s]\s+){5})(.+)')
RE_comment_line = re.compile('^\s*#')
RE_empty_line = re.compile('^\s*$')


class CronParser(object):

    def __init__(self):
        self.parsed_entries = []

    def parse_lines(self, lines):
        for i in range(len(lines)):
            self.lex_line(lines[i], i)
        return self.parsed_entries

    def lex_line(self, line, lno):
        line = line.rstrip()

        m = RE_cron_line.match(line)
        if m:
            schedule = self.to_schedule_tuple(m.group(1))
            print("cron: {} ==> {}".format(m.group(1,3), schedule))
            entry = CronEntry(schedule, m.group(3))
            self.parsed_entries.append(entry)
            return LineType.cron

        if RE_comment_line.match(line):
            return LineType.comment
        elif RE_empty_line.match(line):
            return LineType.empty
        else:
            return None

    def parse_file(self, file_path):
        f = open(file_path, 'r')

        if not f:
            # Exception?
            pass
        
        lines = list(map((lambda x: x.rstrip()), f.readlines()))

        f.close()
        return self.parse_lines(lines)

    def to_schedule_tuple(self, schedule_str):
        # Possibly not all quite this simple, :)
        return Schedule(*(schedule_str.split()))
