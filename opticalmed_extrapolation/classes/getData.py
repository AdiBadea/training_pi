import csv 
# csv.reader(csvFile, delimiter=',')

class GetData():
    def __init__(self, filePath):

        self.readFile(filePath)

    def readFile(self, filePath):

        data = []

        with open(filePath) as csvFile:

            print(csvFile)

            rawData = csv.reader(csvFile, delimiter=',')
            rowIndex = 0

            for row in rawData:
                data.append([row[0], row[1]])
                rowIndex += 1
                del data[0]

            print(data)

GetData('C:/Proiecte/training_pi/opticalmed_extrapolation/data.csv')

