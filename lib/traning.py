from PIL import ImageGrab
import win32gui
import numpy as np
import cv2
import os

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)
def saveData(gamename,dataPath,x=-1,y=-1,key=0,event=0):
    try:
        pencere = [(hwnd, title) for hwnd, title in winlist if gamename.lower() in title.lower()]
        pencere = pencere[0]
        hwnd = pencere[0]
        #win32gui.SetForegroundWindow(hwnd)
        if win32gui.GetForegroundWindow()==hwnd:
            bbox = win32gui.GetWindowRect(hwnd) # (left, top, width,height) şeklinde veriyor.
            img = ImageGrab.grab(bbox)
            img = np.array(img)[:,:,:3]
            img = cv2.resize(img,(150,150))
            cv2.imwrite(os.path.join(dataPath,'{0},{1},{2},{3}.png'.format(x,y,key,event)),img)
            print(os.path.join(dataPath,'{0},{1},{2},{3}.png'.format(x,y,key,event)))
           # img.show() resmi göster
    except IndexError:
        print("\rOyun Açık Değil",end="")

saveData('AirRivals_R','./')