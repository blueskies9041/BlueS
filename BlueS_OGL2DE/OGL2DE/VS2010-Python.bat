@echo off
REM set PYTHON33_INCLUDE="C:\Python33\include"
REM set PYTHON33_LIB="C:\Python33\libs\python33.lib"

REM set PYTHON27_INCLUDE="C:\Python27\include"
REM set PYTHON27_LIB="C:\Python27\python27.lib"

REM Add PYTHONPATH to env vars
set PYTHONPATH=%PYTHONPATH%;C:\Python27

REM Append PYTHONPATH to existing PATH var
set PATH=%PATH%;%PYTHONPATH%

python -V

"C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE\devenv.exe"