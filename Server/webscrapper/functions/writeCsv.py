import csv
import os.path

# outputFolder = "C:/Users/AdrianBadea/Projects/training_pi/Server/webscrapper/webscrappers/ouput"
outputFolder = "C:/Users/AdrianBadea/GoogleDrive/Webscrapper_output"
fileName = "webscrape_history.csv"
completeName = os.path.join(outputFolder, fileName)

def writeCsv(input):
    print(input)
    with open(completeName, mode="a+", newline='') as csv_file:
        fieldnames = ["Data", "Comerciant", "Produs", "Pret"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({"Data": input["scrapeDate"], "Comerciant": input["seller"], "Produs": input["title"], "Pret": input["price"]})