#!/bin/bash

awk 'BEGIN{FS=":"; print "digraph{"}{split($4, a, ","); for (i in a) printf "\"%s\" [shape=box]\n\"%s\" -> \"%s\"\n", $1, a[i], $1}END{print "}"}' /etc/group|display

