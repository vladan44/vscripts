#!/usr/bin/python

import os
import sys
import datetime
import platform

if not len( sys.argv ) == 1: 
    sys.exit('no arguments are accepted')

datum = datetime.date.today()
is_win = platform.system() == 'Windows'

if is_win:
    dir_name = "C:\\dijara\\"
    clear = 'cls'
else: 
    dir_name = os.environ['HOME'] + "/dijara/"
    clear = 'clear'

if not os.path.isdir(dir_name):
    os.system("mkdir " + dir_name)

file_name = "notes-" + datum.isoformat() + ".txt"
command = "cat >> " + dir_name + file_name

if is_win:
    os.system(clear)
    print "win version of dijara is closed with CTRL-Z"
    print "=========================================="

os.system(command)
#os.system(clear)

