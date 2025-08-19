T-Rex Win32 (C++/GDI)
------------------------
Build options:

1) Visual Studio (Windows Desktop App - Empty Project)
   - Add trex_win32.cpp
   - Ensure Gdi32 is linked (usually automatic)
   - Build and run

2) MinGW:
   - Double-click build_mingw.bat (or run in terminal)
   - Produces trex_win32.exe

Controls:
  SPACE/UP/Left-Click: Jump
  DOWN: Duck
  R: Restart
  ESC: Quit

Saves:
  trex_highscore.dat  (best score)
  trex_top5.txt       (top-5 scores)
  trex_runs.log       (timestamped runs)
