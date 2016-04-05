#!/usr/bin/python
################################################################################
# list files in the descending order by their sizes
#

import os
import sys
import getopt 
import platform

gnuenv = 'GNUPATH'
myname = sys.argv[0].split( os.sep )[-1]


def usage(e):
    if e:
        print e
    sys.exit("usage: " + myname + " [-r|--recursive]")


def print_help():
    print """
    lssize

    This script is only meant for Windows systems, since there is a simple
    alternative in bash, nevertheless it runs on Unices as well.
    """
    sys.exit(0)


def main():

    global recursive
    global gnuenv

    if platform.system() == "Linux":
        sort = "sort"
        grep = "grep"
        ls = "ls -l"
    else:
        gnupath = os.environ[gnuenv]
        sort = gnupath + "sort.exe"
        grep = gnupath + "grep.exe"
        ls = gnupath + "ls.exe -l"
    recursive = False

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "rh",
            ["recursive", "help"]
        )

        for o, a in opts:
            if o == '-r' or o == "--recursive":
                recursive = True
                print " recursive"
            if o == '-h' or o == "--help":
                usage(None)

        if recursive:
            ls += "R"

        cmd = ls + " | " + grep + " \"^-\" | " + sort + " -nr -k 5"
        os.system(cmd)

    except Exception as e:
        usage(e)


if __name__ == "__main__":
    main()

