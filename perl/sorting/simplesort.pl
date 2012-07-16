#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  simplesort.pl
#
#        USAGE:  ./simplesort.pl 
#
#  DESCRIPTION: sorting function: sort { $a <=> $b } @unsorted
#               
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  Also, illustrates usage of Tk for dialog boxes
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  1/21/2007 4:17:40 PM Pacific Standard Time
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

use Tk;
use Tk::DialogBox;

die "usage: perl simplesrot.pl" unless $#ARGV == -1 ;

my $main = MainWindow->new();
$main->optionAdd('*BorderWidth' => 2);

$main->Button(
    -text => "Enter an array", 
    -command => \&register
)->pack( -side => "left");

$main->Button(
    -text =>"    Quit        ", 
    -command=> sub {exit} 
)->pack(-side=>"left");

my $dialog = $main->DialogBox ( 
    -title => "SimpleSort",
    -buttons => [ "OK", "NOK" ] 
);

$dialog->add ("Label", -text => "Unesi niz brojeva")->pack();
my $entry = $dialog->add("Entry", -width=>35)->pack();

MainLoop;

sub register 
{
    my $button = $dialog->Show;

    if ($button eq "OK" )
    {
        my $array = $entry->get;
        sortiraj($array);
    }
    else
    { 
        print "onononono!";
        exit;
    }

}


sub sortiraj
{
    my $niz = shift;
    my @unsorted = split " ", $niz;

    # Nota - alfabetsko sortiranje bi bilo ovako:
    # my @sorted = sort { $a cmp $b } @unsorted;

    my @sorted = sort { $a <=> $b } @unsorted;

    foreach my $sort (@sorted) { print "$sort "; }

    exit;
}

