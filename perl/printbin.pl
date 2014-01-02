#!/usr/bin/perl
#===============================================================================
#
#         FILE:  printbin.pm
#
#  DESCRIPTION:  print integer in binary format
#
#        FILES:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (Vladan Jovanovic), <vladan44@gmail.com>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  12-12-21 07:30:14 AM PST
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

sub printbin 
{
    my $x = shift;
    # print $x . "\n";
    for (my $i = 1 << 31, ; $i > 0; $i = $i >> 1) {
        if ($i & $x) {
            print "1";
        } else {
            print "0";
        }
    }
    print "\n";
}

# __main__
die "usage: $0 <integer>" if $#ARGV;
my $number = shift;
my $max = ~0;
die "Maximim 32 bit unsigned integer is: $max" if $number > $max;
printbin($number); 

