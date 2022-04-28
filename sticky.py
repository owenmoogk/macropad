from pynput import keyboard as k
import pyautogui

active = False  # if the sticky caps is active
case = True  # just alternates for caps and not, also useful for returning the status of caps is to what it was before being turned on
print('running sticky')

def onPress(key):
  global active, case

  with open(r'C:\Users\owenm\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\macropad\sticky.txt', "r") as f:
    active = f.readlines()[0] == "true"

  # once it is turned off we need to return to og caps state
  if not active and not case:
    case = not case
    pyautogui.press('capslock')

  # check if it is a letter key and active
  if (len(str(key)) == 3) and active:
    case = not case
    pyautogui.press('capslock')

def onRelease(key):
  pass

with k.Listener(on_press=onPress, on_release=onRelease) as listener:
  listener.join()
