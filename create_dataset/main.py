
import os,time
import cv2
from common import gameScreen
from pynput import mouse,keyboard
import keyboard as kb
fareEgitimYolu = os.path.join("..","Egitim","Veriler","Fare")
klavyeEgitimYolu = os.path.join("..","Egitim","Veriler","Klavye")
if not os.path.exists(fareEgitimYolu):
  os.makedirs(fareEgitimYolu)
if not os.path.exists(klavyeEgitimYolu):
  os.makedirs(klavyeEgitimYolu)
gameName = "AirRivals_R" # buradaki oyun adını değiştirmeniz gerekmektedir.

#Fare İşlemleri

from pynput import mouse

def on_move(x, y):

    gameScreen(fareEgitimYolu,x,y)


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
cv2.waitKey(30000)