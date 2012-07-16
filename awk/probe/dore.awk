#!/usr/bin/awk -f

BEGIN { }
      { 
          if( $0 ~ "~" )  
            { print $0 ; }
      }
