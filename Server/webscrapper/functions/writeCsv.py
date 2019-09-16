import csv

def writeCsv(input):
    print(input)
    with open("webscrape_history.csv", mode="a+", newline='') as csv_file:
        fieldnames = ["Data", "Comerciant", "Produs", "Pret"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({"Data": input["scrapeDate"], "Comerciant": input["seller"], "Produs": input["title"], "Pret": input["price"]})