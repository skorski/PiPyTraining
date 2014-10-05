import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)

input=GPIO.input(17)
i=0

while True:
	input = GPIO.input(17)
	print("Status " + str(input))
	time.sleep(1)


while True:
	previnput = input
	input=GPIO.input(17)
	if ((not previnput) and input):
		print("Buton Pressed " + str(i) + " times.")
		print("Status" + str(input))
		i+=1
	previnput = input
	time.sleep(0.05)