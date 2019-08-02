import csv

writeData =[
    ["Data", "Venit (pe zi)"],
    ["01.01.2018", 1000],
    ["02.01.2018",900]
]

class writeOutput:
    def __init__(self, outputData):
        self.outputData = outputData
        self.writeFile(outputData)

    def writeFile(self, data):

        self.csv.register_dialect(
            'csvConfig',
            quoting=csv.QUOTE_ALL,  
            skipinitialspace=True
        )
        self.writer = csv.writer(f, dialect='csvConfig')

        for row in self.outputData:
            print(row)

writeOutput(writeData)
