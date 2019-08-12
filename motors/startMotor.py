import RPi.GPIO as GPIO
import time

# Setam modul de numerotare al pinilor
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

    
#GPIO.output(13, False)
#GPIO.output(11, False)
#GPIO.output(15, False)
#GPIO.output(19, False)
    # Oprim pin-ul
    
  
    
#GPIO.cleanup()

# Setam ca pin-ul 7 sa emita curent
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

for repetitions in range(0, 5):
    
    GPIO.output(13, True)
    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(19, True)
  
    # Pornim pin-ul
    
    time.sleep(3)
    # Stam o secunda
    
    GPIO.output(13, False)
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(19, False)
    # Oprim pin-ul
    
    time.sleep(1)
    # Stam o secunda
    
GPIO.cleanup()
# Curatam configuratiile date mai sus