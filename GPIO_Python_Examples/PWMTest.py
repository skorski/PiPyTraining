import RPi.GPIO as GPIO
import time

GPIO.cleanup

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, True)
time.sleep(10)
GPIO.output(23,False)


GPIO.cleanup

ledLight = GPIO.PWM(23, 50)
ledLight.start(0)

try:
  while True:
    for i in range (100):
      ledLight.ChangeDutyCycle(i)
      print i
      time.sleep(0.02)         #These last three lines are going to loop and increase the power from 1% to 100% gradually
    for i in range(100):
      ledLight.ChangeDutyCycle(100-i)
      time.sleep(0.02)         #These three lines loop and decrease the power from 100%-1% gradually
except KeyboardInterrupt:
  pass 

ledLight.stop()
GPIO.cleanup()
