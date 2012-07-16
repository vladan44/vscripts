#!/usr/bin/python

import sys
import time
import progressbar



if __name__ == '__main__':
    p = progressbar.AnimatedProgressBar(end=100, width=80)

    while True:
        p + 1
        p.show_progress()
        time.sleep(0.01)
        if p.progress == 100:
            break
    print #new line

