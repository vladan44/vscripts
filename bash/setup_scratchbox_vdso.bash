#!/bin/bash

## scratchbox is incopatible with vdso linux kernel feature
## this script disables the feature by modifying vdso_enabled file
## under /proc tree i.e. disebles it at the runtime

## this needs to be done everytime when running scratchbox, permanent disabling
## is going to be hanled separately

echo 0 | sudo tee /proc/sys/vm/vdso_enabled

