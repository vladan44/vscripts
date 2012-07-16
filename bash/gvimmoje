#!/bin/bash

if [ $# -ne 1 ]
then
	echo "usage $0 <string>"
	exit 0;
fi

grp -n $1 | moje | awk ' BEGIN{ FS=":" } { print $1, "+"$2 }' | xargs gvim

