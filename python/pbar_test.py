#!/usr/bin/python

import sys
import time
import progressbar

def main():
    p = progressbar.AnimatedProgressBar(end=100, width=80)

    while True:
        p + 1
        p.show_progress()
        time.sleep(0.03)
        if p.progress == 100:
            break
    print #new line

if __name__ == '__main__':
    main()

