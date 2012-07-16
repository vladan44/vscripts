# #!/usr/bin/perl -w
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

use charnames ':full';
print "\N{GREEK CAPITAL LETTER DELTA} is called delta.\n";

# import module
use Getopt::Long;
 
# read options
$result = GetOptions ("name=s" => $name);  
      

# print value
print "Input name is $name";

use charnames qw(cyrillic greek);
print "\N{Sigma} and \N{sigma} are Greek sigmas.\n";
print "\N{Be} and \N{be} are Cyrillic bes.\n";


