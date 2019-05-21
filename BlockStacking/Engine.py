
from BlockStacking.Block import Block
from BlockStacking.Layer import Layer
from BlockStacking.Wall import Wall
from BlockStacking.LayerSearchTree import LayerSearchTree


class Engine(object):
    """A class to build Walls."""

    #
    def __init__(self):
        self.blocks = []
        self.layers = []
        self.walls = []
        self.current_width = 0
        self.stree = LayerSearchTree()

    #
    def build_blocks(self, *sizes):
        # When building blocks, reset cached width
        self.current_width = 0
        for sz in sizes:
            self.blocks.append(Block(sz))

    #
    def build_layers(self, width):
        # Don't rebuild layers if called again with same width
        if self.current_width == width:
            return
        
        queue = []
        final = []
        
        for block in self.blocks:
            if block.size > width:
                continue
            layer = Layer([block])
            queue.append(layer)

        while len(queue):
            next_queue = [] # attempt to reduce memory pressure
            for layer in queue:
                for block in self.blocks:
                    if layer.width + block.size > width:
                        continue
                    # lazy clone:
                    new_layer = Layer(layer.blocks)
                    new_layer.add(block)

                    if new_layer.width == width:
                        final.append(new_layer)
                    else:
                        next_queue.append(new_layer)

            queue = next_queue

        self.current_width = width
        self.layers = final

        for layer in final:
            self.stree.add(layer.width_list, layer)

        self.precache_layers()

    #
    def precache_layers(self):
        for layer in self.layers:
            layer.can_be_stacked = self.stree.find_stackable(layer)

    #
    def build_walls(self, height):
        queue = []
        final = []

        for layer in self.layers:
            wall = Wall([layer])
            queue.append(wall)

        if height == 1:
            self.walls = queue
            return

        while len(queue): 
            next_queue = [] # attempt to reduce memory pressure
            for wall in queue:
                top = wall.top()
                for layer in top.can_be_stacked:
                    new_wall = Wall(wall.layers)
                    new_wall.add(layer)

                    if new_wall.height == height:
                        final.append(new_wall)
                    else:
                        next_queue.append(new_wall)
                        
            queue = next_queue

        self.walls = final
        return len(self.walls)

    #
    def count_walls(self, height):
        if height <= 0:
            return 0

        if height == 1:
            return len(self.layers)

        total = 0
        for h in range(height, 1, -1):
            for layer in self.layers:
                if h == height:
                    count = len(layer.can_be_stacked)
                    layer.levels[h] = count
                else:
                    count = 0
                    for stackable in layer.can_be_stacked:
                        if h+1 in stackable.levels:
                            count += stackable.levels[h+1]

                        layer.levels[h] = count

        # I know this seems weird that I'm using 2, but it represents the
        # running sum of combinations of stacking TO that level, i.e. from 1->2.
        for layer in self.layers:
            if 2 in layer.levels:
                total += layer.levels[2]
        return total

    #
    def wall_count(self):
        return len(self.walls)

    #
    def __repr__(self):
        return str(self.__dict__)

