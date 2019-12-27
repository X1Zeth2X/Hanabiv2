# Import our starters
from sys import argv, exit
from modules.modes import *
from pyautogui import alert, press

def notify(mode):
    alert(f'Hanabi ~> Setting up { mode } mode, please wait...', title='Hanabi v3', timeout=3*1000)

def done():
    alert('Hanabi ~> Completed!')

if __name__ == '__main__':
    # Get arguments
    if len(argv) != 2:
        exit('Please pass a valid argument.')

    param = argv[1].lower()
    if param == 'work':
        notify(param)
        workMode()
        done()

    elif param == 'chill':
        notify(param)
        musicMode()
        done()