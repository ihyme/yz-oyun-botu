import cv2
import datetime as zmn
import numpy as np
import pyautogui as py
from PIL import ImageGrab
import win32gui
import os
import base64,mysql.connector
gameName = "AirRivals_R"
windows_list = []
toplist = []
datasets = []
def enum_win(hwnd, result):
    win_text = win32gui.GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))
win32gui.EnumWindows(enum_win, toplist)

def gameScreenVT(path=None,x=-1,y=-1,action=0,key=0):
    db = mysql.connector.connect(  host="localhost",
                                  user="root",
                                  password="",
                                  database="datasets"
                                     )
    cursor = db.cursor()
   # position = py.screenshot()
    screenshot = py.screenshot() # ImageGrab.grab(position)
    screenshot = np.array(screenshot)
    screenshot = cv2.resize(screenshot, (150, 150))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    etiket = str(x)+","+str(y)+","+str(action)+","+str(key)
    retval,buffImg = cv2.imencode('.jpg',screenshot)
    bs64rsm = base64.b64encode(buffImg)
    bs64rsm = bs64rsm.decode('utf-8')
    cursor.execute("INSERT INTO datasets VALUES(id,%s,%s)" ,(bs64rsm,etiket))
    db.commit()
    return


def gameScreenTPL(path=None, x=-1, y=-1, action=0, key=0):
    print('\r',end='')
    game_hwnd = 0
    for (hwnd, win_text) in windows_list:
        if gameName in win_text:
            game_hwnd = hwnd
    if game_hwnd == 0:
        print("Oyun Açık Değil")
        return False

    if win32gui.GetForegroundWindow() == game_hwnd:
        position = win32gui.GetWindowRect(game_hwnd)
        screenshot = ImageGrab.grab(position)
        screenshot = np.array(screenshot)
        screenshot = cv2.resize(screenshot, (150, 150))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        etiket = str(x) + "," + str(y) + "," + str(action) + "," + str(key)
        retval, buffImg = cv2.imencode('.jpg', screenshot)
        bs64rsm = base64.b64encode(buffImg)
        bs64rsm = bs64rsm.decode('utf-8')
        datasets.append((bs64rsm,etiket))
        print('\rBiriktirilen Dataset Sayısı : '+str(len(datasets)),end='')
    else:
        if len(datasets) > 1 :
            db = mysql.connector.connect(  host="localhost",
                                  user="root",
                                  password="",
                                  database="datasets"
                                     )
            cursor = db.cursor()
            bs64rsm,etiket = datasets[0]
            cursor.execute("INSERT INTO datasets VALUES(id,%s,%s)" ,(bs64rsm,etiket))
            db.commit()
            datasets.pop(0)
            print('\rDatabase İşlenmeyi Bekleyin : '+str(len(datasets)),end='')

    return



def gameScreen(path,x=-1,y=-1,action=0,key=0):
    game_hwnd = 0
    for (hwnd, win_text) in windows_list:
        if gameName in win_text:
            game_hwnd = hwnd
    if game_hwnd == 0:
        print("Oyun Açık Değil")
        return False
    
    if win32gui.GetForegroundWindow() == game_hwnd:
        position = win32gui.GetWindowRect(game_hwnd)
        screenshot = ImageGrab.grab(position)
        screenshot = np.array(screenshot)
        screenshot = cv2.resize(screenshot, (150, 150))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        ek = "-"+str(zmn.datetime.now().timestamp())
        path = os.path.join(path,str(x)+","+str(y)+","+str(action)+","+str(key))
        
        cv2.imwrite(path+ek+".png",screenshot)
    return