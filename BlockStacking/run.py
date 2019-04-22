#!/usr/bin/python

# Counting walls is by far the more efficent usage, by orders of magnitude, but walls are not actually stored.
# Building walls actually produces walls, but is VERY slow.

# If `--print_walls` is True, you will get walls. A LOT of walls, like ~900,000 walls (for default)!
# They would look something like this
# (you can sorta see the overlaping principle, even just with numbers):
# W: [
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
# [4.5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4.5],
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
# [4.5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4.5]
# ]

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BlockStacking.Engine import Engine
from datetime import datetime
import argparse

"""Build or count walls with options"""

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, default=27)
parser.add_argument('--height', type=int, default=7)

## Not ready to support these:
# parser.add_argument('--small=small')
# parser.add_argument('--large=large')

parser.add_argument('--build_walls', action="store_true", help='Builds walls in memory (slow) instead of merely counting them')
parser.add_argument('--print_walls', action="store_true", help='Prints all walls built; WARNING: this may be a LOT of output')
parser.add_argument('--one_wall', action="store_true", help='Print one of the walls built as an example')
args = parser.parse_args()

# Change these params to change output...
target_width = args.width # 27
target_height = args.height # 7
width_small = 3
width_large = 4.5

print(f"Building walls {target_width} W x {target_height} H using block sizes [{width_small}, {width_large}]\n")

engine = Engine()

started = datetime.now()
engine.build_blocks(width_small, width_large)
blocks_duration = datetime.now() - started
print("Blocks built: {}".format(len(engine.blocks)))
print("Blocks finished after: ~ {}.{} seconds.\n".format(blocks_duration.seconds, blocks_duration.microseconds))

started = datetime.now()
engine.build_layers(target_width)
layers_duration = datetime.now() - started
print("Layers built: {}".format(len(engine.layers)))
print("Layers finished after: ~ {}.{} seconds.\n".format(layers_duration.seconds, layers_duration.microseconds))

count = 0
started = datetime.now()

if args.build_walls or args.one_wall or args.print_walls:
    count = engine.build_walls(target_height)
else:
    count = engine.count_walls(target_height)

walls_duration = datetime.now() - started
print("Walls of {} x {} built: {}".format(target_width, target_height, count))
print("Walls finished after: ~ {}.{} seconds.\n".format(walls_duration.seconds, walls_duration.microseconds))

if args.print_walls:
    for wall in engine.walls:
        print("W: {}".format(wall))
elif args.one_wall:
    wall = engine.walls[0]
    print('First wall created: [')

    for layer in wall.layers:
        print(f"     {layer}")

    print(']')

