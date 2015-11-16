#!/usr/bin/python

import os
import sys
import re
import getopt



# this should be really command line arguments...
def usage():
    print "usage: " + sys.argv[0] + " <string> <pattern> %d" % len(sys.argv)


def main():

    try:
        opts, args = getopt.gnu_getopt(
            sys.argv[1:],
            "h:p:d:",
            ["host=", "port=", "deeplink="]
        )
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for o, a in opts:
        print "option : " + o + "  argument : " + a


if __name__ == "__main__":
    main()
