#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  bakrename.pl
#
#        USAGE:  ./bakrename.pl 
#  DESCRIPTION:  renames multiple files, e.g:
#                   pera.<from_string> to pera.<to_string>
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  1/22/2007 10:38:16 AM Pacific Standard Time
#
#     REVISION:  1.1 11/23/2007 changing behavior so script rename files from 
#                pera<from_string>ra to pera<to_string>ra
#                note: if second argumend is an empty string:
#                      use superset string, e.g. use:
#                                     % perl bakrename.pl "pera" "p" 
#                      instead of:
#                                     % perl bakrename.pl "era" ""
#                Dilemma: should I keep the old version, just to modify
#                         extentions ?
#===============================================================================

use strict;
use warnings;

my $usage = "usage: perl $0 <from_string> <to_string>";

die $usage unless $#ARGV == 1; 

#=======  main
#
# my @files = glob("*.$ARGV[0]");
my @files = glob("*");

foreach my $file (@files)
{
    my $oldfile = $file; 
    # $file =~ s/\.$ARGV[0]/\.$ARGV[1]/;
    $file =~ s/$ARGV[0]/$ARGV[1]/;
    unless (-e $file) 
    { 
        print "renaming $oldfile to $file...\n";
        rename $oldfile, $file; 
    }
    else { print "file $file already exists, skipping...\n"; }
}

