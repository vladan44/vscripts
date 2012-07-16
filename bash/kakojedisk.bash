#!/bin/bash

# This script does a very simple test for checking disk space.
# it is illustration of case statement in bash

space=`df -h | awk '{print $5}' | grep -v Use | sort -n | 
       tail -1 | cut -d "%" -f1 -`

case $space in
    [1-6]*)
	Message="All is quiet. Disk space is $space % full."
	;;
    [7-8]*)
	Message="Start thinking about cleaning out some stuff. 
                 Disk usage is $space %"
	;;
    9[1-8])
	Message="Better hurry with that new disk...  Disk usage is $space %"
	;;
    99)
	Message="I'm drowning here! There's a partition at $space %!"
	;;
    *)
	Message="???? Disk usage space is $space % "

	;;
esac

echo $Message 

