# PlaycodePython.GridMenu

A job interview asked some approximation of this question.

Q: You have a grid of letters, a cursor on screen, and a remote. The remote moves the cursor, i.e. up, down, left, right. There is an enter button to select the letter on which the cursor is over. Design a program to take in cursor direction input and output the string of letters produced. 

A: In the interview, a 2D array popped into my head first, but I reduced it down to just a single-dimension array. And this is how I first solved it, 1D array (gridMenu.py). 

I've also been thinking about just trying the 2D-array solution, which will be called gridMenu2D.py.

Note, as interesting additional things, I added a backspace and space as moves that can also be input (these are NOT currently letters in the grid). Also, using a 6-column grid uses 5 rows for 26 letters leaves 4 empty columns at the end of the last row with which to deal.

There is no requirement on the alphabet used. As such, you supply how many columns and what the alphabet looks like. The code does the rest.

TODO:

* Add space as a move
* Refactor move function
* Add some documentation
* Implement better debug-system (or remove entirely)
* Add 2D version
