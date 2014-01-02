#!/usr/bin/perl -w
#===========================================================================
#
#         FILE:  awkc.pl
#
#        USAGE:  ./awkc.pl 
#
#  DESCRIPTION:  sipmpifying awk usage
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  11-11-07 02:39:45 PM PST
#     REVISION:  ---
#===========================================================================

# use strict;
# use warnings;

# import module
use Getopt::Long;
use Pod::Usage;
 
# default separator
my $sep = ' ';
my $help = '';


## Parse options and print usage if there is a syntax error,
## or if usage was explicitly requested.
GetOptions(
    'separator|s|fs=s'    => \$sep,
    'help|h'    => \$help
    );

pod2usage(-verbose => 1) if $help;

# perserve number of other arguments
my $num = $#ARGV;
my @rest;

# shift all command line arguments
# save only numbers
for my $i (0..$num) {
    $rest[$i] = shift @ARGV;
    die "column numbers should be integer numbers" if $rest[$i] !~ /^\d+$/;
}

while(<>) {
    chomp;
    unless ($_ =~ /^\s*$/) {
        my @toks = split /$sep+/, $_;
        for my $i (@rest) {
            print "$toks[$i]\t" if $toks[$i];
        }
        print "\n";
    }
}

__END__

=head1 NAME

awkc - shortened version of awk for command line usage

=head1 SYNOPSIS

command | awkc [options] num1 num2 num3...

=head1 OPTIONS

Options:
--separator|s           separator

=head1 DESCRIPTION

B<This program> will read the given input file(s) and do something
useful with the contents thereof.

=cut

