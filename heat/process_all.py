import os
import sys
import matplotlib.pyplot as plt

file = open("out2.txt", "r")
lines = file.readlines()

split_files = []
indexes = []
temp = []
for i in range(len(lines)):
    if "Starting at Power level " in lines[i]:
        continue
    if "Temp:" in lines[i]:
        temp.append(float(lines[i].split(" ")[1].split("*")[0]))

plt.plot(temp)
plt.show()
plt.clf()
