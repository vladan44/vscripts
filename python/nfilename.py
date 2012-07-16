#!/usr/bin/python
#
# Module: nfilename
# 
# functions:
# Function: newest_filename
# Function: get_file_time

import os

###############################################################################
#
# Function: newest_filename
#
# Description: 
#
# Notes: uses linear search - to be optimized: 
#
# @arg string: path - path to the directory where newest filename  
# is to be searched
# @arg bool: recursive - true if newest file is to be looked up in whole tree
#                         false if it is searched only in specified directory
#
# @ret: newest - filename of the newest filename in directory
#

def newest_filename( path , recursive ):

    files = []

    if recursive:
        for dirname, dirnames, filenames in os.walk( path ):
            for filename in filenames:
                files.append( os.path.join(dirname, filename) )

    else:
        files = os.listdir( path )

    # search for newest 
    if len(files):
        newest = files[0]
    else:
        newest = "anewfile"

    for filename in files:
        if get_file_time( newest ) <  get_file_time( filename ):
            newest = filename

    return newest

###############################################################################
#
# Function: get_file_time
#
# Description: given filename returns file modification time
#
# Notes: assumes that the 9th member of stat structure is modification time
#
# @ret integer: number of seconds since unix era

def get_file_time( filename ):
    return os.stat( filename )[8] 


