import RPi.GPIO as GPIO
import time

GPIO.cleanup
GPIO.setmode(GPIO.BCM)

print ("\n\n This will controll two LED's on opposite PWM duty cycles\n\n")

inputPin = 17
outputPinGreen = 23
outputPinRed = 18


if(False):
	inputPin = int(raw_input("What pin has the button?"))
	outputPinGreen = int(raw_input("What pin has the Green LED?"))
	outputPinRed = int(raw_input("What pin has the Red LED?"))



GPIO.setup(inputPin,GPIO.IN)
GPIO.setup(outputPinGreen,GPIO.OUT)
GPIO.setup(outputPinRed,GPIO.OUT)

ledLightGreen = GPIO.PWM(outputPinGreen, 50)
ledLightGreen.start(0)

ledLightRed = GPIO.PWM(outputPinRed, 50)
ledLightRed.start(0)

ledLightGreen.ChangeDutyCycle(90)
ledLightRed.ChangeDutyCycle(90)


print ("\n\n This will controll two LED's on opposite PWM duty cycles\n\n")

inputMultiple = raw_input("What multiple would you like to use?")

multiple = int(inputMultiple)

input=GPIO.input(inputPin)
i=0

while True:
	input=GPIO.input(inputPin)
	if input:
		i+=1 #if it is pressed, make it brighter
	else: #if not, dimm it
		i-=1

	i = max(0,min(i,100/multiple))

	#print i

	CDC = max(0,min(i*multiple,99))
	ledLightGreen.ChangeDutyCycle(CDC)
	ledLightRed.ChangeDutyCycle((100-CDC))

	time.sleep(0.02)

GPIO.cleanup