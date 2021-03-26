from PIL import ImageGrab
import win32gui
import numpy as np
import cv2
import os


def saveData(hwnd,dataPath,x=-1,y=-1,key=0,event=0):
    bbox = win32gui.GetWindowRect(hwnd) # (left, top, width,height) şeklinde veriyor.
    img = ImageGrab.grab(bbox)
    img = np.array(img)[:,:,:3]
    img = cv2.resize(img,(150,150))
    print('once-{0},{1},{2},{3}.png'.format(x, y, key, event))
    cv2.imwrite(dataPath+os.sep+'{0},{1},{2},{3}.png'.format(x,y,key,event),img)
    print('{0},{1},{2},{3}.png'.format(x,y,key,event))



