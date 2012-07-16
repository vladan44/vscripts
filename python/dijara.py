#!/usr/bin/python

import os
import sys
import datetime
import platform

if not len( sys.argv ) == 1: 
    sys.exit( 'no arguments are accepted' )

datum = datetime.date.today()

ostype = platform.system()
if( ostype == 'Windows' ): 
    dir = "C:\\dijara\\"
    clear = 'cls'
else: 
    dir = "~/dijara/"
    clear = 'clear'

file = "notes-" + datum.isoformat() + ".txt"
command = "cat >> " + dir + file

if( ostype == 'Windows' ): 
    os.system( clear )
    print "win verson of dijara is closed with CTRL-Z"
    print "=========================================="

os.system( command )
#os.system( clear )

