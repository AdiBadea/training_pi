import csv

writeData =[
    ["Data", "Venit (pe zi)"],
    ["01.01.2018", 1000],
    ["02.01.2018",900]
]

csv.register_dialect(
    'csvConfig',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True
)

with open('write.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='csvConfig')
    for row in writeData:
        writer.writerow(row)

f.close()