#! /usr/bin/python3
import subprocess as sp


def get_application_window_index(application_name):
    match application_name:
        case 'spotify':
            return 0
        case 'code':
            return 1
        case 'brave-browser':
            return 2
        case 'jetbrains-idea':
            return 3
        case _:
            return 0


def move_application_to_workspace(process_id, window_index):
    # wmctrl -r <WIN> -t <DESK> 
    cmd = f"wmctrl -i -r {process_id} -t {window_index}"
    sp.run(cmd, shell=True, encoding="utf8")


# get list of applications and save in var
p = sp.Popen(["wmctrl", "-l", "-x"], stdout=sp.PIPE)
runningApps, err = p.communicate()

# convert to string
runningApps = str(runningApps, 'utf-8')

# splitting each application
runningApps = runningApps.split('\n')

for x in runningApps:
    if len(x):
        temp = x.split(' ')
        
        processId = temp[0]
        dotPosition = temp[3].find('.')
        applicationName = temp[3][0:dotPosition]

        windowIndex = get_application_window_index(applicationName)
        move_application_to_workspace(processId, windowIndex)
