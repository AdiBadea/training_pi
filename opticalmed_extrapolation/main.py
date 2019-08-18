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

# Main program ---

print(getData("data.csv"))