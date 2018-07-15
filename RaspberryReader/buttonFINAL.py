import RPi.GPIO as GPIO
import time
import os
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	# Gets the input state of the button
	input_state = GPIO.input(18)
	
	if input_state == False:
		# Button is pressed when current blocked between pin and ground
		print("Button Pressed")
		time.sleep(0.2)
		
		# Start a timer
		start = time.time()
		presses = 1
		
		while True:
			# Get new button presses
			input_state = GPIO.input(18)
			if input_state == False:
				print("Button Pressed Again")
				presses += 1
			
			# Keep getting new button presses for 3 seconds	
			if time.time() > start + 3:
				 break
				 
			time.sleep(0.2)
				 
		print("Total presses: " + str(presses))
		
		# If button pressed once, run reader
		if presses == 1:
			os.system("./reader.sh Codemakers")
		
		# If button pressed twice, give weather forecast
		if presses == 2:
			location = weather.lookup_by_location('Hamilton, ON')
			condition = location.condition
			os.system("python3 speech.py 'Currently in Hamilton it is " + condition.temp + " degrees celsius and " + condition.text + "'" )
		exit()
		

