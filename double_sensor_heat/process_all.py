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

# keep temperatures between 34 to 41.1
temp = [x for x in temp if x > 34 and x < 41.1]
temp2 = [x for x in temp2 if x > 34 and x < 41.1]

plt.plot(temp)
plt.plot(temp2)

# show x-axis as number of samples
plt.xlabel("Number of Samples")
# show y-axis as temperature
plt.ylabel("Temperature")

# increase resolution of y-axis
plt.yticks([x/10 for x in range(340, 412, 4)])

# increase size of plot to 4000x4000
plt.gcf().set_size_inches(40, 40)

# show which plot is of Temp and which is of Temp2
plt.legend(["Temp", "Non-contact Temp"])

# show points on plot
# plt.scatter([x for x in range(len(temp))], temp)
# plt.scatter([x for x in range(len(temp2))], temp2)

plt.title("Heat Plot")
plt.savefig("heat.png")
plt.show()
plt.clf()
