# Block Stacking (v 1.4.1)

The idea is that you have certain sized blocks, in the general case one is 3 cm and the other is 4.5 cm, for which you want to build a wall of various widths and heights using these blocks. When stacking, blocks must overlap all  "seams" that appear in the layer below. 

####Running

There are no build instructions. Simply run on CLI; confirmed compatible with Python 2.7 and Python 3.6. 

I've provided a run.py which will take width and height params (defaults to 27x5), like:
```run.py 48 10```

####Comments on Performance
This problem was really an exercise in performant coding. At some point the brute force approach, even with some pruning, only got me as far as 48x4. To get to 48x10 and beyond, I had to actually think through ways to shave orders of magnitude from the code. 

As of v1.4, performance has been significantly improved in the stacking area. 

Where L is number of possible layers and H is height of walls:

* Layer creation is now ```O(L^2)```, pruned
* Wall counting is now ```O(L^2 * H)```

(I keep the H around in the wall counting, since a thin, REALLY tall wall might make the height parameter significant.)

####Counts and Timings (approx, YMMV):
ALL of these now run in under 7 seconds. The bulk of the time is still in testing stacking.

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
* Made it fast enough to crack 48x10 in just under 7 seconds

###Version 1.3 changes:
* Added testing
* Made it fast enough to crack 48x10 in about a minute

###Version 1.2 changes:
* Made it faster

###Version 1.1 changes:
* Made it faster
* Made the output better for run.py