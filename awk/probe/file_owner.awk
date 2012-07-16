#!/usr/bin/awk -f

BEGIN { print "File\t\tOwner" }
      { print $8, "\t", $3}
