import AIE
import Objects
from Objects import Sprite, Vec2, Cell, Pathfinder #Class Names
from Objects import Background, Player, Enemy, Obstacle, AStar, Dot #Instances of classes
import pdb
import copy

######################	

#DONT FORGET THE FUCKING  " : " ON LIKE. EVERYTHING

def PlayerOffScreen():
	if(Player.pos.x > 1024. - (Player.width / 2) or Player.pos.x < 0 + (Player.width / 2) ):
		return True

xspd = 0

def UpdateGame():
	if(Player.active == False):
		Player.Activate()
		Player.name = "Player"
		Enemy.name = "Enemy"
		Obstacle.name = "Obstacle"
		Background.name = "Background"
		Player.vel.x = xspd
		print((Player.pos.x , Player.pos.y))
		print((Enemy.pos.x, Enemy.pos.y))
		print((Player.pos.Distance(Enemy.pos)))
		AStar.cells[1][4].passable = False
		AStar.cells[2][4].passable = False
		AStar.cells[3][4].passable = False
		AStar.Start( (2,2), (2,6))
		AStar.startCell.ConsoleDebug()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		AStar.FindPath()
		
		print AStar.currentCell.index.loc, AStar.currentCell.parent.index.loc, AStar.currentCell.parent.parent.index.loc, AStar.currentCell.parent.parent.parent.index.loc, 
		#for i in range (0, len(AStar.startCell.neighbors)):
			#AStar.startCell.neighbors[i].debug = True
			#AStar.startCell.neighbors[i].ConsoleDebug()
		#AStar.FindPath()
		#AStar.FindPath()
		#AStar.FindPath()
	AStar.FindPath()	
	AStar.Update()

	if(AStar.cells[1][4].ContainsSprite(Player)):
		AIE.DrawString("Success!", 512, 384)
	

	if(Enemy.active == False):
		Enemy.vel.x = .00

		
	if(PlayerOffScreen()):
		if(Player.vel.x > 0):
			Player.pos.x -= .01
		if(Player.vel.x < 0):
			Player.pos.x += .01
		Player.vel.x *= -1.0
	
	#GameGrid.Draw()
	
	Background.Update()
	Player.Update()
	Enemy.Update()
	Obstacle.Update()
	AStar.Update()
	Dot.Move()
	Dot.Draw()
	#TestCell.Draw()
	#AStar.Update()
		

	
	