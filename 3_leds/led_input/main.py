# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
import time

# GPIO.setup(7, GPIO.OUT)  # verde  - 1 
# GPIO.setup(8, GPIO.OUT)  # galben - 2
# GPIO.setup(10, GPIO.OUT) # rosu   - 3

numereLeduri  = ["1", "2", "3"]

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def intrabaLed():
        print("Ce bec doresti sa aprinzi?")
        print("1 - Verde | 2 - Galben | 3 - Rosu")
        becDeAprins = input()
        if becDeAprins not in numereLeduri:
            raise ValueError("Bec invalid, becurile disponibile sunt 1, 2 sau 3")
        else:
            clear() 
            return int(becDeAprins, 10)
           

def intrabaSecunde():
        print("Pentru cate secunde ?")
        secundeDeAprins = input()
        print(type(secundeDeAprins))
        if isinstance(int(secundeDeAprins, 10), int) == False:
            raise ValueError("Valoarea introdusa nu este un numar")
        elif int(secundeDeAprins, 10) > 30:
            raise ValueError("Maximul de secunde pentru care poti aprinde un bec este de 30")
        else:
            clear() 
            return int(secundeDeAprins, 10) 

def delay(secunde):
  countdown = secunde
  while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
    clear()

def aprindeBec(bec, secunde):
    print("Se va aprinde becul:", bec, "pentru", secunde, "secunde")
    if bec == 1:
        print("becul verde aprins")
        time.sleep(secunde)    
        print("becul verde stins")
    elif bec == 2:
        print("becul galben aprins")
        time.sleep(secunde)  
        print("becul galben stins")
    elif bec == 3:
        print("becul rosu aprins")
        time.sleep(secunde)    
        print("becul galben stins")


class Main:
    def __init__(self):
        while True:
            try:
                # print("Se va aprinde becul:", intrabaLed(), "pentru", intrabaSecunde(), "secunde")
                aprindeBec(intrabaLed(), intrabaSecunde())
                break
            except BaseException as errorMessage:
                clear()
                print (errorMessage)
                print("-------------------------------------------------------------------------")

Main()



    

