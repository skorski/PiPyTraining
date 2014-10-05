import RPi.GPIO as GPIO
import time

GPIO.cleanup

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

status = raw_input("Do you want to turn it on? (Y/N): ")

if status == "Y":
	print "Turning On"
	GPIO.output(23,True)
	#time.sleep(5)

if status == "N":
	print "Turning Off"
	GPIO.output(23,False)
	#time.sleep(5)

GPIO.cleanup
