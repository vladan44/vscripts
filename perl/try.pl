#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  try.pl
#
#        USAGE:  ./try.pl 
#
#  DESCRIPTION:  regular expression examples. This is the program to test run 
#                regular expressions
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  12/9/2010 5:31:06 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

my $mystring = "[2004/04/13] The date of this article.";
my @myarray = ( $mystring =~ m/(\d+)/g );
print join(",", @myarray);



