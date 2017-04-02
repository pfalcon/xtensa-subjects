#!/bin/sh
#
# This script requires exported functions to be in funcs/. Temporarily
# uncomment a line in proj_init.py to export such functions.
#

# This script requires https://github.com/pfalcon/ScratchABlock - either
# have it in PATH or uncomment and set path below.
#SABLOCK=~/projects/ScratchABlock/

${SABLOCK}make_callgraph.sh funcs/ --group _ignore_=callgraph_runtime.txt
