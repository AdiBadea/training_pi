import csv

# Functions ---

def getData(inputFile):

  data = []

  with open(inputFile) as fileData:
    csvReader = csv.reader(fileData, delimiter=',')
    for row in csvReader:
      data.append(row)
    del data[0]
  return data

def getYearSpan(input):
    years = []
    for date in input:
        years.append(date[0][6:10])
    yearSpan = list (set (years))
    return yearSpan

# Main program ---

data = getData("data.csv")
yearSpan = getYearSpan(data)

#test = "01.01.2017"

#print(test[6])

print(yearSpan)
print(data)

print(data[0][0][0:5])

# [
#     {"zi": "01.01", "sume": [1000, 500, 700]}
# ]

#np.unique - ptr a obtine zilele
#dupa ce a mzilele, ma duc iara pe dates
#
