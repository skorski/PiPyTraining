import RPi.GPIO as GPIO
import time

GPIO.cleanup

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)
GPIO.setup(23,GPIO.OUT)

ledLight = GPIO.PWM(23, 50)
ledLight.start(0)

inputMultiple = raw_input("What multiple would you like to use?")

multiple = int(inputMultiple)

input=GPIO.input(17)
i=0

while True:
	previnput = input
	input=GPIO.input(17)
	if input:
		i+=1 #if it is pressed, make it brighter
	else: #if not, dimm it
		i-=1

	i = max(0,min(i,100/multiple))

	#print i

	CDC = max(0,min(i*multiple,99))
	ledLight.ChangeDutyCycle(CDC)

	time.sleep(0.02)

GPIO.cleanup