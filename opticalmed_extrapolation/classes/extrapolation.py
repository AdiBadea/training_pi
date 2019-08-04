import csv
# import matplotlib.pyplot as plt
# import numpy as np

realData = {}


data = []

income = []
dates = []

# with open('C:/Users/Roberta/Documents/Adrian/Proiecte/training_pi/opticalmed_extrapolation/data.csv') as csvFile:
with open('C:/Proiecte/training_pi/opticalmed_extrapolation/data.csv') as csvFile:


    rawData = csv.reader(csvFile, delimiter=',')
    rowCount = 0

    for row in rawData:
        data.append([row[0], row[1]])
        rowCount += 1
    del data[0]

    for row in data:
        dates.append(row[0])
        income.append(row[1])
    print(income)
    print(dates)

# i = 0
# while i < len(dates):
#     realData[dates[i]] = income[i]
#     i += 1

# xCoords = list(realData.keys())
# yCoords = list(map(int,realData.values()))

# plt.plot(xCoords, yCoords)

# plt.show()