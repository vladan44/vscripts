#!/usr/bin/awk -f
BEGIN { FS = ":"; }
{ 
    i = 0;  
    while( i++ < NF ) 
    { 
        print "path element:", $i ; 
    } 
}

