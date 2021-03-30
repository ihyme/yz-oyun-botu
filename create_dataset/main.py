
import os,time
from threading import Thread
import cv2
from common import gameScreenVT,gameScreenTPL
from pynput import mouse,keyboard
import keyboard as kb
"""
#data diske yazilirsa
fareEgitimYolu = os.path.join("..","Egitim","Veriler","Fare")
klavyeEgitimYolu = os.path.join("..","Egitim","Veriler","Klavye")
if not os.path.exists(fareEgitimYolu):
  os.makedirs(fareEgitimYolu)
if not os.path.exists(klavyeEgitimYolu):
  os.makedirs(klavyeEgitimYolu)
"""
gameName = "AirRivals_R" # buradaki oyun adını değiştirmeniz gerekmektedir.

#Fare İşlemleri
def on_move(x, y):
  gameScreenTPL(x,y)

    

def on_click(x, y, button, pressed):
    """
      x: x Koordinatı
      y: y Koordinati
      action: 0=not action,1=pressed,2=released
      key: 0=not key-left-right
    """
    action = 1 if pressed else 2
    key = 'left' if button==button.left else 'right'
    th = Thread(target=gameScreenVT,args=(gameName, x, y, action, key))
    th.start()

def on_scroll(x, y, dx, dy):
      
    pass
listenerF = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listenerF.start()

##Klavye ayarları
def on_press(key):
    tus = str(key).strip("'") if len(str(key).strip("'"))<4 else str(key)[4:]
    print("basilan : "+tus)
    gameScreenVT(gameName, "-1", "-1", "1", tus)

def on_release(key):
      
     tus = str(key).strip("'") if len(str(key).strip("'"))<4 else str(key)[4:]
     print("Bırakılan : "+tus)
     gameScreenVT(gameName, "-1", "-1", "2", tus)
   



# ...or, in a non-blocking fashion:
listenerK = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
#listenerK.start()






cv2.waitKey(20*1000)