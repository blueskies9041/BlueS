# Cell Class
import AIE
import Vec2
from Vec2 import Vec2
import Sprite
from Sprite import Sprite
import math
from math import fabs

class CellIndex:
	def __init__(self, _row, _col):
		self.loc = (_row, _col)
		self.row = _row
		self.col = _col

class Cell:
	
	def __init__(self, _width, _height,_pos, _passable):
	#Cell class constructor. Initializes all member variables.
		self.width = _width			#cell's width in pixels
		self.height = _height		#cell's heigh in pixels
		self.pos = _pos				#cell's screen position expressed as Vec2 ( see Vec2 module ). PASS A FUCKING VEC2 IN PLS.
		self.g = 0					#cell's g score ( calculated as [ g score of parent cell + x ] , x = 10 if this cell is orthogonal from parent, x = 14 if it diagonal from its parent _
		self.h = 0					#cell's h score ( calculated using "Manhattan method" total number of vertical/horizontal moves it takes to get from this cell to target cell ) 
		self.f = 0					#cell's f score ( calculated as [ g score + h score ] )
		self.ID = CellIndex(-1,-1)			#cell's position in the grid EXPRESSED AS TUPLE [0] = ROW [1] = COL, initialized to -1, -1 because they are invalid positions ( potential debugging )
		self.passable = _passable	#cell's passable flag, if a cell is passable it can be moved through and will be added to the open list of the pathfinder its contained when it is iterated over. 
		self.parent = self 			#cell's parent cell, all cell's with the exception of the starting cell should have a parent cell that they belong to.
		
	def Hotspot(self, _hotspotID): 
	#Hotspot function. Hotspots are a concept I learned in high school through Digipen, a Hotspot is a position inside a sprite that you want to have easy access to.
	#In this case, 0 = Top Left Corner, 1 = Top Right Corner, 2 = Bottom Left Corner, 3 = Bottom Right Corner
		if(_hotspotID == 0):
			return Vec2(self.pos.x - (self.width / 2), self.pos.y - (self.height / 2 ))
		if(_hotspotID == 1):
			return Vec2(self.pos.x + (self.width / 2), self.pos.y - (self.height / 2 ))
		if(_hotspotID == 2):
			return Vec2(self.pos.x - (self.width / 2), self.pos.y + (self.height / 2 ))	
		if(_hotspotID == 3):
			return Vec2(self.pos.x + (self.width / 2), self.pos.y + (self.height / 2 ))
	
	def Row(self):
		return self.ID.row
	
	def Col(self):
		return self.ID.col
	
	def Index(self):
		return self.ID.index
			
	def ValidID(self):
	#Determines if this cell has a valid cell ID within the pathfinder
		if(self.Row() >= 0 and self.Col() >= 0):
			return True
		else:
			return False
	
	def NeighborIDs(self):
		neighbors = []
		neighbors.insert( 0, CellIndex(self.Row() - 1, self.Col() - 1) )
		neighbors.insert( 1, CellIndex(self.Row() - 1, self.Col()	   ) )
		neighbors.insert( 2, CellIndex(self.Row() - 1, self.Col() + 1) )
		neighbors.insert( 3, CellIndex(self.Row()    , self.Col() - 1) )
		neighbors.insert( 4, CellIndex(self.Row()    , self.Col() + 1) )
		neighbors.insert( 5, CellIndex(self.Row() + 1, self.Col() - 1) )
		neighbors.insert( 6, CellIndex(self.Row() + 1, self.Col()	   ) )
		neighbors.insert( 7, CellIndex(self.Row() + 1, self.Col() + 1) )
		return neighbors
	
	def ContainsSprite(self, _sprite):
	#If the sprite's position is in between all of the cell's corners (Hotspots), then it is inside the cell.
		if( 	(_sprite.pos.x > self.Hotspot(0).x and _sprite.pos.y > self.Hotspot(0).y)
			and (_sprite.pos.x < self.Hotspot(1).x and _sprite.pos.y > self.Hotspot(1).y)
			and (_sprite.pos.x > self.Hotspot(2).x and _sprite.pos.y < self.Hotspot(2).y)
			and (_sprite.pos.x < self.Hotspot(3).x and _sprite.pos.y < self.Hotspot(3).y)) :
			return True
			
	def Orthogonal(self, _cell):
	#If the cell shares a row or a column with the cell being passed in as an argument it's Orthogonal. Otherwise it's diagonal.
		if( self.Row() == _cell.Row() or self.Col() == _cell.Col()):
			return True
		else:
			return False
			
	def CalcG(self):
	#Determines whether to add 10 or 14 to the gVal the cell's gValue.
		gVal = 0
		if( self.Orthogonal(self.parent)):
			gVal = 10 #If ortho to parent, add 10.
		else:
			gVal = 14 #Otherwise it's diag to parent, add 14.
		self.g = self.parent.g + gVal
		
	def CalcH(self, target):
	#Calculated using " Manhattan Method " : Total number of moves vertically/horizontally (NOT diagonal) it takes to get from self to target (ignores all collision)
	#self.ID is a tuple where [0] is the cell's ROW, and [1] is the cell's COLUMN
		self.h = (	fabs(self.Row() - target.Row()) + fabs(self.Col() - target.Col())	) * 10
		
	def CalcF(self):
	#Cell's g score + cell's h score = cell's f score
		self.f = self.g + self.h
		
	def Draw(self):
	#Using AIE Framework's imported Draw Line function to draw lines between all four corners of the cell.
		AIE.DrawLine( int(self.Hotspot(0).x) , int(self.Hotspot(0).y), int(self.Hotspot(1).x), int(self.Hotspot(1).y))
		AIE.DrawLine( int(self.Hotspot(1).x) , int(self.Hotspot(1).y), int(self.Hotspot(3).x), int(self.Hotspot(3).y))
		AIE.DrawLine( int(self.Hotspot(3).x) , int(self.Hotspot(3).y), int(self.Hotspot(2).x), int(self.Hotspot(2).y))
		AIE.DrawLine( int(self.Hotspot(2).x) , int(self.Hotspot(2).y), int(self.Hotspot(0).x), int(self.Hotspot(0).y))
		AIE.DrawString( str((self.Row(),self.Col())), int(self.pos.x) - 25, int(self.pos.y) - 25) 

	
	