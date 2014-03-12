#include "PyTest.h"
#include "Utilities.h"

#define __func__ __FUNCTION__

namespace Pyth
{

	PyMethodDef BLUE_Functions[] = 
	{
		{"HelloWorld", BLUE_HelloWorld, METH_VARARGS, "Prints out a message."},
		{"Sum", BLUE_Sum, METH_VARARGS, "Prints out sum of two numbers & returns it."},
		{NULL, NULL, 0, NULL}
	};

	void ParsePyTupleError( const char* a_pFunction, int a_iLine )
	{
		std::cout << "___Error Parsing Tuple___\nFunction: " <<  a_pFunction << "\nLine#   : " << a_iLine << std::endl;
		PyErr_Print();
	}

	PyObject * ImportModule( const char* a_pModuleName )
	{
		PyObject * pyObjName = PyString_FromString(a_pModuleName); //Get name of the module (.py) & store it
		PyObject * pyModule = PyImport_Import(pyObjName); //Import the module & store it

		if(!pyModule) //error checking...
		{
			PyErr_Print();
			std::cout << stderr << "Failed to load\" " << a_pModuleName << "\"" << std::endl;
		}

		Py_DECREF(pyObjName); //Reference decrement
		return pyModule; 
	}

	PyObject * GetHandle( PyObject* a_pyModule, const char* a_pFunctionName )
	{
		PyObject * pyFunction = PyObject_GetAttrString(a_pyModule, a_pFunctionName); //Retrieve function name from imported module

		if(!(pyFunction && PyCallable_Check(pyFunction))) //Error checking...
		{
			if(PyErr_Occurred())
			{
				PyErr_Print();
			}
		std::cout << stderr << "Cannot find function \"" << a_pFunctionName << "\"" << std::endl;
		}

		return pyFunction;
    }

	PyObject * CallFunction( PyObject* a_pyFunction, PyObject* a_pyArguments)
	{
		PyObject * pyReturnValue = PyObject_CallObject(a_pyFunction, a_pyArguments);
		if(pyReturnValue == NULL)
		{
			PyErr_Print();
			std::cout << stderr << "Call failed!\n" ;
		}

		return pyReturnValue;
	}

	PyObject * BLUE_HelloWorld(PyObject * self, PyObject * args)
	{
		Blue::HelloWorld();
		Py_RETURN_NONE;
	}

	
	PyObject * BLUE_Sum(PyObject * self, PyObject * args)
	{
		int x, y;
		if(!PyArg_ParseTuple(args, "ii", &x, &y))
		{
			ParsePyTupleError( __func__ , __LINE__ );
			return nullptr;
		}
		int result = Blue::Sum(x, y);
		Py_BuildValue("i", result);
	}

}