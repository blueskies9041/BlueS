import AIE
## Grid Class ##
class Grid:
	def __init__(self, _cellSize, _rows, _cols):
		self.cellSize = _cellSize
		self.rows = _rows
		self.cols = _cols
	def Draw(self):
		for x in range(0, self.cols):
			for y in range(0, self.rows):
				AIE.DrawLine( self.cellSize * x, self.cellSize * y, (self.cellSize * x + self.cellSize) - 1, self.cellSize * y)
				AIE.DrawLine( self.cellSize * x, self.cellSize * y, self.cellSize * x, (self.cellSize * y - self.cellSize) - 1 )