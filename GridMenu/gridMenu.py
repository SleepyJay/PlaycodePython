# GridMenu 

import math

class GridMenu(object):
	
	#
	def __init__(self, cols, alphabet):
		self.cols = cols
		self.alphabet = alphabet
		self.position = 0
		self.max = len(alphabet)-1
		self.full = int(math.ceil(self.max / self.cols))
		self.string = ''
		
		self.actions = {
			'D': self.cols,
			'U': -self.cols,
			'R':  1,
			'L': -1
		}
		
	#
	def moveMany(self, moves):
		for move in moves:
			if move == 'E':
				self.string += self.getLetter()
			elif move == 'B':
				self.string[:-1] 
			else:
				self.move(move)
				
		return self.string
	
	#
	def move(self, move):
		if move == 'D':
			self.position += self.cols
			
			if self.position > self.max:
				self.position -= self.full
				
		elif move == 'U':
			self.position -= self.cols
			
			if self.position < 0:
				self.position += self.full			
			
		elif move == 'R':
			self.position += 1
			
			if self.position >self.max:
				self.position -= self.cols				
			
			
		elif move == 'L':
			self.position -= 1
			
			if self.position < 0:
				self.position += self.cols			
			
			
		else:
			pass
			
			
	def clear(self):
		self.string = ''
		self.position = 0
	
	
	def getString(self):
		return self.string
		
	def getLetter(self):
		return self.alphabet[self.position]
