# Project-LED
Get a working Raspberry Pi. 
#Date: 16/03/18
#Description: This code is designed to activate a Raspberry Pi's LEDs in a sequence.

import RPi.GPIO as GPIO  #Tells the python interpreter which library we will be using.

import time  #Imports the time library so we can freely start/pause our script.

GPIO.setmode(GPIO.BCM)  #Each pin on the Raspberry Pi has different names, so this tells the program which naming convention we would like to use.

GPIO.setwarnings(False) #Tells Python to not print out any warnings whislt the program is running.

GPIO.setup(18,GPIO.OUT) #Tells the interpreter that pin 18 is going to be used. We will now be able to turn it "On" and "Off" whenever we'd like.

print "LED on" #Outputs information into the terminal.

GPIO.output(18,GPIO.HIGH) #Turns the GPIO pin "On", which means that we're providing power to the pin.

Time.sleep(1) #Pauses our program for 1 second.

print "LED off" #Displays a print statement that says "LED off".

GPIO.output(18,GPIO.LOW)  #This now turns off the GPIO pin we we're using, which means power is no longer being supplied to it. 
