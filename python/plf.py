#!/usr/bin/python

import platform

output  = platform.system()  + '\n'
output += platform.version() + '\n'
output += platform.release()

print output

