@echo off
setlocal
REM Build T-Rex Win32 with MinGW (g++)
REM Requires: g++ in PATH
g++ trex_win32.cpp -municode -lgdi32 -o trex_win32.exe
if %errorlevel% neq 0 (
  echo Build failed.
  exit /b %errorlevel%
)
echo.
echo Built trex_win32.exe
echo Run: trex_win32.exe
