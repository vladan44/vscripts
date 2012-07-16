#!/usr/bin/python

import os
import sys

if len( sys.argv ) != 2: 
    sys.exit( "usage " + sys.argv[0] + " <string>" )

command = "find . -regex '.*\.h[ix]?\|.*\.cpp' | xargs grep " +  sys.argv[1]

os.system( command )

