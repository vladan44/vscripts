#!/usr/bin/python
#
###############################################################################
# Name: recursivepie
# 
# Script that racursively modifies string in file on specified path

import os
import sys
import re
import getopt

import myregex

usage = "usage: " + sys.argv[0] + " <fromstring> <tostring> <path>"
perl  = "perl -pi.bak -e " 

def get_sed( arg1, arg2 ):
    return "\"s/" + arg1 + "/" + arg2 + "/g\" "


def print_usage():
    print usage
    sys.exit(0)


def print_help():
    print """
    recursivepie

    script that recursively modifies string in file on specified path. It is 
    based on 'perl -pi -e' command, and depends on non-standard myregex module. 

    This version is for c and c++ file exclusively. Current patterns that are
    matched are:
    *.cpp *.c *.C *.h *.H *.inl

    All modified files are backud up with .bak extension. Also, all modified 
    files are printed during execution.

    Synopsis is:
    """ + usage + """

    **** This is silent killer, dont use it without care! **** 
    """

    sys.exit(0)

# main
def main():

    try:
        opts, args = getopt.gnu_getopt( sys.argv[1:], "h", ["help"] )

    except getopt.GetoptError:
        print_usage()

    for opt, arg in opts:
        if opt in ( "-h", "--help" ): print_help()

    if len(sys.argv) != 4: 
        print_usage()

    print "** This is silent killer, dont use it without care! ** "

    for root, dirs, files in os.walk( sys.argv[3] ):
        for file in [f for f in files if myregex.is_cfile(f) or myregex.is_jsfile(f) ]:
            changefile = False
            apath =  os.path.abspath( root )
            fullpath =  os.path.join( apath, file )
            fd = open( fullpath )
            for line in fd:
                if re.search( sys.argv[1], line ):
                    changefile = True

            fd.close()

            if( changefile == True ):
                changefile = False
                print fullpath
                command = perl + get_sed( sys.argv[1], sys.argv[2] ) + fullpath
                os.system( command ) 

###############################################################################
# main
###############################################################################
if __name__ == "__main__":
    main()


