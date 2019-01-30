import os
import shutil
import sys

bogHeader = "42 4F 47 20 31 2E 30 32 20 20 20 00 00 02 00 00 80 00 00 00 80 00 00 00 08 00 00 00 01 00 00 00 F0 55 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"


def DDStoBOG(x):
    with open(sys.argv[x][:-4]+'.bog', 'wb') as f:
        f.write(bytearray(int(i,16) for i in bogHeader.split(' ')))
        with open(sys.argv[x], 'rb') as f2:
            f.write(f2.read())


def BOGtoDDS(x):
    with open(sys.argv[x], 'rb') as f:
        f.seek(len(bogHeader.split(' ')))
        byt = f.read(1)
        form = '.dds'
        if(byt == b'D'):
            form = '.dds'
        elif(byt == b'\x89'):
            form = '.png'    
    shutil.copy(sys.argv[x],sys.argv[x][:-4]+form)
    with open(sys.argv[x][:-4]+form, 'rb') as f:
        f.seek(len(bogHeader.split(' ')))
        data = f.read()
    with open(sys.argv[x][:-4]+form, 'wb') as f:
        f.write(data)


for i in range(1,len(sys.argv)):
    if(sys.argv[i].endswith(".bog")):
        BOGtoDDS(i)


    if(sys.argv[i].endswith(".dds") or sys.argv[i].endswith(".png") ):
        DDStoBOG(i)


input("Done. File is in source directory. Press a button to continue ")
