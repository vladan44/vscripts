#!/usr/bin/python
###############################################################################
# backup script
#

import os
import time
import sys
import getopt
from socket import gethostname


osystem = sys.platform

###############################################################################
# global settins
# : source_dirs_files - list of files and directories to be backed up
# The files and directories to be backed up
# are dependant on os type
#
if osystem[:3] == 'win':
    source_dirs_files = [
            'C:\\vim\\vimfiles',
            'C:\\vim\\_vimrc',
            'C:\\vim\\_gvimrc',
            'C:\\myutils',
            'C:\\dijara',
            'C:\\workspace\gen',
            ]

    # backup E: drive workspace if it exist
    if os.path.exists("E:\\"): source_dirs_files.append('E:\\workspace\\gen')

    zip_command = '7z a %s %s'
    target_dir = 'C:\\backups\\'
    extention = '.Z'

else:
    source_dirs_files = [
            '~/.bashrc',
            '~/.mybashrc',
            '~/scripts',
            '~/.vimrc',
            '~/.gvimrc',
            '~/.vim',
            '~/.emacs',
            '~/.emacs.d',
            '~/dijara',
            '~/Documents',
            '~/workspace/gen'
            ]

    zip_command = 'tar czvf %s %s'
    target_dir = '/opt/backups/'
    extention = '.tar.gz'

today = target_dir + time.strftime('%Y%m%d')
hostname = gethostname()
filename = hostname + '_' + time.strftime('%H%M%S')
dirs = ' '.join(source_dirs_files)

###############################################################################
# usage function
#
def usage():
    sys.exit("Usage: " + sys.argv[0] + """ [ options ]

        Cross-platform script for backing up important data. Depends on tar on
        unix and on 7z on windows.

        available options:
            -h --help               show this message
            -c --comment            Adds comment to the backup filename

        Backup file is:
        %s<date>%s<hostname_current_timestamp>[_comment].Z

        List of files and directories to be backed up:
        %s
        """  % (target_dir, os.sep, dirs))

###############################################################################
# add comment to backup filename
# Take a comment from the user to create the name of the zip file
#
def add_comment():
    comment = raw_input('Enter a comment --> ')
    return today + os.sep + filename + '_' +\
            comment.replace(' ', '_') + extention


###############################################################################
# main
#
def main():

    # command lines option handlers:
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                "hc:", ["help", "comment"])

    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        if opt in ("-c", "--comment"):
            keyword = arg
            target = add_comment()

    # create target path if it does not exist
    if not os.path.exists(today): os.makedirs(today, 0700)


    # absolut target filename
    if not 'target' in locals():
        target = today + os.sep + filename + extention

    # assemble complete command
    command = zip_command % (target, dirs)

    # actual backup
    if os.system(command) == 0: print 'Successful backup to', target
    else: print 'Backup FAILED'


if __name__ == "__main__":
    main()

