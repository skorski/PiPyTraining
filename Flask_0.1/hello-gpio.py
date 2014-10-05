from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%m-%d %H:%M:%S")
	templateData = {
		'title' : 'Hello!',
		'time' : timeString,
		'other' : 'route / '
		}
	return render_template('main2.html', **templateData)

@app.route("/readPin/<pin>")
def readpin(pin):
	try:
		GPIO.setup(int(pin), GPIO.IN)
		if(GPIO.input(int(pin)) == True):
			response = "Pin number " + pin + " is pressed."
		else:
			response = "Pin number " + pin + " is NOT pressed."
	except Exception, e:
		response = "There was an error reading pin " + pin +"."

	templateData = {
		'title' : 'Status of pin ' + pin,
		'response' : response,
		'other' : 'Pin app route'
		}

	return render_template('pin.html', **templateData)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)