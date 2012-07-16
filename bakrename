#!/bin/bash
# 
# Renaming File extensions
#
# usage: bakrename <old> <new> 
#
# example: bakrename bak txt
# 

E_BADARGS=65 # bad number of arguments error number

case $# in
	0|1)
		echo "usage: `basename $0` old_file_suffix new_file_suffix"
		exit $E_BADARGS  # if 0 or 1 number of arguments
	;;
esac

# for all files ending with first argument
echo "moving .$1 files to .$2 files..."
for filename in *.$1
do 
	mv $filename ${filename%$1}$2
	# stripp off part of filename matching 1st argument, and append the second
    # another posibility:
    # mv $f `basename $f $1`$2
done

exit 0
