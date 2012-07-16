#!/usr/bin/python

import nfilename
import bcolors
import sys

sys.stdout.write(bcolors.bcolors.WARNING)
print nfilename.newest_filename( ".", True )
sys.stdout.write(bcolors.bcolors.ENDC)

sys.stdout.write(bcolors.bcolors.HEADER)
print nfilename.newest_filename( ".", True )
sys.stdout.write(bcolors.bcolors.ENDC)

sys.stdout.write(bcolors.bcolors.OKBLUE)
print nfilename.newest_filename( ".", True )
sys.stdout.write(bcolors.bcolors.ENDC)

sys.stdout.write(bcolors.bcolors.OKGREEN)
print nfilename.newest_filename( ".", True )
sys.stdout.write(bcolors.bcolors.ENDC)

sys.stdout.write(bcolors.bcolors.FAIL)
print nfilename.newest_filename( ".", True )
sys.stdout.write(bcolors.bcolors.ENDC)

