#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  fileTimestamp.pl
#
#        USAGE:  ./fileTimestamp.pl 
#
#  DESCRIPTION:  Timestamps of the file
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  1/21/2007 10:02:46 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

use File::Find;
use Time::localtime;

die "usage: perl fileTimestamp.pl <filename>" unless $#ARGV == 0;

my $filename = $ARGV[0];
my ($readtime, $writetime) = (stat($filename))[8,9];

my $tmread = localtime($readtime);
my $tmwrite = localtime($writetime);

printf("File: %s is read %02d:%02d:%02d-%04d/%02d/%02d\n",
    $filename,
    $tmread->hour, 
    $tmread->min, 
    $tmread->sec, 
    $tmread->year + 1900, 
    $tmread->mon + 1, 
    $tmread->mday 
);

printf("File: %s is written %02d:%02d:%02d-%04d/%02d/%02d\n",
    $filename,
    $tmwrite->hour, 
    $tmwrite->min, 
    $tmwrite->sec, 
    $tmwrite->year + 1900, 
    $tmwrite->mon + 1, 
    $tmwrite->mday 
);

