import RPi.GPIO as GPIO
import time

# Setam modul de numerotare al pinilor
GPIO.setmode(GPIO.BOARD)

# Setam ca pin-ul 7 sa emita curent
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)


for repetitions in range(0, 20):
    
    GPIO.output(10, False)
    GPIO.output(7, True)
    time.sleep(3)

    GPIO.output(8, True)
    GPIO.output(7, False)
    time.sleep(3)

    GPIO.output(10, True)
    GPIO.output(8, False)
    time.sleep(3)    
    
GPIO.cleanup()