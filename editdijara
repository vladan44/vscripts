#!/usr/bin/python
#
###############################################################################
# script that accompanies 'dijara' alias 
# used to edit the latest dijara entry

import os
import sys
import re
import getopt
import nfilename
import subprocess


###############################################################################
# globals
###############################################################################
myname = sys.argv[0].split( os.sep )[-1]

###############################################################################
# functions
###############################################################################
def usage():
    sys.exit( "usage: " + myname + " [-h|--help] [-l|--less]" )


def print_debug(x):
    # print(x)
    pass


def windows():
    if sys.platform[:3] == 'win': return True
    else: return False


def dijara_home():
    if windows(): 
        windows_dijara = 'C:\\dijara'

        print_debug( windows_dijara )
        return windows_dijara
    else: 
        whoami = subprocess.check_output(["whoami"])
        if whoami[-1] == '\n': whoami = whoami[:-1]
        default_dijara = '/home/' + whoami + '/dijara'

        print_debug( default_dijara )
        return default_dijara


def edit_command(justread):
    if windows(): 
        windows_editor = "C:\\Vim\\vim73\\gvim.EXE" 
        print_debug( windows_editor)
        return windows_editor 
    else: 
        if not (justread): default_editor = 'vi'
        else: default_editor = 'less'
        print_debug( default_editor )
        return default_editor


# main
def main():

    try:
        opts, args = getopt.getopt( sys.argv[1:], "hl", ["help", "less"] )
    except:
        usage()

    justread = False

    for o, a in opts:
        if o == '-h' or o == "--help":
            usage()
        if o in ("-l", "--less"):
            justread = True

    file_to_edit = nfilename.newest_filename( dijara_home(), True )
    
    command = edit_command(justread) + " " + file_to_edit

    print_debug( command )
    os.system( command )


###############################################################################
# main
###############################################################################
if __name__ == "__main__":
    main()


