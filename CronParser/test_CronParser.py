# CronParser

# Unit tests

import unittest
import collections

from CronParser import CronParser

class Test_CronParser(unittest.TestCase):

    def setup(self):
        self.cron_parser = CronParser()
        self.TestItem = collections.namedtuple( 'TestItem',
            ['name', 'line', 'expected'] )

        self.test_data = [
            self.TestItem('Empty line', '', False),
            self.TestItem('Comment line', '# Foo', False),
            self.TestItem('Bad Daily *:01', '1 * * * *', False),
            self.TestItem('Daily *:01', '1 * * * * echo Daily', True),
        ]
    

    #
    def test_Parse(self):
        print "\n"

        self.setup()
        tests = self.test_data
        i = 0
        for test in self.test_data:
            i += 1
            parsed = self.cron_parser.parseLine(test.line, i)
            self.assertEqual(parsed, test.expected, "Line ({}) parsed ok ({})".format(test.line, parsed))
        

if __name__ == '__main__':
	unittest.main(verbosity=2)



