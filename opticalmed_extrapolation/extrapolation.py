import csv
import matplotlib.pyplot as plt

# data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}


realData = {}


data = []

income = []
dates = []

with open('C:/Users/Roberta/Documents/Adrian/Proiecte/training_pi/opticalmed_extrapolation/data.csv') as csvFile:
    
    rawData = csv.reader(csvFile, delimiter=',')
    rowCount = 0

    for row in rawData:
        data.append([row[0], row[1]])
        rowCount += 1
    del data[0]

    for row in data:
        dates.append(row[0])
        income.append(row[1])
    # print(income)
    # print(dates)

i = 0
while i < len(dates):
    realData[dates[i]] = income[i]
    i += 1

incomes = list(realData.keys())
dates2 = list(realData.values())

# fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
plt.plot(incomes, dates2)
# fig.suptitle('Categorical Plotting')

plt.show()

# print(realData)