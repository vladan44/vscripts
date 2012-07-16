#!/usr/bin/python

import sys
import myregex

if not len( sys.argv ) == 2: sys.exit( "usage: " + sys.argv[0] + " filename" ) 

if myregex.is_cfile( sys.argv[1] ): 
    print "True: " + sys.argv[1] 
else:
    print "False: " + sys.argv[1] 
