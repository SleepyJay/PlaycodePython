# CronParser

# Unit tests

import unittest
import collections

from CronParser import CronParser

class Test_CronParser(unittest.TestCase):

    #
    def setup(self):
        print "\n"

        self.cron_parser = CronParser()
        self.TestItem = collections.namedtuple( 'TestItem',
            ['name', 'line', 'expected'] )

        self.test_data = [
            self.TestItem('Empty line', '', 'empty'),
            self.TestItem('Comment line', '# Foo', 'comment'),
            self.TestItem('Missing command *:01', '1 * * * *', None),
            self.TestItem('Missing schedule', 'echo Foo', None),
            self.TestItem('Daily *:01', '1 * * * * echo Daily', 'cron'),
            self.TestItem('Daily *:01, pound', '1 * * * * # echo Daily', 'cron'),
        ]

        self.expected_test_data_cron_count = 2


    #
    def test_LexLines(self):
        self.setup()
        for i in range(len(self.test_data)):
            test = self.test_data[i]
            parsed = self.cron_parser.lexLine(test.line, i)
            self.assertEqual(parsed, test.expected, "Line ({}) parsed ok ({})".format(test.line, parsed))

    #
    def test_ParseLines(self):
        self.setup()
        lines = []
        for test in self.test_data:
            lines.append(test.line)

        parsed_list = self.cron_parser.parseLines(lines)
        list_count = len(parsed_list)
        self.assertEqual(list_count, self.expected_test_data_cron_count,
            "ParsedLines resulted in {} crons".format(list_count))
        
        
if __name__ == '__main__':
	unittest.main(verbosity=2)



