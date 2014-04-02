import AIE

import Cell
import Vec2
from Vec2 import Vec2

class Pathfinder:
	def __init__(self, _cellsize, _rows, _cols):
	#Pathfinder constructor, initializes all member variables.
		self.rows = _rows
		self.cols = _cols
		self.cells = [[0 for j in range(_cols)] for i in range(_rows)] # The list of ACTUAL CELLS contained in the pathfinder
		self.openList = [] 												# List of open cells (passed in as COPIES from the original cells list)
		self.closedList = [] 											# List of closed cells (passed in as COPIES from the original cells list)
		self.startCell = 0												# Starting Cell 
		self.targetCell = 0												# Target Cell
		self.currentCell = 0											# Current Cell aka the cell with the highest F score whose neighbors are being iterated through
		self.findingPath = False										# Flag to signal that the pathfinder is currently finding a path(start will not be called)
		self.pathComplete = False										# Flag to signal that the pathfinder has found a path
		self.noPath = False												# Flag to signal that the pathfinder could not find a path
		for i in range (0, _rows):
			for j in range(0, _cols):
				self.cells[i][j] = Cell.Cell( _cellsize, _cellsize, Vec2(j * _cellsize, i * _cellsize), True, self)
				self.cells[i][j].index = Cell.CellIndex(i,j)
	
	def Start(self, _startingCellIndex, _targetCellIndex):
	#If the pathfinder hasn't been started yet...
		if self.findingPath == False:
			self.findingPath 		= True
			print "Pathfinder.Start()...\n"
			self.startCell 			= self.cells[_startingCellIndex[0]][_startingCellIndex[1]] #Set starting and target cells
			self.targetCell 		= self.cells[_targetCellIndex[0]][_targetCellIndex[1]]
			self.startCell.active	= True
			self.targetCell.active	= True
			self.startCell.parent 	= self.startCell
			self.startCell.SetNeighbors()
			self.startCell.debug 	= True #Set their debug flags
			self.targetCell.debug	= True
			
			for i in range (0, len(self.startCell.neighbors)): #Mark the starting cell as its neighbor's parent
				self.startCell.neighbors[i].parent = self.startCell
				
			self.openList.append(self.startCell)
		
		else:
			pass
			
	def Update(self):
		for x in range (0, self.rows):
			for y in range(0, self.cols):
				self.cells[x][y].Update()

	
			
		
	
			
		
		