from pynput import mouse,keyboard
import os
from lib.traning import saveData
gameName = 'AirRivals_R'
def klavyeDinle():
   dataPath = 'Data\\Train\\Klavye'
   if not os.path.exists(dataPath):
      os.makedirs(dataPath)
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
   dataPath = 'Data\\Train\\Fare'
   if not os.path.exists(dataPath):
      os.makedirs(dataPath)
   def on_move(x, y):
      saveData(gameName,dataPath,x=x,y=y,key=0,event=0)
      print('Pointer moved to {0}'.format((x, y)))

   def on_click(x, y, button, pressed):
      saveData(gameName,dataPath,x=x,y=y,key=1 if pressed else 0,event=0)
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