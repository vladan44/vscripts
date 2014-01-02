#!/bin/bash

svn status . | grep  -E -v ^\? | awk '{ print $2 }' | xargs tar zcvf $1.tar.gz

