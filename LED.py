
import RPi.GPIO
import time

LED = ["Red", "Pink", "Green", "Purple"]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(18,GPIO.OUT)
    GPIO.setwarnings(false)
    
print ("LED On!")

def led():
    while True:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
def destroy():
    GPIO.output(LED,GPIO.LOW)
    GPIO.cleanup()
    
setup()
try:
    led()
except KeyboardInterrput:
    CTRL+C
    else:
        Destroy()
    

   
    
   
