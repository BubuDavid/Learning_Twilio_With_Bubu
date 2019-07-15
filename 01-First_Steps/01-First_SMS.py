from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa74ae815adb448751e79554f2f64e4c8"

# Your Auth Token from twilio.com/console
auth_token = "5ea7e1589b6142a1c96f4ed075ebccc9"

client = Client(account_sid, auth_token)

message = client.messages.create(
	to = "+524774027085",
	from_ = "+17194254101",
	body = "Hello, this is my message from python") 

print(message.sid)
print("OMG I did it!")