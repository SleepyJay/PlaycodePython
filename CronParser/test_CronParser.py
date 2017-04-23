# CronParser

# Unit tests

import unittest
import collections
import inspect

from CronParser import CronParser
from CronParser import LineType

class Test_CronParser(unittest.TestCase):

    #
    def setup(self):
        print ""

        self.cron_parser = CronParser()
        self.TestItem = collections.namedtuple( 'TestItem',
            ['name', 'line', 'expected'] )

        self.test_data = [
            self.TestItem('Empty line', '', LineType.empty),
            self.TestItem('Comment line', '# Foo', LineType.comment),
            self.TestItem('Missing command *:01', '1 * * * *', None),
            self.TestItem('Missing schedule', 'echo Foo', None),

            self.TestItem('Daily *:01', '1 * * * * echo Daily', LineType.cron),
            self.TestItem('Daily nums', '1 2 3 4 5 echo Daily', LineType.cron),
            self.TestItem('Daily *:01, pound', '1 * * * * # echo Daily', LineType.cron),
        ]

        self.expected_test_data_cron_count = 3
        self.expected_test_file_cron_count = 2


    #
    def test_LexLines(self):
        self.setup()
        for i in range(len(self.test_data)):
            test = self.test_data[i]
            type = self.cron_parser.lexLine(test.line, i)
            self.assertEqual(type, test.expected,
                "Line ({}) parsed ok ({})".format(test.line, type))

    #
    def test_ParseLines(self):
        self.setup()
        lines = []
        for test in self.test_data:
            lines.append(test.line)

        parsed_list = self.cron_parser.parseLines(lines)
        print "ParsedLines: {}".format(parsed_list)
        list_count = len(parsed_list)
        self.assertEqual(list_count, self.expected_test_data_cron_count,
            "ParsedLines resulted in {} crons".format(list_count))
        

    #
    def test_ParseFile(self):
        self.setup()
        parsed_list = self.cron_parser.parseFile('./crontab_test')
        
        list_count = len(parsed_list)
        self.assertEqual(list_count, self.expected_test_file_cron_count,
            "ParsedFiles resulted in {} crons".format(list_count))



if __name__ == '__main__':
	unittest.main(verbosity=2)



