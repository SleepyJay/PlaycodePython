# InterviewCake 2017-37 and 2017-38 combo

## Current Version (WIP)
Given any two numbers, `x` and `y` you should be able to get a random distribution between 1 and `x` by using a function `randY()` (which gives integers between 1 and Y). 

If the numbers are equal, it’s obviously trivial. 

1. If `x` is a multiple of `y`, you can partition the values using a simple mod. For instance, `rand2()` from `rand4()`, so [1,2,3,4] can easily be partitioned into [1,2].
2. If `x` is smaller than`y`, you can rely on rerolling if the number chosen is larger than `x` (also works if multiple `x`’s can fit in `y`unevenly). It’s like pretending the first case, but ignoring rolls that are too big. For instance, `rand2()` from `rand5()`, so [1,2,3,4], ignore 5, and partition like case 1.
3. If `x` is larger than`y`, you can 


## Original Text

### 2017-37
You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that generates a random integer from 1 to 5.

rand7() returns each integer with equal probability. rand5() must also return each integer with equal probability.

### 2017-38
You have a function rand5() that generates a random integer from 1 to 5. Use it to write a function rand7() that generates a random integer from 1 to 7.

rand5() returns each integer with equal probability. rand7() must also return each integer with equal probability.

## Dev Notes

## Todo:
1. Implement basic `rand5` and `rand7` from Python
1. Confirm equal distribution of values
1. Implement `rand5_from_rand7` and `rand7_from_rand5`
1. Confirm equal distribution of values

