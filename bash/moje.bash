#!/usr/bin/python

import os
import sys
import re

myfiles = []

for line in sys.stdin:
    if line[-1] == '\n': line = line[:-1]
    for myfile in myfiles:
        if re.search( myfile, line ) and not re.search( "svn", line ):
            print line

