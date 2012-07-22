#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  myhead.pl
#
#        USAGE:  ./myhead.pl 
#
#  DESCRIPTION:  Prints lines of the input file that are beetween $from and
#               $to
#
#      OPTIONS:  from - line number of the first line to be printed
#                to - line number of the second line to be printed
#                filename - input file name
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  $. is input line number
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  04/07/2006 10:18:23 Pacific Daylight Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

die "Usage: myhead <from> <to> <filename>"
unless $#ARGV == 2;

my $from     = shift;
my $to       = shift;
my $filename = shift;

die "First two arguments should be natural numbers."
unless  $from =~ /^\d+$/ && $to =~ /^\d+$/;

die "Arguments cannot be 0s."
if $from == 0 || $to == 0;

die "Third argument should be readable file."
unless  -e $filename && -r $filename;

# constraint
($from, $to) = ($to, $from) if $from > $to;

open FILE, $filename;
while(<FILE>) { print $_ if $. == $from .. $. == $to; }
close FILE;


