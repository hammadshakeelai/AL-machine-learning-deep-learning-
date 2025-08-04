import win32api, win32con
import time

time.sleep(1)  # Wait for the system to stabilize
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)  # Press the Windows keyj