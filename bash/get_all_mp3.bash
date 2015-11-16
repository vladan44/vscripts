#!/bin/bash

# echo Getting mp3\'s from: $1
wget -r -l1 -H -nd -A mp3 -e robots=off $1
