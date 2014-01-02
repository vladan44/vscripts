#!/bin/bash

SERVICE=$1

me=`basename $0`

# psgrep=`ps ax | grep -v grep | grep -v $me | grep $SERVICE` 
# echo $psgrep
# pid=$(echo $psgrep | awk '{ print $1 }') > /dev/null
# echo $pid ========

pid=`ps ax | grep -v grep | grep -v $me | grep $SERVICE |\
    awk '{ print $1 }'`> /dev/null

name=`ps ax | grep -v grep | grep -v $me | grep $SERVICE |\
    awk '{ print $5 }' | head -1 `> /dev/null

if [[ $name != "" ]] 
then 
    servicename=`basename $name` 
fi

if [[ $pid  != "" ]] 
then
    echo "$servicename service running, ids:"
    echo $pid
else
    echo "$SERVICE is not running"
fi
