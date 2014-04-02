#ifndef _PythonManager_H_
#define _PythonManager_H_

#include "Python.h"
#include <unordered_map>
#include <cstdarg>

class PythonManager
{
	public:

		inline static PythonManager &Instance()
		{
			static PythonManager oInstance;
			return oInstance;
		}

		void Initialize(char * a_pScriptDirectory);
		void Finalize();
		void ImportScript(char * a_pScriptName);
		void ReloadScript(char * a_pScriptName);
		void AddTable(char * a_pTableName, PyMethodDef  * a_pyFunctionTable);

		PyObject * GetFunction(char * a_pScriptName, char * a_pFunctionName);
		PyObject * CallFunction(PyObject * a_pyFunction, char * a_pFormat, ...); 
		/* 
		I use a variable argument list for CallFunction().
			-	If you want to pass variables to Python
				provide a format (ex "iff" for int, float, float) followed by
				the va_list arguments.

				Ex:
					<InterpreterName>.CallFunction( <FunctionID>, "iff", 1, 2.0f, 2.0f);

				-	Where <InterpreterName> is the name of the singleton PythonManager Object
					and <FunctionID> is a PyObject * retrieved from a script via GetFunction(...)
		*/

	private:

		std::unordered_map< char * , PyObject *> m_Scripts;

};

#endif