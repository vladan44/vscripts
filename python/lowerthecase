#!/usr/bin/python

import os

for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        fullname = os.path.join(dirname, filename)
        if not fullname.islower():
            toname = fullname.lower()
            cmd = "mv " + fullname + " " + toname
            print cmd
            os.system( cmd )
