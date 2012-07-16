#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  grp.pl
#
#        USAGE:  ./grp.pl 
#
#  DESCRIPTION: recursive grep 
#
#      OPTIONS:  string filepattern
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  1/21/2007 4:38:38 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

# command line verificaiton

die "usage: $0 <string> <filename>" unless ( $#ARGV == 1 ); 

my $myfind = "c:\\myutils\\unxutils\\ufind.exe";

system "$myfind . -name $ARGV[1] -print | xargs grep -i $ARGV[0] " ;
