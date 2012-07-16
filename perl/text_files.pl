#!/usr/bin/perl

use File::Find;

################################################################################
$usage = "usage: text_files <string> \n";

sub print_files { print "$_\n" if m/$ARGV[0]/ ; }

################################################################################
# main

# command line verificaiton
die $usage unless $#ARGV == 0 ;

find \&print_files, glob "*" ;

