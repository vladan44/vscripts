#!/usr/bin/python

import fnmatch
import sys
import os

if len(sys.argv) != 3:
    sys.exit("usage: grpy <string> <filepattern>")


def mygrep(root, file_name, string):
    print os.path.join(root, file_name) + ": "
    os.system("grep -n " + string + " " + os.path.join(root, file_name))


def main():
    root_path = '.'
    string = sys.argv[1]
    file_pattern = sys.argv[2]

    for root, dirs, files in os.walk(root_path):
        for file_name in files:
            if fnmatch.fnmatch(file_name, file_pattern):
                mygrep(root, file_name, string)


if __name__ == "__main__":
    main()
