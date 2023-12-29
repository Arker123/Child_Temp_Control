import os
import sys
import matplotlib.pyplot as plt

# open all files in split folder
for filename in os.listdir("split"):
    print("Processing " + filename)
    file = open("split/" + filename, "r")
    lines = file.readlines()

    # find all lines with "Starting at Power level"
    indexes = []
    temp = []
    for i in range(len(lines)):
        if "Starting at Power level " in lines[i]:
            continue

        # Extract temp from "Temp: 24.1250*C"
        if "Temp:" in lines[i]:
            temp.append(float(lines[i].split(" ")[1].split("*")[0]))

    plt.plot(temp)
    plt.savefig("plots/" + filename.split(".")[0] + ".png")
    plt.clf()

    