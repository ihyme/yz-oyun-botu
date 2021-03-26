from PIL import ImageGrab
import win32gui

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)
def siaScreen(gamename):
    try:
        pencere = [(hwnd, title) for hwnd, title in winlist if gamename.lower() in title.lower()]
        pencere = pencere[0]
        hwnd = pencere[0]
        win32gui.SetForegroundWindow(hwnd)
        bbox = win32gui.GetWindowRect(hwnd) # (left, top, width,height) şeklinde veriyor.
        img = ImageGrab.grab(bbox)
        img.show()
    except IndexError:
        pass
siaScreen('AirRivals_R')