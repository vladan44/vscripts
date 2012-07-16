import sys
import os

myname = sys.argv[0].split( os.sep )[-1]

def usage_options():

    try:
        opts, args = getopt.getopt( sys.argv[1:], "h", ["help"] )
    except:
        usage()

    for o, a in opts:
        if o == '-h' or o == "--help":
            usage()

def usage():
    sys.exit( "usage: " + myname + " [-h|--help]" )

            
