import AIE
import Cell
from Cell import Cell, CellIndex
import Vec2
from Vec2 import Vec2

class Pathfinder:
	def __init__(self, _cellsize, _rows, _cols):
	#Pathfinder constructor, initializes all member variables.
		self.rows = _rows
		self.cols = _cols
		self.cells = [[ 0 for i in range(_cols)] for i in range(_rows)] # The list of ACTUAL CELLS contained in the pathfinder
		self.open = [] # The list of open cell IDs, NOT ENTIRE CELLS. See the CellID class on Cell.py
		self.closed = [] # The list of closed cell IDs, NOT ENTIRE CELLS... 
		self.start = 0
		self.target = 0
		self.current = 0
		self.findingPath = False
		for i in range (0, _cols):
			for j in range(0, _rows):
				self.cells[i][j] = Cell( _cellsize, _cellsize, Vec2(j * _cellsize, i * _cellsize), True)
				self.cells[i][j].ID = CellIndex(i,j)
				
	def FindMaxF(self):	
	#Iterates through the open list and returns the cell with the highest f score
		fScores = []
		for i in range (len(self.open)):
			print("self.open", i, self.open[i])
			fScores.append(self.open[i].f)
		maxF = max(fScores)
		fScores = []
		for i in range (len(self.open)):
			print("self.open", i, self.open[i].f)
			print(fScores)
			if(self.open[i].f == maxF):
				return self.open[i]
	
	def Findpath(self,_startCell, _targetCell):
		self.start = _startCell
		self.target = _targetCell
		self.start.CalcG()
		self.start.CalcH(self.target)
		self.start.CalcF()
		print(self.target, self.target.Index())
	#Step 1: Add starting cell ID to open list
		print(self.open, len(self.open))
		self.open.append(self.start)
	
		if(self.findingPath == False):
			print(len(self.start.NeighborIDs()))
			for i in range (8):
				neighborRow = self.start.NeighborIDs()[i].row
				neighborCol = self.start.NeighborIDs()[i].col
				self.cells[neighborRow][neighborCol].parent = self.start
				self.cells[neighborRow][neighborCol].CalcG()
				self.cells[neighborRow][neighborCol].CalcH(self.target)
				self.cells[neighborRow][neighborCol].CalcF()
		self.findingPath == True

	#Step 2: Find highest F score of all cells in the open list, the highest f scored cell is the " current cell "
		self.open.append(self.current)
		self.current = self.FindMaxF()
		self.open.remove(self.current)
		self.closed.append(self.current)
	#Step 3: Repeat this iteration process for each of the 8 adjacent cells to the current cell:
		# a) If the cell is not passable or on the closed list, do nothing.
		for i in range (len(self.current.NeighborIDs())):  #Search through neighbors list
			neighborRow = self.current.NeighborIDs()[i].row
			neighborCol = self.current.NeighborIDs()[i].col
			for j in range (len(self.closed)): #Iterate through pathfinder closed list
				if(self.current.NeighborIDs()[i].index == self.closed[j].Index() or self.cells[neighborRow][neighborCol].passable == False): #If it finds a match, skip the next two iterations and start checking the next neighbor
					continue
		#b) If the cell isn't on the open list: ADD it to the open list , SET the current cell as its parent, and RECALCULATE its G H and F scores
			for k in range (len(self.open)): 
				if(self.current.NeighborIDs[i].index != self.open[k].Index()): 
					self.open.append(cells[NeighborIDs[i].row][NeighborIDs[i].col])
					self.cells[neighborRow][neighborCol].parent = self.current
					self.cells[neighborRow][neighborCol].CalcG()
					self.cells[neighborRow][neighborCol].CalcH(self.target)
					self.cells[neighborRow][neighborCol].CalcF()
					
		#c) If it's on the open list already, check for superior path-ing through the current square.
			for n in range (len(self.open)): 
				if(self.current.NeighborIDs[i].index == self.open[n].Index()):
					gVal = 0
					if( self.current.Orthogonal(self.cells[neighborRow][neighborCol]) == True):
						gVal = 10
					else:
						gVal = 14
					if( self.cells[neighborRow][neighborCol].g < self.current.g + gVal):
						self.cells[neighborRow][neighborCol].parent = currentCell
						self.cells[neighborRow][neighborCol].CalcG()
						self.cells[neighborRow][neighborCol].CalcH(self.target)
						self.cells[neighborRow][neighborCol].CalcF()
					else:
						pass
			
		#d) Stop when the target cell has been added to the closed list.
			for q in range (len(self.closed)):
				if(self.closed[q].Index() == self.target.Index()):
					trace = self.target
					while(trace.Index() != self.start.Index()):
						trace = trace.parent
						print(trace.Index())
					self.findingPath = False
				
		#self.open.remove(self.current)
		#self.closed.append(self.current)
		self.current = self.FindMaxF()
				
								
	def Update(self):
		for x in range (0, self.rows):
			for y in range(0, self.cols):
				self.cells[x][y].Draw()
	
	
			
		
	
			
		
		