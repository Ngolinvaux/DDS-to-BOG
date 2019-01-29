import os
import shutil
import sys

bogHeader = "42 4F 47 20 31 2E 30 32 20 20 20 00 00 02 00 00 80 00 00 00 80 00 00 00 08 00 00 00 01 00 00 00 F0 55 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"


def DDStoBOG():
    with open(sys.argv[1]+'.bog', 'wb') as f:
        f.write(bytearray(int(i,16) for i in bogHeader.split(' ')))
        with open(sys.argv[1], 'rb') as f2:
            f.write(f2.read())
    input("Done. File is in source directory. Press a button to continue ")


def BOGtoDDS():
    shutil.copy(sys.argv[1],sys.argv[1]+'.dds')
    with open(sys.argv[1]+'.dds', 'rb') as f:
        f.seek(len(bogHeader.split(' ')))
        data = f.read()
    with open(sys.argv[1]+'.dds', 'wb') as f:
        f.write(data)
    input("Done. File is in source directory. Press a button to continue ")



if(sys.argv[1].endswith(".bog")):
    BOGtoDDS()


if(sys.argv[1].endswith(".dds")):
    DDStoBOG()


