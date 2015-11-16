#!/usr/bin/python

import os
import sys
import re
import json
import getopt
import bcolors


# globals
myname = sys.argv[0].split( os.sep )[-1]


def usage():
    sys.exit( "usage: " + myname + " <filename> [OPTIONS]")


def print_valid_json_warning(filename):
    sys.stdout.write(bcolors.bcolors.WARNING)
    print """ *** file --> """ + filename + """  <-- should contain valid """\
    """ json object to be parsed\ncorrectly."""
    sys.stdout.write(bcolors.bcolors.ENDC)
    sys.exit(0)


def print_help():
    sys.stdout.write(bcolors.bcolors.OKBLUE)
    print """
    jparse is script for parsing JSON files
    
    Synopsis is: \n
    """ + myname + """ <filename> [OPTIONS]

    Available options:

        -h | --help             prints usage
        -l | --lineno           print line numbers  \n"""
    sys.stdout.write(bcolors.bcolors.ENDC)
    sys.exit(0)


def print_json(fj, lineno):
    j = 0

    for i in fj: 
        if lineno: 
            j += 1
            ln = "%2d." % j 
        else:
            ln = ""
        print ln + bcolors.bcolors.OKBLUE + '%20s :' % i + \
            bcolors.bcolors.OKGREEN + " %s" % fj[i]
        sys.stdout.write(bcolors.bcolors.ENDC) 


def main():

    try:
        opts, args = getopt.gnu_getopt(
            sys.argv[1:],
            "hn",
            [
                "help",
                "lineno"
            ]
        )
        
    except getopt.GetoptError:
        usage()

    lineno = False
    filename = args[0]

    for opt, arg in opts:
        if opt in ( "-n", "--lineno" ):
            lineno = True
        if opt in ( "-h", "--help" ):
            print_help()
        if opt in ( "-i", "--ignorecase" ):
            ignorecase = True

    if not len(args) == 1:
        usage()

    try: 
        fd = open(filename, 'r') 
        fc = fd.read() 
        fd.close()

    except:
        print_help()

    try: 
        fj = json.loads(fc)
        # fj = json.read(fc)
    except:
        print_valid_json_warning(filename)

    print bcolors.bcolors.OKBLUE + "======================================================"

    print_json(fj, lineno)

if __name__ == "__main__":
    main()

