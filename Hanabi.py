# Import our starters
from sys import argv, exit
from modules.modes import *
from pyautogui import alert, press, prompt

def notify(mode):
    alert(f'Hanabi ~> Setting up { mode } mode, please wait...', title='Hanabi v3', timeout=3*1000)

def done():
    alert('Hanabi ~> Completed!')
    exit('Completed task.')

if __name__ == '__main__':
    # Get arguments
    command = prompt('Hanabi ~> Please enter a mode.').lower()
    if not command:
        alert('Hanabi ~> No command passed, exiting!')
        exit(0)

    elif command == 'work':
        notify(command)
        workMode()
        done()

    elif command == 'chill':
        notify(command)
        musicMode()
        done()

    alert('Hanabi ~> Mode not found!')