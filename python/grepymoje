#!/usr/bin/python

import os
import sys
import re
import getopt
import myregex

# globals
myname = sys.argv[0].split( os.sep )[-1]


def usage():
    sys.exit( "usage: " + myname + " <string>")


def print_help():
    print """
    grepy is grep-like program that recursively searches for string in C, C++, JavaScript
    and QML files.

    available options:
        -h | --help             prints usage
        -i | --ignorecase       ignores case 
    """
    sys.exit(0)

def main():

    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "hi", ["help", "ignorecase"])

    except getopt.GetoptError:
        usage()

    ignorecase = False

    for opt, arg in opts:
        if opt in ( "-h", "--help" ):
            print_help()
        if opt in ( "-i", "--ignorecase" ):
            ignorecase = True

    if not len( args ) == 1: usage()


    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            fullname = os.path.join(dirname, filename)

            if myregex.is_cfile(filename) or myregex.is_jsfile(filename):
                file = open(fullname, "r")
                for line in file:
                    if line[-1] == '\n': line = line[:-1]

                    if ignorecase: research = re.search( sys.argv[1], line, re.I )
                    else: research = re.search( sys.argv[1], line )

                    if research: print fullname + ": " + line

                file.close()


if __name__ == "__main__":
    main()

