import csv

data = []

income = []
dates = []

with open('C:/Users/AdrianBadea/Projects/training_pi/opticalmed_extrapolation/data.csv') as csvFile:
    
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