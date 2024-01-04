import sys
import os

# open the file
f = open("received.log", "r")

# remove empty lines
lines = f.readlines()
lines = [l for l in lines if l.strip()]

for line in lines:
    # remove the newline character
    line = line.strip()
    print(line)

# close the file
f.close()