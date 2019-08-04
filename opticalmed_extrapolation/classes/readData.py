import csv 
# csv.reader(csvFile, delimiter=',')

class ReadData():
    def __init__(self, filePath):

        self.openReadFile(filePath)

    def openReadFile(self, filePath):

        data = []

        with open(filePath) as csvFile:


            rawData = csv.reader(csvFile, delimiter=',')
            rowCount = 0

            for row in rawData:
                data.append([row[0], row[1]])
                rowCount += 1
                del data[0]

            print(filePath)
            print(data)

ReadData('C:/Proiecte/training_pi/opticalmed_extrapolation/data.csv')

