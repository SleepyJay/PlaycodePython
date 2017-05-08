# GridMenu 

import math

ENTER	= 'E'
BACKSP	= 'B'
SPACE	= 'S'
DOWN 	= 'D'
UP		= 'U'
LEFT	= 'L'
RIGHT	= 'R'

DEBUG   = 0

class GridMenu(object):
	
	#
	def __init__(self, cols, alphabet):
		self.cols = cols
		self.alphabet = alphabet
		self.last = len(alphabet)-1
		
		rows = int(self.last / self.cols)
		if self.last % self.cols:
			rows += 1
		
		self.full = self.cols * rows
		
		self.clear()
		
	#
	def moveMany(self, moves):
		for move in moves:
			if move == ENTER:
				self.string += self.getLetter()
			elif move == BACKSP:
				self.string[:-1] 
			else:
				self.move(move)
				
		return self.string
	
	#
	def move(self, move):
		if move == DOWN:
			if self.atBottomEdge():
				self.position = self.position + self.cols - self.full
				self.log_debug("DOWN + AtBottomEdge: " + self.getLetter())
			else:
				self.position += self.cols
				self.log_debug("DOWN + Else: " + self.getLetter())
			
			if self.inEmptyPos():
				self.move(DOWN)
				self.log_debug("DOWN + InEmpty: " + self.getLetter())
				
		elif move == UP:
			if self.atTopEdge():
				self.position = self.position - self.cols + self.full
				self.log_debug("UP + AtTopEdge: " + self.getLetter())
			else:
				self.position -= self.cols
				self.log_debug("UP + Else: " + self.getLetter())
			
			if self.inEmptyPos():
				self.move(UP)
				self.log_debug("UP + InEmpty: " + self.getLetter())
			
		elif move == RIGHT:
			if self.atRightEdge():
				self.position = self.position - self.cols + 1
				self.log_debug("RIGHT + AtRightEdge: " + self.getLetter())
			else:
				self.position += 1
				self.log_debug("RIGHT + Else: " + self.getLetter())
			
			if self.inEmptyPos():
				self.move(RIGHT)
				self.log_debug("RIGHT + InEmpty: " + self.getLetter())
			
		elif move == LEFT:
			if self.atLeftEdge():
				self.position = self.position + self.cols - 1
				self.log_debug("LEFT + AtLeftEdge: " + self.getLetter())
			else:
				self.position -= 1
				self.log_debug("LEFT + Else: " + self.getLetter())
			
			if self.inEmptyPos():
				self.move(LEFT)
				self.log_debug("LEFT + InEmpty: " + self.getLetter())
			
			
	def clear(self):
		self.string = ''
		self.position = 0
	
	def getPosition(self):
		return self.position
	
	def setPosition(self, pos):
		self.position = int(pos)
	
	def getString(self):
		return self.string
		
	def getLetter(self):
		rtn = ''
		if self.position <= self.last:
			rtn = self.alphabet[self.position]
		
		return rtn
	
	def atLeftEdge(self):
		return (self.position % self.cols == 0)
	
	def atRightEdge(self):
		return ( (self.position % self.cols) + 1 == self.cols)
	
	def atTopEdge(self):
		return (self.position < self.cols)
	
	def atBottomEdge(self):
		return (self.position >= (self.full - self.cols) )
	
	def inEmptyPos(self):
		return (self.position > self.last)
	
	def log_debug(self, message):
		if DEBUG:
			print(message)
	



# 0 1 2 3
# 4 5 6 7
# 8 9 
