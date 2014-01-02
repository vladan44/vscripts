#!/bin/bash

svn status . | grep -v ^? | awk "{ print $2 }"

