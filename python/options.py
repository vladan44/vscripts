#!/usr/bin/python

import optparse

def main():
    p = optparse.OptionParser()
    p.add_option( "-f", "--file", default="filename", help="write to file",
                 metavar="FILE" )
    options, arguments  = p.parse_args()
    print "File is %s" % options.file

if __name__ == '__main__':
    main()



