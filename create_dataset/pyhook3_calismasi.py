
import PyHook3
import os,sys
from common import gameScreen
import pythoncom
hm = PyHook3.HookManager()

fareEgitimYolu = os.path.join("..","Egitim","Veriler","Fare")
klavyeEgitimYolu = os.path.join("..","Egitim","Veriler","Klavye")
if not os.path.exists(fareEgitimYolu):
  os.makedirs(fareEgitimYolu)
if not os.path.exists(klavyeEgitimYolu):
  os.makedirs(klavyeEgitimYolu)
gameName = "AirRivals_R" # buradaki oyun adını değiştirmeniz gerekmektedir.


def OnMouseEvent(event):
  print('MessageName:',event.MessageName)
  print('Message:',event.Message)
  print('Time:',event.Time)
  print('Window:',event.Window)
  print('WindowName:',event.WindowName)
  print('Position:',event.Position)
  print('Wheel:',event.Wheel)
  print('Injected:',event.Injected)
  print('---')
  action = 1 if event.MessageName == "mouse left down" else 2

  if event.WindowName == gameName:
    gameScreen(fareEgitimYolu,str(event.Position[0]),str(event.Position[1]),1,action)
    gameScreen(fareEgitimYolu,str(event.Position[0]),str(event.Position[1]),0,action)
  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True

def OnKeyboardEvent(event):
  print('MessageName:',event.MessageName)
  print('Message:',event.Message)
  print('Time:',event.Time)
  print('Window:',event.Window)
  print('WindowName:',event.WindowName)
  print('Ascii:', event.Ascii, chr(event.Ascii))
  print('Key:', event.Key)
  print('KeyID:', event.KeyID)
  print('ScanCode:', event.ScanCode)
  print('Extended:', event.Extended)
  print('Injected:', event.Injected)
  print('Alt', event.Alt)
  print('Transition', event.Transition)
  print('---')
  if event.Key == "Q":
    sys.exit()
    return False
  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True

# create the hook mananger

# register two callbacks
hm.MouseAllButtonsDown = OnMouseEvent
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookMouse()
hm.HookKeyboard()

if __name__ == '__main__':

  pythoncom.PumpMessages()
