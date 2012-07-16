#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  devetpet.pl
#
#        USAGE:  ./devetpet.pl 
#
#  DESCRIPTION:  Tacno je ...
#
#      OPTIONS:  None
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  12/27/2006 3:57:27 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

# by-name interface to Perl's built-in localtime() function
use Time::localtime; 

printf "Datum je %02d. %02d. %04d.\n", 
                                localtime->mday(),
                                localtime->mon() + 1, 
                                localtime->year() + 1900;

printf "Tacno je %02d casova, %02d minuta i %02d sekundi\n", 
                                localtime->hour(), 
                                localtime->min(), 
                                localtime->sec();
