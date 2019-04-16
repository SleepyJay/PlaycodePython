#!/usr/bin/python

from BlockStacking.Engine import Engine
from datetime import datetime
import sys

started = datetime.now()
print("Started: {}".format(datetime.ctime(started)))

# Change these params to change output...
target_width = 27
target_height = 7
width_small = 3
width_large = 4.5

print(f"Building walls {target_width} W x {target_height} H using block sizes [{width_small}, {width_large}]")

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

count = engine.count_walls(target_height)
walls_duration = datetime.now() - started
print("Walls found: {}".format(count))
print("Walls Finished after: ~ {}.{} seconds.\n".format(walls_duration.seconds, walls_duration.microseconds))

