#!/usr/bin/python

import collections

class FoodXP(object):
    '''FoodXP calculations'''

    #
    def __init__(self, menu=[]):
        self.ItemTuple = collections.namedtuple('Item', ['name', 'cost', 'health', 'xp'])
        self.menu = menu

    # Give me the cheapest health combo (trivial)
    def bestHealth:
        pass

    # Give me the cheapest XP combo (trivial)
    def bestXP(self, layers):
        pass

    # Give me the best health-xp combo (interesting)
    def bestCombo(self):
        pass

    #
    def __repr__(self):
        return str(self.menu)

    #





