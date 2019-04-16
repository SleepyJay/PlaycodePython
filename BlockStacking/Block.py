
# Sooo sparse, I know. I would have used a namedtuple, but made it a class for the __repr__


class Block(object):
    """A class representing a Block, which has a size"""
    
    #
    def __init__(self, size):
        self.size = size
    
    #
    def __repr__(self):
        return str(self.size)
