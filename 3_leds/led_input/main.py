# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 

numereLeduri = ["1", "2", "3"]

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
            return becDeAprins
           

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
            return secundeDeAprins      

class AprindeBec:
    def __init__(self):
        while True:
            try:
                # intrabaLed()
                # intrabaSecunde()
                print("Se va aprinde becul:", intrabaLed(), "pentru", intrabaSecunde(), "secunde")
                break
            except BaseException as errorMessage:
                clear()
                print (errorMessage)
                print("-------------------------------------------------------------------------")

                # break
        # if intrabaLed() != "eroare":
        #     print(intrabaLed())
        #     print(intrabaSecunde())

AprindeBec()



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age




    

