import csv 
# csv.reader(csvFile, delimiter=',')

class GetData():
    def __init__(self, filePath):
    
        self.data = self.readFile(filePath)

    def __repr__(self):

        return self.data


    def readFile(self, filePath):

        container = []

        with open(filePath) as csvFile:

            rawData = csv.reader(csvFile, delimiter=',')
            rowIndex = 0
    
            for row in rawData:
                container.append([row[0], row[1]])
                rowIndex += 1
            del container[0]

        return container

