#!/bin/bash

# generating range of numbers
# it is useful for command line usage as:
#   $ for i in `range 3 20` ; do <something> ; done

low=$1
high=$2

while [ $low -le $high ]
do
    echo -n $low ""
    low=`expr $low + 1`
done