#!/usr/bin/perl
###############################################################################

use strict;
use warnings;

sub usage {
	return <<"";
Usage: 
    $0 <strings>\n
    <strings> is array of strings to be passed to google search.\n
    This script depends on presence of w3m browser\n

}

###############################################################################
### main

my $qs;
my $which;
my $pipe = "which w3m |";
my $googlesearch = "http://www.google.com/search?q=";

die usage() if $#ARGV < 0;
die "'which' is not installed"  unless open W, $pipe;
while (<W>){
    $which = $_; chomp $which;
}
die "'w3m'   is not installed"  unless close W;

my $i = 0;
for my $argv (@ARGV) { 
    $qs .= $argv.'+' if $i++ < $#ARGV; 
}
$qs .= $ARGV[$#ARGV];

system($which." ".$googlesearch.$qs);

