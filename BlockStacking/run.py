#!/usr/bin/python

from Engine import Engine
from datetime import datetime
import sys

started = datetime.now()
print("Started: {}".format(datetime.ctime(started)))


target_width = 27
target_height = 5

if len(sys.argv) > 1:
    target_width =  float(sys.argv[1])
    target_height = int(sys.argv[2])

engine = Engine()

engine.buildBlocks(3, 4.5)
print("Blocks built: {}\n".format(len(engine.blocks)))

engine.buildLayers(target_width)
print("Layers built: {}".format(len(engine.layers)))
layers_duration = datetime.now() - started
print("Layers Finished after: ~ {}.{} seconds.\n".format(layers_duration.seconds, layers_duration.microseconds))

## This actually builds the walls, which could be interesting for debugging
## However, it is too slow to do this way, starting around 48x2 (?)
# engine.buildWalls(target_height)
# for wall in engine.walls:
#     print "W: {}".format(wall)

count = engine.countWalls(target_height)
print("Walls found: {}".format(count))
walls_duration = datetime.now() - started
print("Walls Finished after: ~ {}.{} seconds.\n".format(walls_duration.seconds, walls_duration.microseconds))

