#!/usr/bin/python
################################################################################
# list files in the descending order by their sizes
#

import os
import sys
import getopt 

import platform



sort = "C:\\gnu\\bin\\sort.exe"
grep = "C:\\gnu\\bin\\grep.exe"
ls   = "C:\\gnu\\bin\\ls.exe -l"
recursive = False

myname = sys.argv[0].split( os.sep )[-1]


def usage():
    sys.exit( "usage: " + myname + " [-r|--recursive]" )

def print_help():
    print """
    lssize

    This file is only meant to run on Windows systems.
    """
    sys.exit(0)


def main():

    global sort 
    global grep
    global ls 
    global recursive

    if( platform.system() != 'Windows' ):
        print_help()

    try:
        opts, args = getopt.getopt( sys.argv[1:], "rh", ["recursive", "help"] )
    except:
        usage()

    for o, a in opts:
        if o == '-r' or o == "--recursive":
            recursive = True
            print " recursive"
        if o == '-h' or o == "--help":
            usage()

    if recursive: ls = ls + "R"

    cmd = ls + " | " + grep + " \"^-\" | " + sort + " -nr -k 5"

    os.system( cmd )


if __name__ == "__main__":
    main()

