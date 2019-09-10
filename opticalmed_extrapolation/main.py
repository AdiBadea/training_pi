import csv
import numpy as np

# Functions ---

def stringToInt(string):
    return int(string)

def getData(inputFile):

  data = []

  with open(inputFile) as fileData:
    csvReader = csv.reader(fileData, delimiter=',')
    for row in csvReader:
      data.append(row)
    del data[0]
  return data

def buildDictionary(input):

    days = []
    incomeHistory = []

    for daysAndIncome in input:
        days.append(daysAndIncome[0][0:5])
    days = np.unique(days)

    for day in days:
        incomeHistory.append({"day": day, "incomes": []})

    for date in incomeHistory:
        for inputDate in input:
            if inputDate[0][0:5] == date["day"]:
                date["incomes"].append(inputDate[1])
    return incomeHistory

def findLastYear(input):
    yearContainer = []
    for date in input:
        yearContainer.append(date[0][6:10])
    years = list (set(yearContainer))
    years = list (map(stringToInt, years))
    lastYear = max(years)
    return lastYear

def calculateNextYearIncome(incomeHistory):
    nextYearIncome = []
    for dayIncomes in incomeHistory:

        incomes = dayIncomes["incomes"]
        incomes = list (map(stringToInt, incomes))

        dayIncome = sum(incomes) / len(incomes)
        dayIncomeToInt = int(dayIncome)
        nextYearDayIncome = str( dayIncomeToInt )

        dayIncomes["incomes"] = nextYearDayIncome
        #Schimb numele cheii
        dayIncomes["income"] = dayIncomes.pop("incomes")
        nextYearIncome.append(dayIncomes)
    print(nextYearIncome)
    return nextYearIncome


# Main program ---

data = getData("data.csv")
nextYear = findLastYear(data) + 1
incomeHistory = buildDictionary(data)
nextYearIncome = calculateNextYearIncome(incomeHistory)


# [
#     {"zi": "01.01", "sume": [1000, 500, 700]}
# ]

#np.unique - ptr a obtine zilele
#dupa ce a mzilele, ma duc iara pe dates
#
