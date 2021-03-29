import cv2
import numpy as np
from PIL import ImageGrab
import win32gui
import os
gameName = "AirRivals_R"
windows_list = []
toplist = []
def enum_win(hwnd, result):
    win_text = win32gui.GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))
win32gui.EnumWindows(enum_win, toplist)

def gameScreen(path,x=-1,y=-1,action=0,key=0):
    game_hwnd = 0
    for (hwnd, win_text) in windows_list:
        if gameName in win_text:
            game_hwnd = hwnd
    if game_hwnd == 0:
        print("Oyun Açık Değil")
        return False
    print(str(win32gui.GetForegroundWindow())+" ---- "+str(game_hwnd))
    if win32gui.GetForegroundWindow() == game_hwnd:
        position = win32gui.GetWindowRect(game_hwnd)
        screenshot = ImageGrab.grab(position)
        screenshot = np.array(screenshot)
        screenshot = cv2.resize(screenshot, (150, 150))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        path = os.path.join(path,str(x)+","+str(y)+","+str(action)+","+str(key))
        cv2.imwrite(path+".png",screenshot)
    return