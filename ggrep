#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  ggrep.pl
#
#        USAGE:  ./ggrep.pl 
#
#  DESCRIPTION:  script to describe entire blocks
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  12-05-28 09:46:12 AM PDT
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

die "Usage: ggrep <pattern> <file>"
unless $#ARGV == 1;

my $pattern  = shift;
my $filename = shift;

$/ = '{';
$\ = '}';

open FILE, $filename;
while (<FILE>) { print if /$pattern/; }
close FILE;


