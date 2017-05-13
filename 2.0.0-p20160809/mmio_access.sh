#!/bin/sh
#
# Make a summary of MMIO access per function.
#
# Usage: ./make_mmio_access <directory_of_lsts>
#
# Generated table will be in mmio.txt
#

# This script requires https://github.com/pfalcon/ScratchABlock - either
# have it in PATH or uncomment and set path below.
#SABLOCK=~/projects/ScratchABlock/

set -e

DIR=$(dirname $0)

funcdir="funcs"

PYTHONPATH=. ${SABLOCK}apply_xform.py --script script_esp8266_mmio_access --format none $funcdir
${SABLOCK}funcdb_query.py $funcdir/funcdb.yaml --select "addr, label, mmio_refs" --where mmio_refs --sort >mmio.txt
${SABLOCK}funcdb_query.py $funcdir/funcdb.yaml --select "addr, label, mmio_refs" --where mmio_refs --sort --html >mmio.html
