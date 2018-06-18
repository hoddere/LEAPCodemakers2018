import RPi.GPIO as GPIO
import l293d
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)

leftMotor = l293d.DC(22, 18, 16)
rightMotor = l293d.DC(15,13,7)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)

def SetAngle(angle):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	duty = angle / 18 + 2
        GPIO.output(11, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(11, False)

response = sys.argv[1]
print(sys.argv)

if response == "01":
	leftMotor.clockwise(speed=100, wait=True)
	rightMotor.clockwise(speed=100, wait=True)
	sleep(600)

if response == "02":
	leftMotor.anticlockwise(speed=100, wait=True)
	rightMotor.anticlockwise(speed=100, wait=True)
	sleep(600)

if response == "03":
       	leftMotor.clockwise(speed=20, wait=True)
	rightMotor.clockwise(speed=100, wait=True)
	sleep(600)
if response == "04":
	leftMotor.clockwise(speed=100, wait=True)
	rightMotor.clockwise(speed=20, wait=True)
	sleep(600)
if response == "05":
	sleep(0.1)
	l293d.cleanup()
	GPIO.cleanup()

if response == "06":
	pass


