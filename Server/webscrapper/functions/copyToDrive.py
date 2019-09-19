from shutil import copy
import os.path

fileName = "webscrape_history.csv"

sourceFolder = "C:/Users/AdrianBadea/Projects/training_pi/Server/webscrapper/webscrappers/ouput"
completeName = os.path.join(sourceFolder, fileName)

copyFolder = "C:/Users/AdrianBadea/Google Drive/Webscrapper_output"
copyCompleteName = os.path.join(copyFolder, fileName)

print(completeName)
print(copyCompleteName)


def copyToDrive():
    copy(completeName, copyFolder)
