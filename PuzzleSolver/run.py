# Run Solvers

import sys
from PuzzleSolver.Puzzle.DiamondPuzzle import DiamondPuzzle

action = "all"
if len(sys.argv) > 1:
    action = (sys.argv[1]).lower()

if action == "diamond" or action == "all":
    dp = DiamondPuzzle()
    solution = dp.solve()
    print("Diamond Solution ({}): {} ".format(dp.iterations, solution))

if action == "lightsOut" or action == "all":
    print("LightsOutPuzzle: not currently fully implemented")
    #lo = LightsOutPuzzle()
    #solution = lo.solve()
    #print("LightsOut Solution ({}): {} ".format(lo.iterations, solution));




