#!/usr/bin/python

import os
import re
import sys
import glob


def usage():
    print """    usage """ + sys.argv[0] + """ <from> <to>"""
    sys.exit(0)


def main():
    if not len(sys.argv) == 3: usage()

    for oldname in glob.glob("*"):
        if re.search(sys.argv[1], oldname):
            newname = re.sub(sys.argv[1], sys.argv[2], oldname)
            print "moving ", oldname, " to ", newname
            os.rename(oldname, newname)


if __name__ == "__main__":
    main()
