#!/usr/bin/perl

@myfiles = ( );

while( <> ) { foreach $file (@myfiles) { print $_ if $_ =~ $file; } }
