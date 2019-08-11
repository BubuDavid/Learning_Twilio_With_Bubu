#Importing library
from flask import Flask
from flask import render_template
from twilio.rest import Client
import os

#Creating our app variable.
app = Flask(__name__)

#Functions
@app.route('/')
def home():
	return render_template('Home.html')

@app.route('/SMS/')
def sms():
	
	#Sending the message
	account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
	auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	to = "+52" + os.environ.get('MY_PHONE_NUMBER'),
	from_ = "+1 719 425 4101",
	body = "Help me! I'm in danger")


	return render_template('Home.html')


#run method
if __name__ == '__main__':
	app.run(debug = True)