#!/bin/sh

# diff is called by git with 7 parameters:
# path old-file old-hex old-mode new-file new-hex new-mode

mybc3=`which bcompare`
$mybc3 "$2" "$5" | cat

# trailing cat ensures constant return code, which might be problem in some 
# cases
