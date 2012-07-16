#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  newestFile.pl
#
#        USAGE:  ./newestFile.pl 
#
#  DESCRIPTION:  globs through directories and finds the newest file
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  1/21/2007 10:20:48 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

# use strict;
# use warnings;

use Cwd;
use File::Find;
use Time::localtime;

my $usage = "usage: newestFile [directory]" ;

die $usage unless $#ARGV == 0 or $#ARGV == -1;

my $dir = $#ARGV == 0 ? $ARGV[0] : getcwd;

my $newestfile;
my $newesttime = 0;

sub process_file
{
    unless ( -d $_ )
    {
        my $time = (stat($_))[9];

        if ( $time > $newesttime )
        {
            $dir = getcwd;
            $newestfile = $_;
            $newesttime = $time;
        }
    }
}

chdir $dir or die $usage;


my @directories = glob("*");
find (\&process_file, @directories);
 

my $tmwrite = localtime ( $newesttime );

die "no file" if $newesttime == 0 ; 

printf "%s \t %04d/%02d/%02d -%02d:%02d:%02d- %s \n",
    $newestfile,
    $tmwrite->year + 1900, 
    $tmwrite->mon + 1, 
    $tmwrite->mday,
    $tmwrite->hour, 
    $tmwrite->min, 
    $tmwrite->sec,
    $dir;
