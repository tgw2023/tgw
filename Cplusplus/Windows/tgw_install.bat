@echo off & setlocal enabledelayedexpansion
set TGW_PACK_PATH=%~dp0
set TGW_CRT_PATH=%SystemDrive%\Users\Public\Documents\mdga_file
set TGW_LIB_PATH=%SystemDrive%\Users\Public\Documents\mdga_file\lib
if not exist %TGW_CRT_PATH% mkdir %TGW_CRT_PATH%
if not exist %TGW_LIB_PATH% mkdir %TGW_LIB_PATH%
if exist %TGW_CRT_PATH%\.ca.crt del %TGW_CRT_PATH%\.ca.crt /q
xcopy %TGW_PACK_PATH%c++\lib\.ca.crt %TGW_CRT_PATH%
del %TGW_LIB_PATH%\* /q
xcopy %TGW_PACK_PATH%c++\lib\* %TGW_LIB_PATH%
echo cat %path%|find /C "mdga_file\lib"
if %errorlevel% neq 0 (
    setx Path "%path%;%TGW_LIB_PATH%"
	echo success
) else (
echo success
)
pause
