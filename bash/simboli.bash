#!/bin/bash
# 
# demangles symbols from the file <file>, grepped by <pattern>
#

if [ $# -ne 2 ] 
then 
    echo "usage: $0 <elffile> <pattern>" 
fi

nm $1 | grep $2 | awk '{ print $3 }' | xargs c++filt

## comment to be todoed:
#
#UNIX GURU UNIVERSE
#UNIX HOT TIP
#
#Unix Tip 3561 - November  9, 2011
#
#
#If you ever find yourself typing "command | grep pattern | awk '{print $3}'
#you can shorten this by using the regexp matching in awk, like this:
#
#command | awk '/pattern/{print $3}'
#
#
# which would in this case be:
# nm $1 | awk '/$2/{ print $3 }' | xargs c++filt
