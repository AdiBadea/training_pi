dataFile = open("C:/Users/AdrianBadea/Projects/training_pi/opticalmed_extrapolation/data.csv", "r")

if dataFile.mode == "r":
    content = dataFile.read()
    print(content)    