#include "Python.h"

extern PyMethodDef BLUE_Functions[]; //Python function lookup table
void ParsePyTupleError( const char * a_pFunction, int a_iLine );
PyObject * ImportModule( const char * a_pModuleName );
PyObject * GetHandle( PyObject * a_pyModule, const char * a_pFunctionName );
PyObject * CallFunction( PyObject * a_pyFunction, PyObject * a_pyFuncArguments );

/*
	Notes


*/