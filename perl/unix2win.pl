#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  unix2win.pl
#
#        USAGE:  ./unix2win.pl 
#
#  DESCRIPTION:  recursive addition of WINDOWS' carriage return
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  6/20/2007 9:26:41 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

use File::Find;

sub printaj 
{
    if ( $_ =~ /\.[hc]/i ) 
    {
        my $filename = $_;
        my $tempname = $_ . ".temp";

        print "File: $filename  :\n" ;

        open FILE,  "$filename"  || die "Cannot open file: $filename $!";
        open OUT, "> $tempname"  || die "Cannot open file: $tempname $!";

        while (<FILE>)
        {
            s/\n/\r\n/;
            print OUT $_;
        }

        close FILE;
        close OUT;

        unlink $filename;
        rename $tempname, $filename;
    }
}

#########################################################
# main

my @directories = <*>; 

find \&printaj, @directories;

