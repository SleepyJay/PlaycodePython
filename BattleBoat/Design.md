# BattleBoat - Design Notes.

## TODO
1. django: POST vs GET
2. django: get POST content
3. django: templates
4. views: render foo-output
5. GameBoard: fix loading-state for no-spaces

## Assets

### Game
1. Consists of two players, each with 1 board.
2. Table: { id (PK int), player1(FK int), player2(FK int), board1 (string), board2 (string), status (LU int) } 

### Board
1. Each board contains a NxN set of Cells.
3. Boards should be initialized with boat positions.
4. Boards should know how to validate positions.
5. Boards can tell you what is in a cell.
6. Boards can "attack" a cell.  
7. Boards should load string data ==> array.
8. Boards should define thingy_ids: [ open, 2_boat_1, 2x3_boat, 1x4_boat, 1x5_boat  ] 

### Cell
2. Cells have two sets of states:
    1. Stuff: [ open, 2-boat, 3-boat, 4-boat ]
    2. Discovery: [ unknown, miss, hit ]  
3. String rep:  

### Player
1. foo

### DataAccessLayer
1. bar

### WebController
1. baz

### Web UI
1. Django
2. Backbone
3. 2-grids, one clickable
