import AIE

x = 500.
y = 250.

def UpdatePlayer():
	AIE.MoveSprite(1,x,y); #hard coded in Player's Sprite ID (1)
	AIE.DrawSprite(1)
	return (x,y)


def UpdateBackground(a, b, c): #takes values passed in from C++ , can't modify during run time
	AIE.MoveSprite(a, b, c);
	AIE.DrawSprite(a);




