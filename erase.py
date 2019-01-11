#!/usr/bin/env python

##
# Because TI compiler puts source file name -- which is random --
# into symbol table, we need to erase it, to make more reproducible
# output binary. 
#
# Once, TI Expert said it is frustrating [1], so maybe this script will
# bring happiness to the world. :-)
#
# Anyway that temporary file does not exist afterwards, so this erasing seems
# to be relatively harmless.
#
# [1] https://e2e.ti.com/support/tools/ccs/f/81/p/682645/2514688#2514688
##

import re, subprocess, sys

ERASE_CHARACTER = b'0'

if len(sys.argv) != 2:
    print("Usage: erase.py FILE")
    sys.exit(1)

file_to_erase = sys.argv[1]

readelf = subprocess.check_output(['readelf', '-s', file_to_erase], stderr=subprocess.PIPE)
tmpvar = re.search(b'FILE\s+LOCAL\s+HIDDEN\s+ABS\s+(\S+)', readelf)
string_to_erase = tmpvar.group(1)

with open(file_to_erase, 'r+b') as fh:
    file_content = fh.read()

    for match in re.finditer(b'/tmp/%s:(?:[^:]+:){2}(\d+)' % string_to_erase, file_content):
        offset_to_erase = match.start(1)

        timestamp_to_erase = match.group(1)
        fh.seek(offset_to_erase)
        fh.write(ERASE_CHARACTER * len(timestamp_to_erase))

    for match in re.finditer(string_to_erase, file_content):
        offset_to_erase = match.start()
        fh.seek(offset_to_erase)
        fh.write(ERASE_CHARACTER * len(string_to_erase))

