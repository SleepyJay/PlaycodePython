#!/usr/bin/python

# Run Tube journeys

from LondonTube.Engine import Engine

STOPS_AWAY = 5
TUBE_FILENAME = './data/London tube lines.csv.txt'

tubeDir = Engine(TUBE_FILENAME)
found = tubeDir.find_journeys('East Ham', STOPS_AWAY)

for nodeName in sorted(found):
    journey = found[nodeName]
    print(f'{journey.furthest()} (lines = {str(", ".join(journey.lines))})')

print("----------------")

tubeNonDir = Engine()
tubeNonDir.set_directed(0)
tubeNonDir.parse_file(TUBE_FILENAME)
found = tubeNonDir.find_journeys('East Ham', STOPS_AWAY)

for nodeName in sorted(found):
    journey = found[nodeName]
    print(f'{journey.furthest()} (lines = {str(", ".join(journey.lines))})')
