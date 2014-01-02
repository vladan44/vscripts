#!/usr/bin/python

import os
import sys
import datetime
import platform

if not len( sys.argv ) == 1: 
    sys.exit( 'no arguments are accepted' )

datum = datetime.date.today()
iswin = platform.system() == 'Windows'

if iswin:
    dir = "C:\\dijara\\"
    clear = 'cls'
else: 
    dir = os.environ['HOME'] + "/dijara/"
    clear = 'clear'

if not os.path.isdir(dir):
	os.system ("mkdir " + dir)

file = "notes-" + datum.isoformat() + ".txt"
command = "cat >> " + dir + file

if iswin:
    os.system(clear)
    print "win verson of dijara is closed with CTRL-Z"
    print "=========================================="

os.system(command)
#os.system(clear)

