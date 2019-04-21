# Block Stacking (v 1.4.5)

The idea is that you have certain sized blocks, in the general case one is 3 cm and the other is 4.5 cm, for which you want to build a wall of various widths and heights using these blocks. When stacking, blocks must overlap all  "seams" that appear in the layer below. 

The other point was to 

####Running

There are no build instructions. You have a few choices on what you might run.

First, there are "tests". Really, these just excercise the wall counting algorithm, making sure the expected number of walls come back in a reasonable amount of time.





There are three runnable choices:

1. Run tests:
    * The main point of this was
    1. `python test.py`: run all "fast" tests currently available.
    2. `python test.py slow`: will run all tests currently available, including slow ones.
    3. 



`prove tests/test_Engine.py`: runs several different block scenarios and counts possible walls (efficient). This ends with finding 392 Quadrillion, 48 x 12 walls combos in under 7 seconds.
2. `build_walls.py`: does actual wall building (inefficient), instead of just counting. This is really slow. Accepts width and height arguments on command line (see performance below). Prints one wall. (Default 42 x 4) 
3. `run.py`: will do wall counting (efficient) for passed in width and height (default 27 x 7).   

#### Design Notes
Given the two block sizes, we can can create a set of layers of a certain length. Each of these layers can be combined with each other such that they can or cannot be stacked (by the rule of all "seams" have to be covered). 

Once you have what can stack on what, you can easily build walls. However, building all of the walls in memory takes a lot of resources. So instead, you start from the top and count all possible stackings as you move down the height. This becomes significantly more efficient.


####Comments on Performance
Even with some pruning, the brute force approach (where all walls were built as as it runs) only got me as far as 48x4 (before I got bored of waiting). To get to 48x10 and beyond, required improving the code by orders of magnitude. 

As of v1.4, performance has been significantly improved in the stacking area. 

Where L is number of possible layers and H is height of walls:

* Layer creation is now ```O(L^2)```, pruned
* Wall counting is now ```O(L^2 * H)```

(I keep the H around in the big-O above, since a thin, REALLY TALL wall might make the height parameter significant.)

####Counts and Timings (approx, YMMV):
ALL of these now run in around 5-7 seconds (on my computer). The bulk of the time is still in testing stacking.

```
* 48x2:                   37,120 walls
* 48x4:               10,178,548 walls
* 48x6:            3,919,649,942 walls
* 48x8:        1,722,438,038,790 walls
* 48x10:     806,844,323,190,414 walls
* 48x12: 392,312,088,153,557,198 walls
```

###Version 1.4 changes:
* Added timing to testing, because why not?
* Made it fast enough to crack 48x12 in just under 7 seconds

###Version 1.3 changes:
* Added testing
* Made it fast enough to crack 48x10 in about a minute

###Version 1.2 changes:
* Made it faster

###Version 1.1 changes:
* Made it faster
* Made the output better for run.py