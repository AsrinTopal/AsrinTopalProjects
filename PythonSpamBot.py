import pyautogui
import time 
time.sleep(3)
for i in range(10):
    pyautogui.typewrite("hey")
    pyautogui.press("enter")
    