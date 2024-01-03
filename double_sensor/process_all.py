import os
import sys
import matplotlib.pyplot as plt

file = open("out2.txt", "r")
lines = file.readlines()

split_files = []
indexes = []
temp = []
temp2 = []
for i in range(len(lines)):
    if "Starting at Power level " in lines[i]:
        continue
    if "Temp:" in lines[i]:
        temp.append(float(lines[i].split(" ")[1].split("*")[0]))
    if "Temp2:" in lines[i]:
        temp2.append(float(lines[i].split(" ")[1].split("*")[0]))

plt.plot(temp)
plt.plot(temp2)

# show which plot is of Temp and which is of Temp2
plt.legend(["Temp", "Non-contact Temp"])

plt.title("Heat Plot")
plt.savefig("heat.png")
plt.show()
plt.clf()
