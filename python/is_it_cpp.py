#!/usr/bin/python

import sys
import vregex

if not len( sys.argv ) == 2: sys.exit( "usage: " + sys.argv[0] + " filename" ) 

if vregex.is_cfile( sys.argv[1] ): 
    print "True: " + sys.argv[1] 
else:
    print "False: " + sys.argv[1] 
