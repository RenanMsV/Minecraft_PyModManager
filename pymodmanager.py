import sys
import glob
import os
import win_console

VERSION_TO_MANAGE = 'null'
FOLDERS = 'null'
FILES = 'null'

def main():
    global VERSION_TO_MANAGE, FOLDERS
    print('Python {}'.format(sys.version))
    print("Starting manager\n\n\n....\n\n\n")
    print('Select the version you want to manage:\n')
    FOLDERS = glob.glob("*/")
    for i in range(len(FOLDERS)):
        if not (FOLDERS[i] == "__pycache__\\"):
            print('{} - {}'.format(i, FOLDERS[i]))
    VERSION_TO_MANAGE = input('')
    if not (VERSION_TO_MANAGE.isnumeric()):
        print('This is not a number. Aborting.')
    else:
        print('Managing version : {}'.format(FOLDERS[int(VERSION_TO_MANAGE)])[:-1])
    loopManageMods()

def loopManageMods():
    SELECTED_MOD = '0'
    while not (SELECTED_MOD == '-1'):
        global VERSION_TO_MANAGE, FOLDERS, FILES
        win_console.set_color(10)
        print('\n=# Enabled mods: #=\n')
        win_console.set_color(7)
        FILES = glob.glob("{}/*".format(FOLDERS[int(VERSION_TO_MANAGE)]))
        for i in range(len(FILES)):
            if not FILES[i].endswith('.pymodmanager'):
                print('{} - {}'.format(i, FILES[i]))
        win_console.set_color(12)
        print('\n=# Disabled mods: #=\n')
        win_console.set_color(7)
        for i in range(len(FILES)):
            if FILES[i].endswith('.pymodmanager'):
                print('{} - {}'.format(i, FILES[i]))
        SELECTED_MOD = input('\nSelect the mod you want to disable/enable. Type -1 to exit.\n')
        if not SELECTED_MOD == '-1' and int(SELECTED_MOD) < len(FILES):
            enable_disableMod(FILES[int(SELECTED_MOD)],FILES[int(SELECTED_MOD)].endswith('.pymodmanager'))

def enable_disableMod(path, enable):
    if enable:
        os.rename(path,path[:-13])
    else:
        os.rename(path, '{}.pymodmanager'.format(path))

main()
input("\nFinishing...\n\nEnter to close this window")