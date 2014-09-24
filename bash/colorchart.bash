#!/bin/bash

for c in {0..255} ; do
    echo -e "\e[38;05;${c}m ${c} Bash Prompt Color Chart" 
done
