//////////////////////////////////////////////////////////////////////////
#include <string>
#include <cmath>
#include <time.h>
#include <assert.h>
#include <crtdbg.h>
#include <iostream>
#include "AIE.h"
#include "AIE_Py.h"
#include "PythonInterpreter.h"

struct Sprite
{
	unsigned int m_uiSpriteID;
	char * m_pTexturePath;
	int m_iWidth;
	int m_iHeight;

	unsigned int ID() { return m_uiSpriteID; }

	Sprite(char * a_pTexturePath, int a_iWidth, int a_iHeight)
		:	m_pTexturePath(a_pTexturePath), 
			m_iWidth(a_iWidth),
			m_iHeight(a_iHeight),
			m_uiSpriteID( CreateSprite(a_pTexturePath, a_iWidth, a_iHeight))
	{ }
};

int main( int argc, char* argv[] )
{	
	//Framework Init
	Initialise(1024, 768);

	//Sprite Init
	Sprite BG("./images/bg.png", 1024, 768);
		MoveSprite(BG.ID(), 512, 384);
	Sprite Player("./images/crate_sideup.png", 100, 100);


	//Sprite Player(

	//Python Interpreter Initialization
	PythonInterpreter Slither = PythonInterpreter::Instance();

	Slither.Initialize("./scripts");
	Slither.AddTable("AIE", AIE_Functions);
	Slither.ImportScript("Game");

	//Python Functions
	PyObject * DrawPlayerFunctionID = Slither.GetFunction("Game", "UpdatePlayer");
	PyObject * DrawBGFunctionID = Slither.GetFunction("Game", "UpdateBackground");
	
	static float fTimer = 0.f;

	do 
	{
		fTimer++;

		Slither.ReloadScript("Game");
		Slither.CallFunction(DrawBGFunctionID, "iff", 0, 512.f /*+ fTimer*/, 384.f);
		Slither.CallFunction(DrawPlayerFunctionID, NULL);

		if(IsKeyDown(KEY_ESC))
			break;

	} while ( FrameworkUpdate() == false );
	
	Slither.Finalize();
	Shutdown();

	return 0;
}

