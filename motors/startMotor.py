import RPi.GPIO as GPIO
import time

# Setam modul de numerotare al pinilor
GPIO.setmode(GPIO.BOARD)

# Setam ca pin-ul 7 sa emita curent
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


for repetitions in range(0, 5):
    
    GPIO.output(7, True)
    GPIO.output(11, True)

  
    # Pornim pin-ul
    
    time.sleep(3)
    # Stam o secunda
    
    GPIO.output(7, False)
    GPIO.output(11, False)
    # Oprim pin-ul
    
    time.sleep(1)
    # Stam o secunda
    
GPIO.cleanup()
# Curatam configuratiile date mai sus
