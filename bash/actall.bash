#!/bin/bash
# 
# this is bash example for action on all files provided as cmd line arguments
#

for FN in $*
do
    echo changing $FN...
    # action
    chmod 0750 $FN
done