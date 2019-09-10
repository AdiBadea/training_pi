import csv
import numpy as np

# Functions ---

def getData(inputFile):

  data = []

  with open(inputFile) as fileData:
    csvReader = csv.reader(fileData, delimiter=',')
    for row in csvReader:
      data.append(row)
    del data[0]
  return data

def stringToInt(string):
    return int(string)

def findNextYear(input):
    yearContainer = []
    for date in input:
        yearContainer.append(date[0][6:10])
    years = list (set(yearContainer))
    years = list (map(stringToInt, years))
    lastYear = max(years)
    return lastYear

def buildDictionary(input):

    days = []
    dictionary = []

    for daysAndIncome in input:
        days.append(daysAndIncome[0][0:5])
    days = np.unique(days)

    for day in days:
        dictionary.append({"day": day, "incomes": []})

    for date in dictionary:
        for inputDate in input:
            if inputDate[0][0:5] == date["day"]:
                date["incomes"].append(inputDate[1])
    # print(dictionary)
    return dictionary



# Main program ---

data = getData("data.csv")
lastYear = findNextYear(data)
# dictionary = buildDictionary(data)

#test = "01.01.2017"

#print(test[6])

# print(yearSpan)
# print(data)

# print(data[0][0][0:5])
buildDictionary(data)

# [
#     {"zi": "01.01", "sume": [1000, 500, 700]}
# ]

#np.unique - ptr a obtine zilele
#dupa ce a mzilele, ma duc iara pe dates
#
