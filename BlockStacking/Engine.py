#!/usr/bin/python

from Block import Block
from Layer import Layer
from Wall import Wall

class Engine(object):
    '''A class to build Walls.'''

    #
    def __init__(self):
        self.blocks = []
        self.layers = []
        self.walls = []
        self.current_width = 0

    #
    def buildBlocks(self, *sizes):
        # When building blocks, reset cached width
        self.current_width = 0
        for sz in sizes:
            self.blocks.append(Block(sz))

    #
    def buildLayers(self, width):
        # Don't rebuild layers if called again with same width
        if self.current_width == width:
            return
        
        queue = []
        final = []
        
        for block in self.blocks:
            if block.size > width:
                continue
            layer = Layer( [block] )
            queue.append(layer)

        while len(queue):
            next_queue = [] # attempt to reduce memory pressure
            for layer in queue:
                for block in self.blocks:
                    if layer.width + block.size > width:
                        continue
                    # lazy clone:
                    newLayer = Layer(layer.blocks)
                    newLayer.add(block)

                    if newLayer.width == width:
                        final.append(newLayer)
                    else:
                        next_queue.append(newLayer)

            queue = next_queue
            
        self.layers = final
        self.current_width = width
        
        self.preCacheLayers()


    #
    def preCacheLayers(self):
        layer_len = len(self.layers)
        for i in range(layer_len):
            layer = self.layers[i]
            for j in range(i, layer_len):
                under = self.layers[j]
                stackable = under.checkCanStack(layer)

                if stackable:
                    under.can_be_stacked.add(layer)
                    layer.can_be_stacked.add(under)

    #
    def buildWalls(self, height):
        queue = []
        final = []

        for layer in self.layers:
            wall = Wall( [layer] )
            queue.append(wall)

        if height == 1:
            self.walls = queue
            return

        while len(queue): 
            next_queue = [] # attempt to reduce memory pressure
            for wall in queue:
                top = wall.top()
                for layer in top.can_be_stacked:
                    newWall = Wall(wall.layers)
                    newWall.add(layer)

                    if newWall.height == height:
                        final.append(newWall)
                    else:
                        next_queue.append(newWall)
                        
            queue = next_queue

        self.walls = final

    #
    def countWalls(self, height):
        if height <= 0:
            return 0

        if height == 1:
            return len(self.layers)

        total = 0
        for l in range(height, 1, -1):
            for layer in self.layers:
                if l == height:
                    count = len(layer.can_be_stacked)
                    layer.levels[l] = count
                else:
                    count = 0
                    for stackable in layer.can_be_stacked:
                        if l+1 in stackable.levels:
                            count += stackable.levels[l+1]

                        layer.levels[l] = count

        # I know this seems weird that I'm using 2, but it represents the
        # running sum of combinations of stacking TO that level, i.e. from 1->2.
        for layer in self.layers:
            if 2 in layer.levels:
                total += layer.levels[2]
        return total

    #
    def wallCount(self):
        return len(self.walls)


    #
    def __repr__(self):
        return str(self.__dict__)

    #
    




