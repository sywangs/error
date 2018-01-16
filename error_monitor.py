#! /usr/bin/python

import time
import os
import commands as cm
import sys

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

while 1:
	command = "/usr/bin/python2.7" + " " + cur_file_dir() + "/error_run.py"
	print command
	os.system(command)
	time.sleep(10)
