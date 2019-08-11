from twilio.rest import Client
import os

# La SID de tu cuenta de Twilio, o "Identificador de Seguridad"
# The SID of your Twilio account or "Security Identifier"
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')

# Tu "Ficha de autor" de Twilio
# Your Auth Token from twilio.com/console
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

#Creating our message
message = "Whatever you want, baby"


#To work with the APIs you need this two things
client = Client(account_sid, auth_token)

client.messages.create(
	to = "+52" + os.environ.get('MY_PHONE_NUMBER'),
	from_ = "+1 719 425 4101",
	body = message
	) 