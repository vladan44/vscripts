#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  grepim.pl
#
#        USAGE:  ./grepim.pl 
#
#  DESCRIPTION:  recursive grep using perl's grep
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  1/21/2007 9:26:41 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;
use File::Find;

my $usage = "usage: $0 <string> \n";

sub printaj 
{
    open FILE, $_ or return;
    print grep {m/$ARGV[0]/} <FILE> ;
}

#########################################################
# main

# command line verificaiton
die $usage unless $#ARGV == 0 ; 

my @directories = <*>; 

find \&printaj, @directories;

