#!/usr/bin/python
###############################################################################
# \file vregex.py
#
# \brief regex library collection.

import re

###############################################################################
# Function: bool is_cfile( string )
#
# \fn bool is_cfile( string )
#
# \brief check filename if it conventionally named C or C++ source file
# 
# \param filename to be checked
# 
# \retval  true if pattern matches, false otherwise
#
def is_cfile( filename ):
    c_regex = '\w+\.(([Cc](pp)?)|[Hh]|(inl))$'
    return does_it_match( filename, c_regex )


###############################################################################
# Function: bool is_cfile( string )
#
# \fn bool is_cfile( string )
#
# \brief check filename if it conventionally named JavaScript or QML source file
# 
# \param filename to be checked
# 
# \retval  true if pattern matches, false otherwise
#
def is_jsfile( filename ):
    js_regex = '\w+\.(([Jj][Ss])|([Qq][Mm][Ll]))$'
    return does_it_match( filename, js_regex )

###############################################################################
# Function: bool is_httpurl( url )
#
# \fn bool is_httpurl( url )
#
# \brief check url if it matches http regular expression. Regex has been taken 
#        from www.regexlib.com. Url has to start with http in order to be 
#        matched
# 
# \param url to be checked
# 
# \retval  true if pattern matches, false otherwise
#
def is_httpurl( url ):
    http_regex = 'https?:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
    return does_it_match( url, http_regex )


###############################################################################
# Function: bool does_it_match( string )
#
# \fn bool does_it_match( string )
#
# \brief generinc regex check function
#
# \param string to be checked
# \param regular expression 
#
# \retval  true if pattern matches, false otherwise
#
def does_it_match( string, regex ):
    pattern = re.compile( regex )
    if pattern.match( string ): return True
    else: return False



