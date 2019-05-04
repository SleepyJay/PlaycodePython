# PuzzleSolver

## Intro
I was playing some casual video game one day with various puzzles. One of them was the Diamond Puzzle (below). I figured I could write a program to solve these kinds of things, so I did. Then I also did it for the Lights Out type puzzle (below). 

I'm moving towards a somewhat generic idea of a puzzle solver, but not quite there yet.

## Approach
The algorithm I used is **not** brute force, but instead, it makes a bunch of random moves and tracks the boards state. If a move takes me back to a previous state, then we can essentially reset back to that state and remove all extra moves. This allows me to prune all the way back to a handful of moves WITHOUT needing to brute force them all. Of course, it is possible that this algorithm yields no answer, in which case we stop trying after 1000 moves.



## Diamond Puzzle
Imagine a puzzle where you have a set of diamonds that are clickable. Each time you click one, it toggles itself and some other diamonds between "off" and "on". You are trying to turn them all to "on". The pattern of what toggles isn't as "regular" as wit Lights Out.

The program runs by taking a starting point as a string and then the program finds the moves needed to solve it as output. 

## Lights Out Puzzle
This ones comes up occassionally. You have a 5x5 grid. Clicking on a square in the grid toggles itself and all (non-diagonal) adjacent squares. Goal is to turn all to "off". This one might not be done yet.
