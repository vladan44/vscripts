#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  complement.pl
#
#        USAGE:  ./complement.pl 
#
#  DESCRIPTION:  testing complemnt of the language
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  12/1/2013 2:33:08 AM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;
use Algorithm::Permute;

sub get_strings {
    my @a = ();
    my @ab = ('a', 'b');
    my $len = shift;

    for my $i (1..$len) {
        my $s = "";
        for my $i (1..$len) {
            for my $b (@ab) {
                $s = $s.$b;
            }
        }
        push(@a ,$s);
    }

    return @a;
}

sub main {
    my $rega = 'a|ba+';

    my @str = get_strings(5);

    for my $pr (@str) {
        print $pr . " ";
    }
}

exit main(@ARGV);

