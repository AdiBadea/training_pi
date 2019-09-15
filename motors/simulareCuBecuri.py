##########################################
# Programul acesta are ca scop reglarea motoarelor folosind becuri.
# Becurile Rosii = Motor Stang
#Becurile Verzi = Motor Drept
##########################################

import RPi.GPIO as GPIO
import time

#Dezzactivez avertizarile
GPIO.setwarnings(False)

# Setam modul de numerotare al pinilor
GPIO.setmode(GPIO.BOARD)

#Becuri verzi = Motor Drept
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

#Becuri Rosii = Motor Stang
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

for repetitions in range(0, 10):
    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    time.sleep(1)

    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(1)
    
GPIO.cleanup()