#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  allFiles.pl
#
#        USAGE:  ./allFiles.pl
#
#  DESCRIPTION:  Example of processing All Files in a Directory Recursively
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:
#      VERSION:  1.0
#      CREATED:  1/21/2007 9:50:08 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

use File::Find;

sub process_file {
    # do something ....
    print $_ . "\n" unless (-d $_);
}

my @directories = glob("*");
find (\&process_file, @directories);
