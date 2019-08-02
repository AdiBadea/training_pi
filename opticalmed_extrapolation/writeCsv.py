import csv

# writeData =[
#     "Data",
#     "Venit (pe zi)",
#     "01.01.2018",
#     1000,
#     "02.01.2018",
#     900,
#     "03.01.2018",
#     450
# ]

person = [
    ['SN', 'Person', 'DOB'],
    ['1', 'John', '18/1/1997'],
    ['2', 'Marie','19/2/1998'],
    ['3', 'Simon','20/3/1999'],
    ['4', 'Erik', '21/4/2000'],
    ['5', 'Ana', '22/5/2001']
]

csv.register_dialect('myDialect',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)

# with open('write.csv', 'w') as f:
with open('write.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)

f.close()