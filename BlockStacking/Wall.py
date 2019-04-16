
class Wall(object):
    """A class representing a Wall, as a collection of Layers"""

    #
    def __init__(self, layers=[]):
        self.layers = []
        self.height = 0

        self.add_many(layers)

    #
    def add(self, layer):
        self.layers.append(layer)
        self.height += 1

    #
    def add_many(self, layers):
        for layer in layers:
            self.add(layer)

    #
    def top(self):
        return self.layers[-1]

    #
    def __repr__(self):
        return str(self.layers)

