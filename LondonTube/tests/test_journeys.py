#!/usr/bin/python

# London Tube Tester: test_journeys.py

from LondonTube.Engine import Engine
import unittest

TUBE_FILENAME = '../data/London tube lines.csv.txt'


class TestLondonTube(unittest.TestCase):
    def test_journeys_dir(self):
        tube = Engine(TUBE_FILENAME)
        found = tube.find_journeys('East Ham', 4)

        expected_results = [
            ('Abbey Road', ['Hammersmith and City', 'DLR']),
            ('Bromley-by-Bow', ['District']),
            ('Canning Town', ['Hammersmith and City', 'Jubilee']),
            ('Dagenham Heathway', ['District']),
            ('Leytonstone High Road', ['District', 'Overground']),
            ('Star Lane', ['District', 'DLR']),
            ('Stratford', ['District', 'Jubilee'])
        ]

        actual_keys = sorted(found)
        actual_count = len(actual_keys)

        expected_count = len(expected_results)
        self.assertEqual(actual_count, expected_count, "Same end nodes found")

        for i in range(actual_count):
            expected = expected_results[i]
            actual_key = actual_keys[i]
            actual = found[actual_key]

            exp_dest = expected[0]
            act_dest = actual.furthest()
            self.assertEqual(act_dest, exp_dest, "Found same dest ({})".format(act_dest))

            exp_lines = expected[1]
            act_lines = actual.lines
            lines_count = len(act_lines)
            for j in range(lines_count):
                act_line = act_lines[j]
                exp_line = exp_lines[j]
                self.assertEqual(
                    act_line, exp_line, "{}: Found same lines ({} vs {})".format(act_dest, act_line, exp_line))

    def test_journeys_undir(self):
        tube = Engine()
        tube.set_directed(0)
        tube.parse_file(TUBE_FILENAME)
        found = tube.find_journeys('East Ham', 4)

        expected_results = [
            ('Abbey Road', ['District', 'DLR']),
            ('Bromley-by-Bow', ['District']),
            ('Canning Town', ['District', 'Jubilee']),
            ('Dagenham Heathway', ['District']),
            ('Leytonstone High Road', ['District', 'Overground']),
            ('Star Lane', ['District', 'DLR']),
            ('Stratford', ['District', 'Jubilee'])
        ]

        actual_keys = sorted(found)
        actual_count = len(actual_keys)

        expected_count = len(expected_results)
        self.assertEqual(actual_count, expected_count, "Same end nodes found")

        for i in range(actual_count):
            expected = expected_results[i]
            actual_key = actual_keys[i]
            actual = found[actual_key]

            exp_dest = expected[0]
            act_dest = actual.furthest()
            self.assertEqual(act_dest, exp_dest, "Found same dest ({})".format(act_dest))

            exp_lines = expected[1]
            act_lines = actual.lines
            lines_count = len(act_lines)
            for j in range(lines_count):
                act_line = act_lines[j]
                exp_line = exp_lines[j]
                self.assertEqual(
                    act_line, exp_line, "{}: Found same lines ({} vs {})".format(act_dest, act_line, exp_line))


if __name__ == '__main__':
    unittest.main(verbosity=2)
