#!/bin/python3


from flask import Flask

app = Flask(__name__)
"""
 __name__ is a flask function that tells 
Flask that everything needed to run the app is here
"""

@app.route("/")
# tells that "app" is right here, hence the "/"

def index():
    return "Drink more coffee Right Now!"

app.run(host="0.0.0.0", port=80)
# run flask on our host at this specific port
