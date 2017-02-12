# London Tube Tester: test_journeys.py

from LondonTube import LondonTube
import unittest

TUBE_FILENAME = './London tube lines.csv.txt'

class Test_LondonTube(unittest.TestCase):
    def test_journeys_dir(self):
        tube = LondonTube(TUBE_FILENAME)    
        found = tube.findJourneys('East Ham', 4)
        
        expectedResults = [
            ( 'Abbey Road', ['Hammersmith and City', 'DLR'] ),
            ( 'Bromley-by-Bow', ['District'] ),
            ( 'Canning Town', ['Hammersmith and City', 'Jubilee'] ),
            ( 'Dagenham Heathway', ['District'] ),
            ( 'Leytonstone High Road', ['District', 'Overground'] ),
            ( 'Star Lane', ['District', 'DLR'] ),
            ( 'Stratford', ['District', 'Jubilee'] )
        ]
        
        
        actualKeys = sorted(found)
        actualCount = len(actualKeys)
        
        expectedCount = len(expectedResults)
        self.assertEqual(actualCount, expectedCount, "Same end nodes found")
        
        for i in range(actualCount):
            expected = expectedResults[i]
            actualKey = actualKeys[i]
            actual = found[actualKey]
            
            exp_dest = expected[0]
            act_dest = actual.furthest()
            self.assertEqual(act_dest, exp_dest, "Found same dest ({})".format(act_dest))
            
            exp_lines = expected[1]
            act_lines = actual.lines
            linesCount = len(act_lines)
            for j in range(linesCount):
                act_line = act_lines[j]
                exp_line = exp_lines[j]
                self.assertEqual(act_line, exp_line, "{}: Found same lines ({} vs {})".format(act_dest, act_line, exp_line))
                
    def test_journeys_undir(self):
        tube = LondonTube()
        tube.setDirected(0)
        tube.parseFile(TUBE_FILENAME)        
        found = tube.findJourneys('East Ham', 4)
        
        expectedResults = [
            ( 'Abbey Road', ['District', 'DLR'] ),
            ( 'Bromley-by-Bow', ['District'] ),
            ( 'Canning Town', ['District', 'Jubilee'] ),
            ( 'Dagenham Heathway', ['District'] ),
            ( 'Leytonstone High Road', ['District', 'Overground'] ),
            ( 'Star Lane', ['District', 'DLR'] ),
            ( 'Stratford', ['District', 'Jubilee'] )
        ]
        
        
        actualKeys = sorted(found)
        actualCount = len(actualKeys)
        
        expectedCount = len(expectedResults)
        self.assertEqual(actualCount, expectedCount, "Same end nodes found")
        
        for i in range(actualCount):
            expected = expectedResults[i]
            actualKey = actualKeys[i]
            actual = found[actualKey]
            
            exp_dest = expected[0]
            act_dest = actual.furthest()
            self.assertEqual(act_dest, exp_dest, "Found same dest ({})".format(act_dest))
            
            exp_lines = expected[1]
            act_lines = actual.lines
            linesCount = len(act_lines)
            for j in range(linesCount):
                act_line = act_lines[j]
                exp_line = exp_lines[j]
                self.assertEqual(act_line, exp_line, "{}: Found same lines ({} vs {})".format(act_dest, act_line, exp_line))            

if __name__ == '__main__':
	unittest.main(verbosity=2)
