#!/usr/bin/python

import fnmatch
import sys
import os

if len(sys.argv) != 3: 
  sys.exit( "usage: grpy <string> <filepattern>" )

rootPath = '.'
string = sys.argv[1]
filepattern = sys.argv[2]

def mygrep( root, filename ):
    print os.path.join(root, filename) + ": "
    os.system( "grep -n " + string + " " + os.path.join(root, filename) )

for root, dirs, files in os.walk(rootPath):
    for filename in files:
        if fnmatch.fnmatch(filename, filepattern):
            mygrep( root, filename )


