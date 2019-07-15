from twilio.rest import Client

# La SID de tu cuenta de Twilio, o "Identificador de Seguridad"
# The SID of your Twilio account or "Security Identifier"
account_sid = my_Account_SID

# Tu "Ficha de autor" de Twilio
# Your Auth Token from twilio.com/console
auth_token = my_account_token

#To work with the APIs you need this two things
client = Client(account_sid, auth_token)

message = client.messages.create(
	to = my_phone_number,
	from_ = phone_number_bought,
	body = "Hello, this is my message from python") 

print(message.sid)
print("OMG I did it!")