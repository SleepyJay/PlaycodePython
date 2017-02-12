# Puzzler Solver Base

import random

__package__ = "puzzle"

class Puzzle(object):
	
	def __init__(self, starting_point = None, goal = None):
		self.MAX_ITERS = 1000
		self.MAX_SOLVE_ATTEMPTS = 50
		
		self.starting_point = self.toIntList(starting_point)
		self.goal = self.toIntList(goal)
		
		self.solutions = []
		self.prevStates = {}
		self.currentState = []
		self.iterations = []
		self.solveAttempts = 0
		
		self.createBoard()
		self.reset()

	#
	def createBoard(self):
		self.board = []
	
	#
	def reset(self, to_str = None):
		to_str = to_str or self.starting_point
		vals = list(to_str)
		for i in range(self.getRange()):
			self.setInt(i, int(vals[i]))
			
	#
	def getBoardState(self):
		if not self.currentState:
			self.currentState = self.calcBoardState()
		return self.currentState
	
	#
	def calcBoardState(self):
		board = []
		for position in self.board:
			board.append(position['value'])	
		return board
	
	#
	def clearBoardState(self):
		self.currentState = []
		
	def toIntList(self, str_):
		return map(lambda x: int(x), list(str_)) 

	#
	def getRange(self):
		return len(self.starting_point)
	
	#
	def get(self, index):
		return self.board[index]

	#
	def getInt(self, index):
		pos = self.get(index)
		return pos['value']

	#
	def setInt(self, index, int_):
		self.clearBoardState()
		pos = self.get(index)
		pos['value'] = int_

	#
	def flip(self, index):
		position = self.get(index)
		position['value'] = (0 if position['value'] else 1)

	# move is an int
	def move(self, move):
		self.clearBoardState()
		position = self.get(move)
		for aff in position['affects']:
			self.flip(aff)

	# moves is list of ints
	def moveMany(self, moves):
		for mv in moves:
			self.move(int(mv))	
	
	#
	def unmove(self, move):
		self.move(move)
	
	#
	def getRandomMove(self):
		range_ = self.getRange()
		rand_ = random.randrange(0,range_,1)
		return rand_
	
	#
	def solve(self):
		self.reset()
		moves = []
		for g in range(self.MAX_ITERS):
			mv = self.getRandomMove()
			self.move(mv)
			moves.append(mv)
			
			if(self.getBoardState() == self.goal):
				moves = self.prune(moves)
				self.solutions.append(moves)
				self.iterations.append(g)
				return moves
		
		self.iterations.append(self.MAX_ITERS-1)	
		return None

	#
	def solveMany(self, n):
		s = 0
		for i in range(self.MAX_SOLVE_ATTEMPTS):
			while(s < n):
				solution = self.solve()
				if solution:
					s += 1		
	
	#
	def solveShortest(self, n):
		self.solveMany(n)
		best = ()
		min_ = 0
		for s in self.solutions:
			if( (not min_) or min_ > len(s)):
				min_ = len(s)
				best = s
		
		self.solveAttempts += 1
		return best
	
	#
	def confirmSolution(self, solution):
		self.reset()
		self.moveMany(list(solution))
		curr = self.getBoardState()
		return (curr == self.goal)
	
	#
	def clearSolutions(self):
		self.solutions = []
	
	#
	def prune(self, solution):
		start = list(self.starting_point)
		moveCounts = {}
		for b in solution:
			if b in moveCounts:
				moveCounts[b] += 1
			else:
				moveCounts[b] = 1
		
		pruned = []
		# moving the same position an odd number of times means you changed the value
		for (k, v) in moveCounts.items():
			if v % 2:
				pruned.append(k)
		
		return pruned
