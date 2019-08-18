import csv        

def getData(inputFile):
  with open(inputFile) as fileData:
    csvReader = csv.reader(fileData, delimiter=',')
    for row in csvReader:
      print(row)
     
getData("data.csv")