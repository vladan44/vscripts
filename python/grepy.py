#!/usr/bin/python

import os
import sys
import re
import getopt

sys.dont_write_bytecode = True
import bcolors

# this should be really command line arguments...
excludes = ["svn", "swp"]

# globals
myName = sys.argv[0].split(os.sep)[-1]


def usage():
    sys.exit("usage: " + myName + " <string> <pattern> ")


def print_help():
    sys.stdout.write(bcolors.bcolors.WARNING)
    print """
    grepy is grep-like program that recursively searches for string in files 
    that match pattern in their filenames.  
    Synopsis is: 

        grepy <string> <pattern> [OPTIONS]

    Available options:

        -h | --help             prints usage
        -p | --printexcludes    print patterns that will be excluded from search
        -l | --lineno           print line numbers 
        -x | --excludes         add exclude patterns
        -i | --ignorecase       ignores case \n"""
    sys.stdout.write(bcolors.bcolors.ENDC)
    sys.exit(0)


def print_excludes():
    print "-------------------------------------------------"
    print "excludes: ",

    for exclude in excludes:
        print "| " + exclude,

    print "\n-------------------------------------------------"
    return

def main():

    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                "hipnx:", ["help", "ignorecase", "printexcludes", "lineno", "excludes"])

        if not len(args) == 2:
            usage()

    except getopt.GetoptError:
        usage()

    printex = False
    lineno = False
    ignorecase = False

    for opt, arg in opts:
        if opt in ("-p", "--printexcludes"):
            printex = True
        if opt in ("-n", "--lineno"):
            lineno = True
        if opt in ("-h", "--help"):
            print_help()
        if opt in ("-i", "--ignorecase"):
            ignorecase = True
        if opt in ("-x", "--excludes"):
            lineno = True
            excludes.append(arg)

    if printex:
        print_excludes()

    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            fullname = os.path.join(dirname, filename)
            
            if re.search(args[1], fullname):
                ex = False
                for exclude in excludes: 
                    if re.search(exclude, fullname):
                        ex = True
                if ex: continue
                fd = open(fullname, "r")
                counter = 0
                for line in fd:
                    counter += 1
                    if line[-1] == '\n': line = line[:-1]
                    if ignorecase: research = re.search(args[0], line, re.I)
                    else: research = re.search(args[0], line)
                    if research:
                        if lineno:
                            sys.stdout.write(bcolors.bcolors.WARNING)
                            print fullname + ":%d" % counter + ": " + line
                            sys.stdout.write(bcolors.bcolors.ENDC)
                        else:
                            sys.stdout.write(bcolors.bcolors.WARNING)
                            print fullname + ": " + line
                            sys.stdout.write(bcolors.bcolors.ENDC)
                fd.close()

if __name__ == "__main__":
    main()

