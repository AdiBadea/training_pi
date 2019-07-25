#mile = km * c, unde c este constanta

#Informatii ghid:
	# 0km = 0 mile
	# 100 km = 62.137 mile
	
#eroare = adevar - calcul


mile = 0
error = 0 

def convertToMiles(km, constant):
	mile = km * constant
	print("numarul de mile este: ", mile)
	calculateError(62.137, mile)

def calculateError(truth, result):
	error = truth - result
	print("Eroare este de: ", error)

convertToMiles(100, 0.61)



