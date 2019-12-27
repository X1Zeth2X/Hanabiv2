from pyautogui import press, typewrite, hotkey

# Run an application using dmenu rofi.
def run(app_name):
    press('altright')
    typewrite(app_name)
    press('enter')

def workspace(num):
    hotkey('winleft', str(num))

# Command must be a string
def write_enter(command):
    typewrite(command)
    press('enter')

# Define applications here
def terminal():
    hotkey('winleft', 'enter')

def firefox():
    run('Firefox')

def rambox():
    run('rambox')

def vscode():
    run('VSCodium')
