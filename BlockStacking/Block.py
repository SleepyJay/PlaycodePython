#!/usr/bin/python


class Block(object):
    '''A class representing a Block, which has a size'''
    
    #
    def __init__(self, size):
        self.size = size
    
    #
    def __repr__(self):
        return str(self.size)



    
