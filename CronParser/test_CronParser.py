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
            self.TestItem('Empty line', '', 'empty'),
            self.TestItem('Comment line', '# Foo', 'comment'),
            self.TestItem('Missing command *:01', '1 * * * *', None),
            self.TestItem('Missing schedule', 'echo Foo', None),
            self.TestItem('Daily *:01', '1 * * * * echo Daily', 'cron'),
            self.TestItem('Daily *:01, pound', '1 * * * * # echo Daily', 'cron'),
        ]
    

    #
    def test_LexLines(self):
        print "\n"

        self.setup()
        tests = self.test_data
        i = 0
        for test in self.test_data:
            i += 1
            parsed = self.cron_parser.lexLine(test.line, i)
            self.assertEqual(parsed, test.expected, "Line ({}) parsed ok ({})".format(test.line, parsed))

        
        

if __name__ == '__main__':
	unittest.main(verbosity=2)



