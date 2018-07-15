import RPi.GPIO as GPIO
import l293d

try: 
	motor1 = l293d.DC(22, 18, 16)
	motor2 = l293d.DC(15, 13, 7)
	GPIO.setmode(GPIO.BOARD)

	from evdev import InputDevice, categorize, ecodes

	# Use ls /dev/input to find the gamepad's event
	gamepad = InputDevice('/dev/input/event0')

	# Prints information about gamepad
	print(gamepad)

	# Might be useful to list the button codes here as variable
	aBtn = 289

	# Runs each time something happens
	for event in gamepad.read_loop():
		
		# Runs if we get a key pressed
		if event.type == ecodes.EV_KEY:
			print(event)
			
			# Runs if the key is PRESSED
			if event.value == 1:
				if event.code == aBtn:
					print("The A button was pressed")
					motor1.clockwise(speed=100)
					motor2.clockwise(speed=100)
				
				# Add some code here for the other buttons
				
			
			# Runs if ANY button is RELEASED
			elif event.value == 0:
				# Try making code to run if only a SPECIFIC button is released
				print("Button released")
				motor1.stop()
				motor2.stop()
				
		
		# Runs if the D-pad is used
		elif event.type == ecodes.EV_ABS:
			absevent = categorize(event)
			print(ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
			
			# Runs if the value of the x-position changes
			if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
				if absevent.event.value == 0:
					print("Left")
				
				# Write some code to run for other directions on the D-pad
				# See if you can write code to run when two directions are combined
			
			# Runs if the value of the x-position changes
			if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
				if absevent.event.value == 0:
					print("Up")
					
				# Write some code to run for other directions on the D-pad
				# See if you can write code to run when two directions are combined

except KeyboardInterrupt:
	l293d.cleanup()
	GPIO.cleanup()

