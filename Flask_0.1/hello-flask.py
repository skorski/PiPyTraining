from flask import Flask
app = Flask(__name__) #this creates a flask object called app

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)