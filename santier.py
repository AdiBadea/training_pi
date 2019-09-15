import RPi.GPIO as GPIO
import time

#Dezzactivez avertizarile
GPIO.setwarnings(False)

# Setam modul de numerotare al pinilor
GPIO.setmode(GPIO.BOARD)

# Setam ca pin-ul 7 sa emita curent
GPIO.setup(7, GPIO.OUT)


for repetitions in range(0, 10):
    
    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)

    
GPIO.cleanup()