#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  color.pl
#
#        USAGE:  ./color.pl 
#
#  DESCRIPTION:  Illustration of color printing in perl
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  11-10-30 05:46:05 PM PDT
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;


use Term::ANSIColor;          

print color 'bold blue';     
print "This text is bold blue.\n";     
print color 'reset';                  
print "This text is normal.\n";      
print colored ("Yellow on magenta.\n", 'yellow on_magenta');  
print "This text is normal.\n";                              
print colored ['yellow on_magenta'], "Yellow on magenta.\n"; 

use Term::ANSIColor qw(uncolor);  
print uncolor, "";

use Term::ANSIColor qw(:constants);
print BOLD, BLUE, "This text is in bold blue.\n", RESET;

use Term::ANSIColor qw(:constants);

$Term::ANSIColor::AUTORESET = 1;
print BOLD BLUE "This text is in bold blue.\n";
print "This text is normal.\n";

