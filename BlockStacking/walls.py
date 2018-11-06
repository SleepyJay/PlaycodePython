#!/usr/bin/python

from Engine import Engine
from datetime import datetime
import sys

# This code actually builds the walls, which could be interesting.
# However, it is too slow to do this way for large sets (like around 42x5 or 48x2, etc.).

started = datetime.now()
print("Started: {}".format(datetime.ctime(started)))

# Change these params to change output...
target_width = 42
target_height = 4
width_small = 3
width_large = 4.5
print_walls = False


if len(sys.argv) > 1:
    target_width = float(sys.argv[1])
    target_height = int(sys.argv[2])

engine = Engine()

engine.build_blocks(width_small, width_large)
print("Blocks built: {}\n".format(len(engine.blocks)))

engine.build_layers(target_width)
layers_duration = datetime.now() - started
print("Layers built: {}".format(len(engine.layers)))
print("Layers Finished after: ~ {}.{} seconds.\n".format(layers_duration.seconds, layers_duration.microseconds))

engine.build_walls(target_height)
walls_duration = datetime.now() - started
count = len(engine.walls)
print("Walls built: {}".format(count))
print("Walls building took: ~ {}.{} seconds.\n".format(walls_duration.seconds, walls_duration.microseconds))

for wall in engine.walls:
    # Change to True for wall-printing
    if print_walls:
        print("W: {}".format(wall))


