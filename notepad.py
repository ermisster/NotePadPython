import pyautogui
import time

pyautogui.press("winleft")
time.sleep(0.5)
pyautogui.write("notepad")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.write("you got hacked")
time.sleep(0.5)
pyautogui.hotkey("alt","f4")
