import AIE
import Vec2
from Vec2 import Vec2
import Sprite
from Sprite import Sprite
import Cell
from Cell import Cell
import Pathfinder
from Pathfinder import Pathfinder
import math
from math import sqrt, pow

#Class Instances

AStar 		= Pathfinder(100., 12, 12)
Background 	= Sprite("./images/bg.png"			, 1024, 768, Vec2(512.0, 384.0))
Player 		= Sprite("./images/crate_sideup.png", 100 , 100, AStar.cells[2][1].pos)
Enemy		= Sprite("./images/crate_sideup.png", 100 , 100, AStar.cells[2][7].pos)
Obstacle 	= Sprite("./images/crate_sideup.png", 100 , 300, AStar.cells[2][5].pos)

