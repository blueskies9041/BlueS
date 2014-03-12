#include "PyTest.h"
#include "Utilities.h"

//Python Test Project

int main(int argc, char *argv[])
{
	/* PYTHON SETUP */
	Py_Initialize(); 
	PySys_SetArgv(argc, argv);
	PyObject * pySysPath = PySys_GetObject((char*)"path");
	PyList_Append(pySysPath, PyString_FromString("resources/scripts")); // script directory to pythons directory list for this program

	/* TESTING */

	//Module Stuff
	Py_InitModule("BLUE", Pyth::BLUE_Functions); // exports the function lookup table from PyTest.cpp to Python (import BLUE to include it in a .py file)
	PyObject * pyModule = Pyth::ImportModule("Test"); //Allows me to extract functions from Test.py in .../scripts
	
	PyObject * pyTestHandle = Pyth::GetHandle( pyModule, "Hey"); //Searches Test.py for a function named "Hey", stores the name.
	PyObject * pyTestHandleB = Pyth::GetHandle( pyModule, "Math"); 
	PyObject * pyTestHandleC = Pyth::GetHandle( pyModule, "MoreMath"); 

	/* Making an argument list to pass to CallFunction( handle, (...) ) */
		PyObject * pyA = PyInt_FromLong(1);
		PyObject * pyB = PyInt_FromLong(3);

		PyObject * pyArgs = PyTuple_New(2);
		PyTuple_SetItem(pyArgs, 0, pyA);
		PyTuple_SetItem(pyArgs, 1, pyB);

	Pyth::CallFunction(pyTestHandle, 0); //HELLO WORLD :D
	Pyth::CallFunction(pyTestHandleB, pyArgs);
	std::cout << endl;
	Pyth::CallFunction(pyTestHandleC, 0);

	cin.get();
	return 0;
}