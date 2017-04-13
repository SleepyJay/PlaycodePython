# Run Tube journeys

from LondonTube import LondonTube

STOPS_AWAY = 5
TUBE_FILENAME = './London tube lines.csv.txt'

tubeDir = LondonTube(TUBE_FILENAME)
found = tubeDir.findJourneys('East Ham', STOPS_AWAY)

for nodeName in sorted(found):
    journey = found[nodeName]
    print '{} (lines = {})'.format(journey.furthest(), str(", ".join(journey.lines)))

print "----------------"

tubeNonDir = LondonTube()
tubeNonDir.setDirected(0)
tubeNonDir.parseFile(TUBE_FILENAME)
found = tubeNonDir.findJourneys('East Ham', STOPS_AWAY)

for nodeName in sorted(found):
    journey = found[nodeName]
    print '{} (lines = {})'.format(journey.furthest(), str(", ".join(journey.lines)))


    



	
