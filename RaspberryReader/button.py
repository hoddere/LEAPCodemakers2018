import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	# Gets the input state of the button
	input_state = GPIO.input(18)
	
	if input_state == False:
		# Button is pressed when current blocked between pin and ground
		print("Button Pressed")
		time.sleep(0.2)
		
		# Integrate with the Raspberry Reader
		# Try to implement code to do something when button pressed
		# multiple times.
		
