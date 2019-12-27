from pyautogui import typewrite
from .apps import *

def workMode():
    # Start Firefox
    firefox()
    rambox()
    # Switch to workspace 3 and run terminal
    workspace(3)
    terminal()
    # Run Code
    vscode()

def musicMode():
    # Start Firefox
    firefox()
    # Start mpd and ncmpcpp
    workspace(4)
    terminal()
    write_enter('mpd')
    write_enter('ncmpcpp')