#!/usr/bin/env python3

""" Import Stuff """
import os, sys
import time
import subprocess
import yaml

## Colors Definitions ##
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

config = 'conf.yml'

####
def heading():
    spaces = " " * 50
    sys.stdout.write(GREEN + spaces + """

           ██  ██ ▄████▄ ███  ██ ▄████▄ █████  ██
           ██  ██ ██  ██ ████ ██ ██  ██ ██▄▄██ ██
           ██████ ██████ ██ ████ ██████ ██  ██ ██
           ██  ██ ██  ██ ██   ██ ██  ██ █████  ██

  """ + END + BLUE +
 '\n' + '{}A Simple CLI Assistant! Made for i3(wm/gaps)({}HANABI{}){}'.format(YELLOW, RED, YELLOW, BLUE).center(80) +
 '\n' + 'Version:{}2{} \n'.format(YELLOW, END).center(68))
####

####
def loadConfig():
    """ Loads the configuration """
    with open(config, 'r') as f:
        conf = yaml.load(f)
        f.close()
    return conf
####

####
def tildes():
    print("\t~~~~~~~~~~~~~~")

def equals():
    print("\t==============")
####

####
def quitHanabi():
    print("\t~~~~~~~~~~~~~~")
    print("\t{}* Quitting *{}".format(RED, WHITE))
    print("\t=-=-=-=-=-=-=-")
    time.sleep(1)
    quit()
####

####
def firstStart():
    print("\n\tHi I'm {}Hanabi{} A simple CLI assistant".format(RED,WHITE))
    time.sleep(2)
    print("\t{}Hanabi:{} This seems to be your first run".format(RED, WHITE))
    time.sleep(2)
    print("\t{}Hanabi:{} Let's do a quick setup! :D".format(RED, WHITE))
    time.sleep(2)
####

####
def CLIStarter():
    disown = " & disown"
    terminal = (conf["terminal"]) + ' '
    command = str(input("What is the name of the CLI Application?\nName (Case Sensitive): "))
    workspace = "i3 workspace"+ str(input("Choose a workspace\nWorkspace > ")) + " &&"
    os.system(workspace + terminal + command + disown)
def AppImageStarter():
    disown = " & disown"
    location = str(input("Where is the AppImage located?\nFull Location (Case Sensitive): "))
    name = str(input("What is the name of the AppImage Application?\nName (Case Sensitive): ")) + ".AppImage"
    workspace = "i3 workspace"+ str(input("Choose a workspace\nWorkspace > ")) + " &&"
    os.chdir(location)
    os.system(workspace + "./" + name + disown)
####

####
def launchImage(choice):
    disown = " & disown"
    location = conf["appimage"][choice]["location"]
    name = conf["appimage"][choice]["name"] + ".AppImage"
    workspace = "i3 workspace" +' '+(conf["appimage"][choice]["workspace"]) + " &&"
    os.chdir(location)
    os.system(workspace + "./" + name + disown)
####

####
def launch(choice):
    disown = " & disown"
    nohup = " & nohup"
    terminal = (conf["terminal"]) + ' '
    command = conf["apps"][choice]["command"]
    workspace = "i3 workspace"+' '+(conf["apps"][choice]["workspace"]) + " &&"
    return_ws = "i3 workspace "+ (conf["hanabi"]["mainworkspace"])

    ###     ###     ###     ###     ###     ###
    if conf["apps"][choice]["type"] == "cli":
        os.system(workspace + terminal + command + disown)
        time.sleep(2)
        os.system(return_ws)
    elif conf["apps"][choice]["type"] == "gui":
        os.system(workspace + "exec " + command + nohup)
        time.sleep(4)
        os.system(return_ws)
    ###     ###     ###     ###     ###     ###
####

def startApp():
    for app in sorted(conf["apps"]):
        """ [{}{app}{}] """
        print("\t{}[{}{}{}]{} To start {}".format(YELLOW, RED, app, YELLOW, WHITE, conf["apps"][app]['name']))
    for appimage in sorted(conf["appimage"]):
        print("\n")
        """ [{}{appimage}{}] """
        print("\t{}[{}{}{}]{} To start {} AppImage".format(YELLOW, RED, appimage, YELLOW, WHITE, conf["appimage"][appimage]['name']))

def List():
    while True:
        time.sleep(0.2)
        os.system("clear")
        heading()
        print('\n')
        time.sleep(fancydelay)
        startApp()
        time.sleep(fancydelay)
        print("\n\t{}[{}CLI{}]{} To start a custom CLI application".format(YELLOW, BLUE, YELLOW, WHITE))
        time.sleep(fancydelay)
        print("\t{}[{}AIM{}]{} To start a custom AppImage application".format(YELLOW, BLUE, YELLOW, WHITE))
        time.sleep(fancydelay)
        print("\n\t{}[{}Menu{}]{} to return to Main menu.".format(YELLOW, RED, YELLOW, WHITE))
        time.sleep(fancydelay)
        print("\t{}[{}Quit{}]{} to quit Hanabi.\n".format(YELLOW, RED, YELLOW, WHITE))
        choice = input("\tHanabi > ")
        if choice == "Menu":
            menu()
            break
        elif choice == "Quit":
            quitHanabi()
        elif choice in conf["apps"]:
            launch(choice)
        elif choice in conf["appimage"]:
            launchImage(choice)
        elif choice == "CLI":
            CLIStarter()
        elif choice == "AIM":
            AppImageStarter()
        else:
            print("Please choose a valid option")

####    ####    ####    ####

#######
def menu():
    os.system("clear")
    heading()
    time.sleep(fancydelay)
    print("\n\t{}Options:\n\t========".format(GREEN))
    time.sleep(fancydelay)
    print("\t{}[{}List{}]{} List applications to start".format(YELLOW, RED, YELLOW, WHITE))
    time.sleep(fancydelay)
    print("\t{}[{}Quit{}]{} Quit Hanabi".format(YELLOW, RED, YELLOW, WHITE))
    time.sleep(fancydelay)
#    Adding soon.
#    print("\t{}[{}Help{}]{} Guide and help on how to use the application".format(YELLOW, RED, YELLOW, WHITE))
#    time.sleep(fancydelay)
    print("\t{}[{}Settings{}]{} Change settings for Hanabi\n".format(YELLOW, RED, YELLOW, WHITE))
    time.sleep(fancydelay)
    while True:
        menu_choice = str(input("\tHanabi > "))
        if menu_choice == "List":
            List()
        elif menu_choice == "Settings":
            Settings()
        elif menu_choice == "Quit":
            quitHanabi()
        else:
            tildes()
            print("Please choose a valid option!")
            time.sleep(1)
            menu()
#######


#######
def Settings():
    os.system("clear")
    heading()
    time.sleep(0.2)
    print("\n\t================= Settings =================")
    time.sleep(delay)
    print("\t{}Hanabi:{} Welcome to the settings area.".format(RED, WHITE))
    time.sleep(delay)
    print("\t{}Hanabi:{} Choose what you want to setup.\n".format(RED, WHITE))
    time.sleep(delay)
    print("\t{}[1]{} Set Terminal, current ({})".format(YELLOW, WHITE, conf["terminal"]))
    print("\t{}[2]{} Fancy delays\n".format(YELLOW, WHITE))
    print("\t{}[Menu]{} Return to menu.".format(YELLOW, WHITE))
    print("\t{}[Quit]{} Quit Hanabi.\n".format(YELLOW, WHITE))
    while True:
        decide = str(input("\tHanabi > "))
        if decide == "1":
            terminal_choice = str(input("{}Terminal{} (Case Sensitive): ".format(YELLOW,WHITE)))
            tildes()
            print("Setting terminal, please wait.")
            equals()
            time.sleep(2)
            ####
            with open(config, 'w') as f:
                conf['terminal'] = terminal_choice + " -e"
                conf['firststart'] = 'false'
                yaml.dump(conf, f, default_style="'")
                f.close()
            ####
        elif decide == "2":
            fancy_delay = str(input("\tTurn fancy delays \"on\" or \"off\"?\n\t Delays > "))
            if fancy_delay == "on":
                tildes()
                print("\tTurning fancy delays {}on{}".format(BLUE, WHITE))
                equals()
                with open(config, 'w') as f:
                    conf['fancydelay'] = 'on'
                    yaml.dump(conf, f, default_style="'")
                    off.close()
                    time.sleep(2)
                tildes()
                print("\tFancy delays are now [{}ON{}]".format(BLUE, WHITE))
                print("\tPlease {}restart{} to take effect".format(GREEN, WHITE))
                equals()
            elif fancy_delay == "off":
                tildes()
                print("\tTurning fancy delays {}off{}".format(BLUE, WHITE))
                equals()
                with open(config, 'w') as f:
                    conf['fancydelay'] = 'off'
                    yaml.dump(conf, f, default_style="'")
                    f.close()
                    time.sleep(2)
                tildes()
                print("\tFancy delays are now [{}OFF{}]".format(BLUE, WHITE))
                print("\tPlease restart to take effect")
                equals()
            else:
                print("\t{}Unknown argument! Returning to settings{}".format(RED, WHITE))
                time.sleep(1)
                Settings()
                break
        elif decide == "Quit":
            quitHanabi()
        elif decide == "Menu":
            time.sleep(1)
            print("\t{}Leaving{}, returning to menu.".format(RED, WHITE))
            time.sleep(1)
            menu()
            break
        else:
            print("\t{}Please choose a valid option{}".format(RED, WHITE))
            time.sleep(2)
            Settings()
 
####
conf = loadConfig()
if conf["fancydelay"] == "on":
    fancydelay = 0.2
else:
    fancydelay = 0
####

###  Main Process ###
###  Starts here  ###

### First Startup Setup ###
if conf["firststart"] == 'true':
    delay = 1
    heading()
    firstStart()
    ###  Quick Setup  ###
    Settings()
   ### ##### ##### ###

elif conf["firststart"] == 'false':
    delay = 0
    menu()
