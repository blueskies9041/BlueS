import math
from math import sqrt, pow

## Vec2 Class ##
class Vec2:
# __init__ is a special "constructor" esque function, must have self as first arg
	def __init__( self, _x, _y): 
		self.x = _x
		self.y = _y	
	def Mag(self):
		return sqrt((pow(self.x, 2) + pow(self.y, 2)))
	def Distance(self, _otherVec):
		return sqrt( pow( (_otherVec.x - self.x) , 2) + pow( (_otherVec.y - self.y), 2))