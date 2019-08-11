from twilio.rest import Client
import os

def send_SMS(account_sid, auth_token):
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	to = "+52" + os.environ.get('MY_PHONE_NUMBER'),
	from_ = "+1 719 425 4101",
	body = "Hello, Excuse me, I'm in danger")

def make_call(account_sid, auth_token):
	pass