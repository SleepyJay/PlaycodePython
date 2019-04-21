# CronParser

# Unit tests

import unittest
import collections
from CronParser import CronParser
from CronEntry import CronEntry


class Test_CronEntry(unittest.TestCase):

    #
    def setup(self):
        print()

        cron_parser = CronParser()
        self.cron_entry = CronEntry(cron_parser.Schedule('*', '*', '*', '*', '*'), '#')

        self.TestItem = collections.namedtuple('TestItem', ['name', 'value', 'expected'])

        self.test_minute_data = [self.TestItem('minute 1', '1', [1])]
        self.test_hour_data = [self.TestItem('hour 1', '1', [1])]
        self.test_month_day_data = [self.TestItem('month day 1', '1', [1])]
        self.test_month_data = [self.TestItem('month 1', '1', [1])]
        self.test_weekday_data = [self.TestItem('Monday', '1', [CronEntry.Monday])]

    # This is just to tests the split mechanism
    def test_ParseMinutes(self):
        self.setup()

        for test in self.test_minute_data:
            actual = self.cron_entry.parse_minutes(test.value)
            self.assertEqual(actual, test.expected, "{}: {} ==> {}".format(
                test.name, actual, test.expected
            ))

        for test in self.test_hour_data:
            actual = self.cron_entry.parse_hours(test.value)
            self.assertEqual(actual, test.expected, "{}: {} ==> {}".format(
                test.name, actual, test.expected
            ))

        for test in self.test_month_day_data:
            actual = self.cron_entry.parse_month_days(test.value)
            self.assertEqual(actual, test.expected, "{}: {} ==> {}".format(
                test.name, actual, test.expected
            ))

        for test in self.test_month_data:
            actual = self.cron_entry.parse_months(test.value)
            self.assertEqual(actual, test.expected, "{}: {} ==> {}".format(
                test.name, actual, test.expected
            ))

        for test in self.test_weekday_data:
            actual = self.cron_entry.parse_week_days(test.value)
            self.assertEqual(actual, test.expected, "{}: {} ==> {}".format(
                test.name, actual, test.expected
            ))


if __name__ == '__main__':
    unittest.main(verbosity=2)
