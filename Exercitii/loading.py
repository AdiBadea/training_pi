# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 


percent = 90
# loading = None
result = None

i = 0
while i < percent:
    result = "=" * i
    print ("[", result, "|", i,"%"," ", "]" )
    sleep(0.4) 
    system('cls') 
    i = i + 1 #increment i

