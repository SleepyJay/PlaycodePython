# CronParser

# Unit tests

import unittest
from collections import namedtuple
from CronParser.CronParser import CronParser, LineType, Schedule

TestLine = namedtuple('TestLine', 'name, line, expected')
TestSchedule = namedtuple('TestSchedule', 'name, sched_str, expected')


class Test_CronParser(unittest.TestCase):
    
    #
    def setup(self):
        self.cron_parser = CronParser()

        self.test_line_data = [
            TestLine('Empty line', '', LineType.empty),
            TestLine('Comment line', '# Foo', LineType.comment),
            TestLine('Missing command *:01', '1 * * * *', None),
            TestLine('Missing schedule', 'echo Foo', None),

            TestLine('Daily *:01', '1 * * * * echo Daily', LineType.cron),
            TestLine('Daily nums', '1 2 3 4 5 echo Daily', LineType.cron),
            TestLine('Daily *:01, pound', '1 * * * * # echo Daily', LineType.cron),
        ]

        self.expected_test_data_cron_count = 3
        self.expected_test_file_cron_count = 2

        self.test_schedule_data = [
            # name, line, minutes, hours, month_days, months, weekdays
            TestSchedule('Daily *:01', '1 * * * *',
                         Schedule('1', '*', '*', '*', '*')),
            TestSchedule('Daily nums', '1 2 3 4 5',
                         Schedule('1', '2', '3', '4', '5'))
        ]

    #
    def test_Schedule(self):
        self.setup()
        for test in self.test_schedule_data:
            schedule = self.cron_parser.to_schedule_tuple(test.sched_str)
            self.assertEqual(schedule, test.expected,
                             "Schedule ({}) parsed ok ({})".format(schedule, test.expected))

    #
    def test_LexLines(self):
        self.setup()
        i = 0
        for test in self.test_line_data:
            i += 1
            type = self.cron_parser.lex_line(test.line, i)
            self.assertEqual(type, test.expected,
                             "Line ({}) parsed ok ({})".format(test.line, type))

    #
    def test_ParseLines(self):
        self.setup()
        lines = []
        for test in self.test_line_data:
            lines.append(test.line)

        parsed_list = self.cron_parser.parse_lines(lines)
        list_count = len(parsed_list)
        self.assertEqual(list_count, self.expected_test_data_cron_count,
                         "ParsedLines resulted in {} crons".format(list_count))

    #
    def test_ParseFile(self):
        self.setup()
        parsed_list = self.cron_parser.parse_file('./crontab_test_data')

        list_count = len(parsed_list)
        self.assertEqual(list_count, self.expected_test_file_cron_count,
                         "ParsedFiles resulted in {} crons".format(list_count))


if __name__ == '__main__':
    unittest.main(verbosity=2)
