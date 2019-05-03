# PlaycodePython.GridMenu v0.6.0

Runs with Python 3.6.

A job interview asked some approximation of this question.

Q: You have a grid of letters, a cursor on screen, and a remote. The remote moves the cursor, i.e. up, down, left, right. There is an enter button to select the letter on which the cursor is over. Design a program to take in cursor direction input and output the string of letters produced. 

A: In the interview, a 2D array popped into my head first, but I reduced it down to just a single-dimension array. `GridMenu` is the solution as a 1D array. (I've also been thinking about just trying the 2D-array solution, which I would probably call `GridMenu2D.py`.)

`GridMenu` takes a number of columns (defaults to 6) and an alphabet (defaults to the 26 English letters). It builds the appropriate grid from that. Like this, for default:

|   |   |   |   |   |   | 
|---|---|---|---|---|---| 
| a | b | c | d | e | f |
| g | h | i | j | k | l |
| m | n | o | p | q | r |
| s | t | u | v | w | x |
| y | z |   |   |   |   |

It should work if you pass in other values, though. Note the four empty boxes as something that has to be accounted for in the movement. This is done generically by math, since you could pass a different list of items or use a different number of columns.

Once you have a grid, you just pass "moves" to it. Like, `grid.move(code)`, where `code` is one of these single letters:

```
E = enter
B = backspace
S = space
D = down
U = up
L = left
R = right
```

I include a backspace and space in this solution, although they don't occupy space in the grid.

In the default case of 26 letters, a 6-column grid uses 5 rows, with 4 empty columns at the end. Moving around has to make sure it accounts for the empty. 


TODO:

* Add space as a move
* Refactor move function
* Add some documentation
* Implement better debug-system (or remove entirely)
* Add 2D version
