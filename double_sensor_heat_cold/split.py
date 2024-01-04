import os
import sys

file = open("out2.txt", "r")
lines = file.readlines()

split_files = []
indexes = []
for i in range(len(lines)):
    if "Starting at Power level " in lines[i]:
        print("Found split at line " + str(i))
        indexes.append(i)

'''
# find difference between indexes -> all 1669 lines
diff = []
for i in range(len(indexes)):
    if i == len(indexes) - 1:
        break
    diff.append(indexes[i+1] - indexes[i])

print(diff)
'''

for i in range(len(indexes)):
    if i == len(indexes) - 1:
        split_files.append(lines[indexes[i]:])
        break
    split_files.append(lines[indexes[i]:indexes[i+1]])

for i in range(len(split_files)):
    file = open("split/out" + str(i) + ".txt", "w")
    file.writelines(split_files[i])
    file.close()