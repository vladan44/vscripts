#!/bin/bash

if [ $# -ne 1 ] 
then 
    echo "usage: $0 <programname>" 
fi

valgrind -v $1 2>&1 | egrep -i -B 1 -A 4 "ERROR SUMMARY|leak"
