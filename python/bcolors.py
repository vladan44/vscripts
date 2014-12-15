#!/usr/bin/python


class bcolors:
    HEADER = "\033[38;05;%dm" % 5
    OKBLUE = "\033[38;05;%dm" % 4
    WARNING = "\033[38;05;%dm" % 3
    OKGREEN = "\033[38;05;%dm" % 2
    FAIL = "\033[38;05;%dm" % 1
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

