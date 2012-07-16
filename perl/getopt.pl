#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  getopt.pl
#
#        USAGE:  ./getopt.pl 
#
#  DESCRIPTION:  Illustration of GetOptions() usage
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  9/15/2006 2:39:13 PM Pacific Daylight Time
#     REVISION:  0.01 - not at the first checkpoint yet!
#===============================================================================

# use strict;
# use warnings;

# import module
use Getopt::Long;
use Pod::Usage;
 
my $man = 0;
my $help = 0;

## Parse options and print usage if there is a syntax error,
## or if usage was explicitly requested.
GetOptions(
    'help|?'    => \$help, 
    man         => \$man
    ) or pod2usage(2); 

pod2usage(1)             if $help;
pod2usage(-verbose => 2) if $man;


## if it's not connected to a terminal (otherwise print usage)
pod2usage("$0: No files given.")  if ((@ARGV == 0) && (-t STDIN));

# print value
print 'Input name is $name';

__END__

=head1 NAME

sample - Using GetOpt::Long and Pod::Usage

=head1 SYNOPSIS

sample [options] [file ...]

Options:
-help            brief help message
-man             full documentation

=head1 OPTIONS

=over 8

=item B<-help>

Print a brief help message and exits.

=item B<-man>

Prints the manual page and exits.

=back

=head1 DESCRIPTION

B<This program> will read the given input file(s) and do something
useful with the contents thereof.

=cut



