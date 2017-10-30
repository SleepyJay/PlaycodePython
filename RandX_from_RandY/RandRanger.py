import random
from array import *
from math import floor, ceil
from functools import partial
from collections import namedtuple


class RandRanger (object):

    #
    def __init__(self, trials=100):
        self.trials = trials
        self.Result = namedtuple("result", ['spread', 'func', 'misses'])

        self.allow_max_misses = 100

        self.reset()

    #
    def reset(self):
        self.misses = 0

    #
    def run_trials(self, spread_size, func, trials=500):
        self.reset()
        spread = self.build_int_array(spread_size)
        
        if func:
            for run in range(trials):
                n = func()
                spread[n] += 1

        return self.Result(spread.tolist(), func.func, self.misses)

    #
    def best_x_from_y_function(self, x, y, rand_fn=None):
        """Guess at best algorithm to use"""
        algorithm = None
        if x == y:
            algorithm = self.randX_from_randY_value
        elif x < y:
            if divmod(y, x)[1] == 0:
                algorithm = self.randX_from_randY_by_division
            else:
                algorithm = self.randX_from_randY_by_reject
        else: # x > y
            # TODO: Fill this guy in!
            if False:
                algorithm = self.randX_from_randY_by_num_base
            else:
                algorithm = self.randX_from_randY_by_upscale_reject
            
        if algorithm:
            return partial(algorithm, x, y, rand_fn)
        
        return None

    # === randX_from_randY Functions
    # 
    def randX_from_randY_by_reject(self, x, y, rand_fn=None):
        misses = 0

        rand_fn = rand_fn or self.rand_n

        n = rand_fn(y)
        print("rand: {}".format(n))
        while n > x:
            n = rand_fn(y)
            misses += 1

            if misses > self.allow_max_misses:
                # Exception, maybe?
                print("MAX EXCEEDED: {}".format(n))
                self.misses += misses
                return 0
        self.misses += misses
        return n

    #
    def randX_from_randY_by_num_base(self, x, y, rand_fn=None):
        # This needs some checking...
        rand_fn = rand_fn or self.rand_n
        while len(self.bin_run) < x:
            a = rand_fn(y+1)
            l = self.to_bin_list(a-1)
            #print(l)
            self.bin_run.extend(l)
            
        #print(self.bin_run)
        #print(self.bin_run[:x])
        
        s = sum(self.bin_run[:x])
        self.bin_run = []

        return s

    #
    def randX_from_randY_by_division(self, x, y, rand_fn=None):
        rand_fn = rand_fn or self.rand_n
        n = rand_fn(y)
        multiplier = divmod(y, x)[0]
        return divmod(n, multiplier)[0]
    
    #
    def randX_from_randY_value(self, x, y, rand_fn=None):
        """Just returns result of rand_fn, which, careful, could be out of scope""" 
        rand_fn = rand_fn or self.rand_n
        return rand_fn(y) 
        
    #
    def randX_from_randY_by_upscale_reject(self, x, y, rand_fn=None):
        # This needs to be filled in
        pass

    # === Rand Functions
    #
    def rand_n(self, y):
        """Plain ol' randomness"""
        return random.randrange(1, y + 1)
    
    #
    def rand_always_n(self, n, y=None):
        """Get a specific value back"""
        return n
        
    #
    def rand_distributed(self, ask_count, y):
        """Distribute random as evenly as possible""" 
        max_use = ceil(ask_count/y)
        print("{}".format(max_use))
        
        while True:
            used = self.build_int_array(y)
            for i in range(0,ask_count):
                n = self.rand_n(y)
                while used[n] >= max_use:
                    n = self.rand_n(y)
                
                used[n] += 1
                print("{}".format(n))
                yield n

    #
    def init_rand_distributed(self, ask_count, y):
        gen_distributed = self.rand_distributed(ask_count,y)
        return partial(next, gen_distributed)
      
    #
    def rand_consecutive(self, y):   
        self.current += 1
        if self.current > y:
            self.current = 1 
        return self.current
            
    # === Helpers
    #
    def build_int_array(self, size):
        init = []
        for i in range(0, size + 1):
            init.append(0)
        return array('i', init)

    #
    def to_bin_list(self, num, rpad_zeros=0):
        # Seriously dumb way to do this!!
        bin = '{0:b}'.format(num).rjust(rpad_zeros, '0')
        return [int(x) for x in list(bin)]





