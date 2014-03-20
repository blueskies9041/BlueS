#include "PythonInterpreter.h"
#include <iostream>

void PythonInterpreter::Initialize(char * a_pScriptDirectory)
{
	Py_Initialize(); 
	PyObject * pySysPath = PySys_GetObject((char*)"path");
	PyList_Append(pySysPath, PyString_FromString(a_pScriptDirectory)); 
}

void PythonInterpreter::Finalize()
{
	//maybe delete member maps
	Py_Finalize();
}

void PythonInterpreter::ImportScript(char * a_pScriptName)
{
	PyObject * pyScriptName = PyString_FromString(a_pScriptName);
	PyObject * pyScript = PyImport_Import(pyScriptName);

	if(!pyScript)
	{
		PyErr_Print();
		std::cout << stderr << "Cannot find function \"" << a_pScriptName << "\"" << std::endl;
	}

	m_Scripts[a_pScriptName] = pyScript;
}

void PythonInterpreter::ReloadScript(char * a_pScriptName)
{
	m_Scripts[a_pScriptName] = PyImport_ReloadModule(m_Scripts[a_pScriptName]);
}

void PythonInterpreter::AddTable(char * a_pTableName, PyMethodDef * a_pyFunctionTable) 
{
	Py_InitModule(a_pTableName , a_pyFunctionTable ); 
}

PyObject * PythonInterpreter::GetFunction(char * a_pScriptName, char * a_pFunctionName)
{
	PyObject * pyFunction = PyObject_GetAttrString( m_Scripts[a_pScriptName], a_pFunctionName);

	if( !(pyFunction && PyCallable_Check(pyFunction)) ) 
	{
        if (PyErr_Occurred())
        {
			PyErr_Print();
		}
        std::cout << stderr << "Cannot find function \"" << a_pFunctionName << "\"" << std::endl;
    }
	return pyFunction;
}

PyObject * PythonInterpreter::CallFunction(PyObject * a_pyFunction, char * a_pFormat, ...)
{
	if(a_pFormat == NULL)
	{
		PyObject * pyReturn = PyObject_CallObject( a_pyFunction, 0);
		if (pyReturn == nullptr)
		{
			PyErr_Print();
			fprintf(stderr,"Call failed\n");
		}
		return pyReturn;
	}

	else
	{
		va_list args;
		va_start(args, a_pFormat );

		PyObject * pyArgs = Py_VaBuildValue( a_pFormat, args);

		va_end(args);

		PyObject * pyReturn = PyObject_CallObject( a_pyFunction, pyArgs);

		if (pyReturn == nullptr)
		{
			PyErr_Print();
			fprintf(stderr,"Call failed\n");
		}
		return pyReturn;
	}

	
}


