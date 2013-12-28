#!/bin/bash
# /usr/bin/backup
# Backup script for Directory X and PHP Include Files
# The following MySQL databses are also backed up:
# DB_NAME
#
# DATE: 05/05/2003

#################################
# Assign DTG and Date variables #
# to $a & $b respectively       #
#################################
a=$(date +%T-%d_%m_%Y)
b=$(date +%d_%m_%Y)

#############################

echo "Backup made at: " $a 

if [ ! -e /usr/local/share/backups ]
then
    mkdir /usr/local/share/backups
fi 

if [ ! -e /usr/local/share/backups/$b ]
then
    mkdir /usr/local/share/backups/$b
fi

tar czvf --exclude "gnupoc" --exclude "workspace" /usr/local/share/backups/$b/home_dir.tar.gz $HOME

