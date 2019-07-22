import csv

data = []

income = []
dates = []

with open('C:/Users/AdrianBadea/Projects/training_pi/opticalmed_extrapolation/data.csv') as csvFile:
    rawData = csv.reader(csvFile, delimiter=',')
    rowCount = 0
    for row in rawData:
        # print(row[0] + " - " + row[1])
        data.append([row[0], row[1]])
        rowCount += 1
    print(data) 

    #     if lineCount == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')