# Cell Class
import AIE
import Vec2
from Vec2 import Vec2
import Sprite
from Sprite import Sprite
import math
from math import fabs
import Pathfinder
from Pathfinder import Pathfinder

class CellIndex:
	def __init__(self, _row, _col):
		self.loc = (_row, _col)
		self.row = _row
		self.col = _col

class Cell:
	
	def __init__(self, _width, _height, _pos, _passable, _owner):
	#Cell class constructor. Initializes all member variables.
		self.width = _width			#cell's width in pixels
		self.height = _height		#cell's heigh in pixels
		self.pos = _pos				#cell's screen position expressed as Vec2 ( see Vec2 module ). PASS A FUCKING VEC2 IN PLS.
		self.active = False			#cell's active flag, when a cell is activated it will aquire its neighbors.
		self.rendered = True
		self.g = 0					#cell's g score ( calculated as [ g score of parent cell + x ] , x = 10 if this cell is orthogonal from parent, x = 14 if it diagonal from its parent _
		self.h = 0					#cell's h score ( calculated using "Manhattan method" total number of vertical/horizontal moves it takes to get from this cell to target cell ) 
		self.f = 0					#cell's f score ( calculated as [ g score + h score ] )
		self.index = CellIndex(-1,-1)			#cell's position in the grid EXPRESSED AS TUPLE [0] = ROW [1] = COL, initialized to -1, -1 because they are invalid positions ( potential debugging )
		self.passable = _passable	#cell's passable flag, if a cell is passable it can be moved through and will be added to the open list of the pathfinder its contained when it is iterated over. 
		self.parent = "No Parent!" 	#cell's parent cell, all cell's with the exception of the starting cell should have a parent cell that they belong to.
		self.owner = _owner			#cell's owner, the owner is the pathfinder that the cell belongs to
		self.neighbors = [] 		#cell's neighbors will be its bordering cells (contained in its owner - the pathfinder) , see SetNeighbors()
		self.debug = False			#cell's debug, flag, if enabled it will call ConsoleDebug() in .Update()
		self.debugSprite = AIE.CreateSprite("./images/yellowdot.png", 25, 25)
	def Hotspot(self, _hotspotID): 
	#Hotspot function. Hotspots are a concept I learned in high school through Digipen, a Hotspot is a position inside a sprite that you want to have easy access to.
	#In this case, 0 = Top Left Corner, 1 = Top Right Corner, 2 = Bottom Left Corner, 3 = Bottom Right Corner
		if _hotspotID == 0:
			return Vec2(self.pos.x - (self.width / 2), self.pos.y - (self.height / 2 ))
		if _hotspotID == 1:
			return Vec2(self.pos.x + (self.width / 2), self.pos.y - (self.height / 2 ))
		if _hotspotID == 2:
			return Vec2(self.pos.x - (self.width / 2), self.pos.y + (self.height / 2 ))	
		if _hotspotID == 3:
			return Vec2(self.pos.x + (self.width / 2), self.pos.y + (self.height / 2 ))
		else:
			print "Not a valid Hotspot ID\n"
			
	def ValidID(self):
	#Determines if this cell has a valid cell ID within the pathfinder
		if(	self.index.row >= 0 
			and self.index.col >= 0 
			and	self.index.row <= self.owner.rows 
			and self.index.col <= self.owner.cols ):
			return True
		else:
			print "This cell does not have a valid index\n"
			return False
			
	def ContainsSprite(self, _sprite):
	#If the sprite's position is in between all of the cell's corners (Hotspots), then it is inside the cell.
		if (	(_sprite.pos.x > self.Hotspot(0).x and _sprite.pos.y > self.Hotspot(0).y)
			and (_sprite.pos.x < self.Hotspot(1).x and _sprite.pos.y > self.Hotspot(1).y)
			and (_sprite.pos.x > self.Hotspot(2).x and _sprite.pos.y < self.Hotspot(2).y)
			and (_sprite.pos.x < self.Hotspot(3).x and _sprite.pos.y < self.Hotspot(3).y)) :
			return True
		else:
			pass
			
	def Orthogonal(self, _cell):
	#If the cell shares a row or a column with the cell being passed in as an argument it's Orthogonal. Otherwise it's diagonal.
		if self.index.row == _cell.index.row or self.index.col == _cell.index.col:
			return True
		else:
			return False
	
	def Diagonal(self, _cell):
	#If the cell does NOT share a cell or row with the cell being passed in as an arg it's Diagonal. Otherwise it's orthogonal.
		if self.index.row != _cell.index.row and self.index.col != _cell.index.col:
			return True
		else:
			return False
			
	def IsStart(self):
	#Determines whether the cell is marked as the starting cell in the pathfinder
		if self.index.loc == self.owner.startCell.index.loc:
			return True
		else:
			return False
			
	def IsTarget(self):
	#Determines whether the cell is marked as the target cell in the pathfinder
		if self.index.loc == self.owner.targetCell.index.loc:
			return True
		else:
			return False
			
	def InOpenList(self):
	#Determines whether the cell is in the open list of its owner
		for i in range(0 , len(self.owner.openList)):
			if self.index.loc == self.owner.openList[i].index.loc:
				return True
			else:
				continue
		return False

	def InClosedList(self):
	#Determines whether the cell is in the closed list of its owner
		for i in range(0 , len(self.owner.closedList)):
			if self.index.loc == self.owner.closedList[i].index.loc:
				return True
			else:
				continue
		return False
	
	def SetNeighbors(self):
	#Sets the neighbors of the cell. Checks for valid IDs on each first.
		print "SetNeighbors() Call!\n"
		print str(self.index.loc)
		neighborIndexes = []
		#CW Iteration starting from NW
		neighborIndexes.append( CellIndex(self.index.row - 1, self.index.col - 1)) #NW
		neighborIndexes.append( CellIndex(self.index.row - 0, self.index.col - 1)) #N
		neighborIndexes.append( CellIndex(self.index.row + 1, self.index.col - 1)) #NE
		neighborIndexes.append( CellIndex(self.index.row + 1, self.index.col - 0)) #E
		neighborIndexes.append( CellIndex(self.index.row + 1, self.index.col + 1)) #SE
		neighborIndexes.append( CellIndex(self.index.row - 0, self.index.col + 1)) #S
		neighborIndexes.append( CellIndex(self.index.row - 1, self.index.col + 1)) #SW
		neighborIndexes.append( CellIndex(self.index.row - 1, self.index.col + 0)) #W
		
		for i in range (0, len(neighborIndexes)):
			if (neighborIndexes[i].row < 0 or neighborIndexes[i].col < 0) or (neighborIndexes[i].row > self.owner.rows or neighborIndexes[i].col > self.owner.cols):
				print "Passing over index " + str(neighborIndexes[i].loc)
				pass
			else:
				print "Adding cell " + str(neighborIndexes[i].loc) + " to neighbors[]!"
				self.neighbors.append(self.owner.cells[neighborIndexes[i].row][neighborIndexes[i].col])
		
			

	def CalcG(self):
	#If the cell is the starting cell, it has a g score of 0
		if self.IsStart():
			self.g = 0
		if self.parent != "No Parent!" and self.IsStart() == False :
	#Determines what gVal is in g = parent.g + gVal ; gVal is 10 if it's orthogonal to its parent, gVal = 14 if it's diagonal to its parent
			gVal = 0
			if self.Orthogonal(self.parent):
				gVal = 10 #If ortho to parent, add 10.
			if self.Diagonal(self.parent):
				gVal = 14 #Otherwise it's diag to parent, add 14.
			#Calculation happens here.
			self.g = self.parent.g + gVal
	
		
	def CalcH(self):
	#Calculated using " Manhattan Method " : 
		# Manhattan Method - Total number of moves vertically/horizontally (NOT diagonal) it takes to get from self to target cell (ignores all collision)
	#Formula - finds  the abs val of the difference between its own index and the destination cells index, then multiplies by 10
		#If the cell is the destination cell, its h score is obviously 0. 
		self.h = (	fabs(self.index.row - self.owner.targetCell.index.row) + fabs(self.index.col - self.owner.targetCell.index.col)	) * 10
		if self.IsTarget():
			self.h = 0
		#Example - The cell is at [2][1] in the grid, and the target cell is at [1][7]
		# abs (2 - 1) + abs ( 1 - 7) = 1 + 6
		# 1 + 6 = 7
		# 7 * 10 = 70
	#So in the example the cell would have an H score of 70
		
	def CalcF(self):
	#Cell's g score + cell's h score = cell's f score
		if self.IsStart(): #Cell can't have an fScore without a gScore
			self.f = 99999
		if self.parent != "No Parent!" and self.IsStart() == False:
			self.f = self.g + self.h

			
	def ConsoleDebug(self):
		print "\nCell " + str(self.index.loc) + " information: "
		print "- position - " + str((self.pos.x , self.pos.y)) 
		neighborsStr = "- neighbors - "
		for n in range (0, len(self.neighbors)):
			neighborsStr += str(self.neighbors[n].index.loc) + " "
		print neighborsStr
		print "- passable? - " + str(self.passable)	
		print "- parent - " + str(self.parent.index.loc)
		print "- gScore - " + str(self.g) 
		print "- hScore - " + str(self.h) 
		print "- fScore - " + str(self.f) 
		if self.IsStart():
			print "- This cell is the starting cell."
		else:
			pass
		self.ValidID()
		
	def Draw(self):
	#Using AIE Framework's imported Draw Line function to draw lines between all four corners of the cell.
	#Vec2 x and y are floats, DrawLine MUST have integers... -_-
		if self.rendered == True:
			AIE.DrawLine( int(self.Hotspot(0).x) , int(self.Hotspot(0).y), int(self.Hotspot(1).x), int(self.Hotspot(1).y))
			AIE.DrawLine( int(self.Hotspot(1).x) , int(self.Hotspot(1).y), int(self.Hotspot(3).x), int(self.Hotspot(3).y))
			AIE.DrawLine( int(self.Hotspot(3).x) , int(self.Hotspot(3).y), int(self.Hotspot(2).x), int(self.Hotspot(2).y))
			AIE.DrawLine( int(self.Hotspot(2).x) , int(self.Hotspot(2).y), int(self.Hotspot(0).x), int(self.Hotspot(0).y))
			if(self.parent != "No Parent!"):
				AIE.DrawLine( int(self.pos.x), int(self.pos.y), int(self.parent.pos.x), int(self.parent.pos.y))
				AIE.MoveSprite(self.debugSprite, int(self.pos.x), int(self.pos.y))
				AIE.DrawSprite(self.debugSprite)
			AIE.DrawString( str(int(self.f)), int(self.Hotspot(0).x) + 5, int(self.Hotspot(0).y) + 10) 
			AIE.DrawString( str(int(self.g)), int(self.Hotspot(2).x) + 5, int(self.Hotspot(2).y) - 40) 
			AIE.DrawString( str(int(self.h)), int(self.Hotspot(3).x) - 40, int(self.Hotspot(3).y) - 40)			
	def Update(self):
		self.CalcH()
		self.CalcG()
		self.CalcF()
		self.Draw()
		
		
			

	
	