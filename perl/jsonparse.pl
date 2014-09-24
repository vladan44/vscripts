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
use JSON;
 
my $in = 0;

sub print_object() {

    local $arg = \@_;
    # print "== $in\n";

    # check if decoded json is actually reference to embedded json object.
    # Synopsys of the function ref()

    # Returns a TRUE value if EXPR is a reference, FALSE otherwise. If EXPR
    # is not specified, $_ will be used. The value returned depends on the
    # type of thing the reference is a reference to. Builtin types include:
    #
    #    REF
    #    SCALAR
    #    ARRAY
    #    HASH
    #    CODE
    #    GLOB
    # 
    # example of usage
    #
    #    if (ref($decjsn{$key}) eq "HASH") {
    #        print " is a reference to a hash.\n";
    #    }
    #    if (!ref($decjsn{$key})) {
    #        print "is *not* a reference at all.\n";
    #    }

    local $kk = shift @{$arg};
    local $vv = shift @{$arg};
    local $uhhh = scalar @{$arg};
    $in++;
    if (!ref($vv)) {
        for $a (0..$in) { print "   "; }
        print "$kk =";
        print " $vv\n";
    } elsif (ref($vv) eq "HASH") {
        for $a (0..$in) { print "   "; }
        print "$kk = { \n";
        &print_object(%{$vv});
        for $a (0..$in) { print "   "; }
        print "}\n";
    } elsif (ref($vv) eq "ARRAY") {
        for $a (0..$in) { print "   "; }
        print "$kk = [ "; 
        foreach (@{$vv}) { 
            if (ref($_) eq "HASH") { 
                &print_object(%{$_});
            } else { 
                print "$_  "; 
            }
        } 
        print "]\n";
    } 

    $in--;
    &print_object(@{$arg}) if ($uhhh);
}

###############################################################################
# __main__

my $man = 0;
my $help = 0;

## Parse options and print usage if there is a syntax error,
## or if usage was explicitly requested.
GetOptions(
    help    => \$help,
    man     => \$man) or pod2usage(2);

pod2usage(1)             if $help;
pod2usage(-verbose => 2) if $man;

#
## if it's not connected to a terminal (otherwise print usage)
pod2usage("$0: No files given.")  if ((@ARGV == 0) && (-t STDIN));

my $filename = shift;

my $json;
{
	local $/; # enable slurp
	open my $fh, "<", $filename;
	$json = <$fh>;
	close $fh;
}

print "\n";
&print_object(%{decode_json($json)});
print "\n";

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



