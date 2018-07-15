# Imports modules to let us use l293d (motor chip)
import RPi.GPIO as GPIO
import l293d

GPIO.setmode(GPIO.BCM)

# These are the pins we use to control the motors.
motor1 = l293d.DC(22, 18, 16)
motor2 = l293d.DC(15, 13, 7)

# These run the motors clockwise
motor1.clockwise()
motor2.clockwise()

# How can we make the motors go at a certain speed?
# Try to make the motors go counterclockwise
# Hint: What's another word for counterclockwise?

input("Press enter to terminate.")

# Frees up GPIO pins used by l293d
l293d.cleanup()
GPIO.cleanup()
