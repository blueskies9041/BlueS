//////////////////////////////////////////////////////////////////////////
// #INCLUDES
#include <string>
#include <cmath>
#include <time.h>
#include <assert.h>
#include <crtdbg.h>
#include <iostream>
#include "AIE/AIE.h"
#include "AIE/AIE_Py.h"
#include "Python/PythonManager.h"
#include "BlueS/Sprite.h"
#include "BlueS/Vec2.h"

int main( int argc, char* argv[] )
{	
	//Framework Init
	Initialise(1024, 768);

	//Python Interpreter Initialization
	PythonManager Slither = PythonManager::Instance();

	Slither.Initialize("./scripts");
	Slither.AddTable("AIE", AIE_Functions);
	Slither.ImportScript("BlueS");

	//Game Update Function
	PyObject * PyFunc_UpdateGame = Slither.GetFunction("BlueS", "UpdateGame");
	
	do 
	{
		Slither.ReloadScript("BlueS");
		PyFunc_UpdateGame = Slither.GetFunction("BlueS", "UpdateGame");
		Slither.CallFunction(PyFunc_UpdateGame, NULL);

	} while ( FrameworkUpdate() == false );
	
	Slither.Finalize();
	Shutdown();

	return 0;
}

