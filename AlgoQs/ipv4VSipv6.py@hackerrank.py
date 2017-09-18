import sys
import re
import string

pattern = "0[xX][0-9a-fA-F]+"
for lines in sys.stdin:
    lines = lines.strip()
    if lines.isdigit() :
        continue
    elif " " in lines:
        print("Neither")
    elif "." in lines:
        list = lines.split(".")
        if max([int(x) for x in list]) > 255 or min([int(x) for x in list])<0:
            print("Neither")
        else:
            print("IPv4")
    elif ":" in lines:
        list = lines.split(":")
        isheximal = True
        for l in list:
            if not all(c in string.hexdigits for c in l):
                isheximal = False
                break
        if isheximal == True:
            print("IPv6")
        else:
            print("Neither")
