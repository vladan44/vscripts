#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  lstr.pl
#
#        USAGE:  ./lstr.pl 
#
#  DESCRIPTION:  sorting files by date in multiple directories
#
#      OPTIONS:  none
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:
#      VERSION:  1.0
#      CREATED:  12/27/2006 9:47:35 AM Pacific Standard Time
#     REVISION:  1.0
#===============================================================================

use strict;
use warnings;
use File::Find;
use Time::localtime;
use Term::ANSIColor;          

#===============================================================================
### my variables
my $usage = "usage: $0\n";
my @dirs; my @files; 
my $file; my %combe;

#===============================================================================
### my subroutines
sub funkcija 
{ 
    # my $vreme = -M $_; 
    unless ( -d $_ )
    {
        my $vreme = (stat($_))[9];
        # my $vreme = (stat($_))[8];
        $combe{ $_ } = $vreme; 
    }

}

sub sorting { $combe{$b} <=> $combe{$a}; }

#===============================================================================
### main

### command line verification
die $usage unless $#ARGV == -1;

@dirs = <*>;

find \&funkcija, @dirs;

print color 'yellow';     

foreach (sort sorting keys %combe ) { 
    my $tmwrite = localtime ( $combe{$_} );
    printf "%25s\t %04d/%02d/%02d -%02d:%02d:%02d- \n",
        $_,
        $tmwrite->year + 1900, 
        $tmwrite->mon + 1, 
        $tmwrite->mday,
        $tmwrite->hour, 
        $tmwrite->min, 
        $tmwrite->sec;
}

print color 'reset';     
