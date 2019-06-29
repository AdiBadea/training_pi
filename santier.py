# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
import time

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

s = 3

def delay(secunde):
  countdown = secunde
  while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
    clear() 
   


delay(s)