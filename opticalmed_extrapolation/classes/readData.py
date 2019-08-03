import csv 
# csv.reader(csvFile, delimiter=',')

class ReadData():
    def __init__(self, filePath):
        # setting variables
        # self.filePath = filePath

        self.openReadFile(filePath)

    def openReadFile(self, filePath):
        # self.filePath = filePath
        print(filePath)

ReadData("test/test")

