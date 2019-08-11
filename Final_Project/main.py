#Importing library
from flask import Flask
from flask import render_template
import Twilio
import os

#Creating our app variable.
app = Flask(__name__)

#Functions
@app.route('/')
def home():
	return render_template('Home.html')

@app.route('/SMS/')
@app.route('/SMS')
def sms():

	sid = os.environ.get('TWILIO_ACCOUNT_SID')
	token = os.environ.get('TWILIO_AUTH_TOKEN')
	
	#Twilio.send_SMS(sid, token)

	return render_template('SMS.html')


#run method
if __name__ == '__main__':
	app.run(debug = True)