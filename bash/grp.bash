#!/bin/bash

# better alternative:
find . -regex '.*\.\(h\|cp?p?\|qml\|js\)' | xargs grep --color=tty $*

