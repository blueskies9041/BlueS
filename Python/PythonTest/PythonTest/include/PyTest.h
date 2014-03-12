#ifndef _PYTEST_H_
#define _PYTEST_H_

#include "Python.h"
#include <iostream>

using namespace std;

namespace Pyth
{

	extern PyMethodDef BLUE_Functions[]; //Function lookup table

	void ParsePyTupleError( const char* a_pFunction, int a_iLine ); // Outputs Python Errors to Console
	PyObject * ImportModule( const char* a_pModuleName ); // For loading in .py files (ex... "Game.py")
	PyObject * GetHandle( PyObject* a_pyModule, const char* a_pFunctionName ); //Retrieves the given function name from the given module, stores it in a PyObject * for use in CallFunction(...)
	PyObject * CallFunction( PyObject* a_pyFunction, PyObject* a_pyFuncArguments); //Calls the given python function with the supplied arguments

	//Python functions
	PyObject * BLUE_Sum(PyObject * self, PyObject * args);
	PyObject * BLUE_HelloWorld(PyObject * self, PyObject * args); //Test function, calls HelloWorld() from Utilities.h
	

};

#endif