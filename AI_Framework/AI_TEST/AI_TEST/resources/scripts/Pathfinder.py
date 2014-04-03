import copy 					#Python copy module
from copy import copy
import operator					#Python operator module
from operator import attrgetter
import AIE
import Cell
import Vec2
from Vec2 import Vec2

#TO DO:
	# Organize into functions more
	# Assert errors in problematic situations ( ex - belonging to the open & closed list at the same time )
	# Disable corner cutting
	# Disable G H and F scores for parent and target cells completely

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
		#Get & Init target cell
			self.targetCell 		= self.cells[_targetCellIndex[0]][_targetCellIndex[1]]			
			#self.targetCell.active	= True
			self.targetCell.debug	= True
			print self.targetCell.index.loc
		#Get & Init starting cell
			self.startCell 			= self.cells[_startingCellIndex[0]][_startingCellIndex[1]] #Arguments should have been Tuples , maybe add more flexibility later
			#self.startCell.active	= True													   #Active cells 
			self.startCell.parent 	= self.startCell
			self.startCell.SetNeighbors()
			self.startCell.debug 	= True #Set their debug flags
			self.startCell.Update()
		#Set the start cell as its neighbors' parent
			for i in range (0, len(self.startCell.neighbors)): #Mark the starting cell as its neighbor's parent
				self.startCell.neighbors[i].parent = self.startCell
				self.startCell.neighbors[i].Update()
				self.openList.append(self.startCell.neighbors[i])
				#print self.startCell.neighbors[i].index.loc , self.startCell.neighbors[i].g
		#Add a COPY of the starting cell to the open list
			self.closedList.append(copy(self.startCell))
		else:
			pass
			
	def FindPath(self):
	#Primary loop, will repeat the A* Pathfinding sequence until the target cell is added to the closed list.
	
		#Step 1 - Search for the lowest F cost cell on the open list, it is now the " Current Cell " 
		print "\nFindpath()..."
		self.openList.sort(key = attrgetter('f'),) #Sort the list by f score				
		print "\nLowest F Score Cell: " + str(self.openList[0].index.loc) + ":" + str(self.openList[0].f)
		self.currentCell = self.cells[self.openList[0].index.row][self.openList[0].index.col]
		print "Current Cell: " + str(self.currentCell.index.loc)
		if self.currentCell.index.loc == self.targetCell.index.loc:
			print "Done!"
			return
		#Step 2) - Switch the cell with the lowest F score to the closed list
		self.closedList.append(self.openList[0])
		self.openList.remove(self.openList[0])	
		#Step 3) - For each of the current cell's neighbors, perform the following three checks/responses:
		self.currentCell.SetNeighbors()
		for i in range (0, len(self.currentCell.neighbors)):
			self.currentCell.neighbors[i].Update()
			#Check One - If the cell is not passable or on the closed list - do nothing.
			if self.currentCell.neighbors[i].InClosedList() == True or self.currentCell.neighbors[i].passable == False:
				continue
			#Check Two - If the cell is NOT on the open list, add it to the open list (cell.update re-calculates ghf scores every frame)
			if self.currentCell.neighbors[i].InOpenList() == False and self.currentCell.neighbors[i].passable == True:
				self.cells[self.currentCell.neighbors[i].index.row][self.currentCell.neighbors[i].index.col].parent = self.currentCell
				self.currentCell.neighbors[i].Update()
				self.openList.append(copy(self.currentCell.neighbors[i]))
				continue
			#Check Three - If the cell is on the open list, check to see if the path through this cell is superior. 
				# Meaning - If the current.g + x < neighbor.g (x = 10 if the current cell is 
			if self.currentCell.neighbors[i].InOpenList() == True:
				gVal = 0
				if self.currentCell.Orthogonal(self.currentCell.neighbors[i]):
					gVal = 10
				if self.currentCell.Diagonal(self.currentCell.neighbors[i]):
					gVal = 14
				if self.currentCell.Orthogonal(self.currentCell.neighbors[i]) and self.currentCell.Diagonal(self.currentCell.neighbors[i]):
					print "Orientation error between cell:" + str(self.currentCell.neighbors[i].index.loc) + " and " + str(self.currentCell.index.loc)
				if self.currentCell.g + gVal < self.currentCell.neighbors[i].g:
					self.currentCell.neighbors[i].parent = self.currentCell
					self.currentCell.neighbors[i].Update()
				else:
					pass
		
			
		
		
	def Update(self):
		for x in range (0, self.rows):
			for y in range(0, self.cols):
				self.cells[x][y].Draw()
	
			
		
	
			
		
		