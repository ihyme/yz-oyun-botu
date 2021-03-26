from pynput import mouse,keyboard
import os
import win32gui
from lib.traning import saveData
gameName = 'AirRivals_R'
farePath = os.path.join("Data","Train","Fare")
klavyePath = os.path.join("Data","Train","Klavye")

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)
pencere = [(hwnd, title) for hwnd, title in winlist if gameName.lower() in title.lower()]
pencere = pencere[0]
hwnd = pencere[0]


def klavyeDinle():
   if not os.path.exists(klavyePath):
      os.makedirs(klavyePath)
   def on_press(key):
      try:
         print('alphanumeric key {0} pressed'.format(key.char))
      except AttributeError:
         print('special key {0} pressed'.format(key))
   def on_release(key):
      print('{0} released'.format(key))

   listener = keyboard.Listener(on_press=on_press,on_release=on_release)
   listener.start()


def fareDinle():
   if not os.path.exists(farePath):
      os.makedirs(farePath)
   def on_move(x, y):
      saveData(hwnd,farePath,x=x,y=y,key=0,event=0)
      print('Pointer moved to {0}'.format((x, y)))

   def on_click(x, y, button, pressed):
      if win32gui.GetForegroundWindow() == hwnd:
         saveData(hwnd,farePath,x=x,y=y,key=1 if pressed else 0,event=0)
      print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

   def on_scroll(x, y, dx, dy):
      print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

   listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
   listener.start()


def main():
   print("Training Başlıyor")
   fareDinle()
   klavyeDinle()

   while 1:
      pass



if __name__ == '__main__':
   main()