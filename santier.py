import RPi.GPIO as GPIO
import time

GPIO.setwarnings(false)

# Setam modul de numerotare al pinilor
GPIO.setmode(GPIO.BOARD)

# Setam ca pin-ul 7 sa emita curent
GPIO.setup(3, GPIO.OUT)


for repetitions in range(0, 10):
    
    GPIO.output(3, True)
    time.sleep(2)
    GPIO.output(3, False)
 
    
GPIO.cleanup()