#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  permtry.pl
#
#        USAGE:  ./permtry.pl 
#
#  DESCRIPTION:  Illustration of permutation
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  12/1/2013 7:18:23 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

use Algorithm::Permute;
use List::Permutor;

sub get_perms {
    my @list = shift;
    my @ret = ();
    my $perms = new Algorithm::Permute(@list, 2 );
    while (my @res = $perms->next) {
        push(@ret, join("", @res));
    }
    return @ret
}

sub new_perms {
    my $perm = List::Permutor->new( 0, 1, 2);
    while ( my @p = $perm->next() ) {
        print "@p\n";
    }
}

sub main {
    my @list = ('a', 'b', 'c');
    my @pres = get_perms(\@list);

    for my $p (@pres) {
        print $p . "\n";
    }

    new_perms();
}

exit main(@ARGV);

