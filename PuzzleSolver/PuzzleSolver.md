# PuzzleSolver

I was playing a video game that has puzzles as part of it's game play. In one of the puzzles, you have these diamonds that you are trying to turn all to "on". Each time you touch a diamond, it toggles itself and some other diamonds between "off" and "on". You want them to end up all on. 

I figured I could write a program to solve this, which I did. You give it the starting point as a string and it outputs the moves needed to solve it. 

The algorithm I used is not brute force, but instead, it makes a bunch of random moves and tracks the boards state. If a move takes me back to a previous state, then we can essentially reset back to that state and remove all extra moves. This allows me to prune all the way back to a handful of moves WITHOUT needing to brute force them all. It is possible that this algorithm yields no answer, in which case we stop trying after 1000 moves.

I started on using this code for the classic 5x5 grid for the "Lights Out" puzzle, but it is not finished.

TODO:

* Finish writing the Lights Out solution
