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
use Config qw( %Config );

sub printbin 
{
    my ($num, $size) = @_;
    for (my $i = 1 << $size ; $i > 0; $i = $i >> 1) {
        print $i & $num ? '1' : '0';
    }
    print "\n";
}

# __main__
die "usage: $0 <integer>" if $#ARGV;
my $number = shift;
my $max = ~0;
my $len = $Config{ivsize} * 8;
die "Maximim $len bit unsigned integer is: $max" if $number > $max;

printbin($number, $len - 1);

