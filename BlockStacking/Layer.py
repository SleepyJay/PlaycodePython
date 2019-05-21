
class Layer(object):
    """A class representing a Layer, a collection of Blocks"""
    
    #
    def __init__(self, blocks=None):
        self.blocks = []
        self.width = 0

        self.can_be_stacked = set()
        self.cannot_stack = set()
        self.levels = {}
        self.width_set = set()
        self.width_list = []
        
        self.add_many(blocks or [])

    #
    def add(self, block):
        self.blocks.append(block)
        self.width += block.size
        self.width_set.add(self.width)
        self.width_list.append(self.width)

    #
    def add_many(self, blocks):
        for block in blocks:
            self.add(block)

    #
    def check_can_stack(self, layer):
        for w in self.width_set:
            if self.width == w:
                continue
            if w in layer.width_set:
                return False

        return True

    #
    def __repr__(self):
        return str(self.blocks)
