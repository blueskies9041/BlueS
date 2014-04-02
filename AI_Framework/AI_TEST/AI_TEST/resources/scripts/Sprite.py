## Sprite Class ##
import AIE
import Vec2
from Vec2 import Vec2

class Sprite:
	def __init__( self, _texPath, _width, _height, _pos):
		self.texPath = _texPath
		self.name = "Default"
		self.width = _width
		self.height = _height
		self.pos = _pos
		self.vel = Vec2(0.0 , 0.0)
		self.ID = AIE.CreateSprite(_texPath, _width, _height) # 0 for False 
		self.active = False
		print(self.texPath, self.width, self.height, (self.pos.x, self.pos.y), self.ID)
	def Dimensions(self):
		return (self.width, self.height)
	def TopLeft(self):
		return Vec2(self.pos.x - (self.width / 2), self.pos.y - (self.height / 2 ))
	def Activate(self):
		self.active = True
	def Move(self):
		self.pos.x += self.vel.x
		AIE.MoveSprite(self.ID, self.pos.x, self.pos.y)
	def Draw(self):
		AIE.DrawSprite(self.ID)
	def Debug(self):
		AIE.DrawString(self.name, int(self.TopLeft().x), int(self.TopLeft().y))
		AIE.DrawString(str((int(self.pos.x), int(self.pos.y))), int(self.TopLeft().x), int(self.TopLeft().y + 25))
		AIE.DrawString(str(((self.vel.x),(self.vel.y))), int(self.TopLeft().x), int(self.TopLeft().y + 50))
	def Update(self):
		self.Debug()
		self.Move()
		self.Draw()