#!/usr/bin/python

for a in range(0,256):
		COLOR = "\033[38;05;%dm" % a
		print COLOR + str(a) + " PYTHON Color Pallete" 
