# Learning Twilio with Bubu!

## What is Twilio?
Twilio is a cloud communications platform as a service company based in San Francisco, California. Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs.

## How to start?
The very first thing is to create a Twilio account, in the [official Twilio website](https://www.twilio.com), don’t worry, this is free and you only have to create the account and accept the terms and conditions.

The next step is get in Twilio console, then you could see one amazing button that says: 
“TwilioQuest” these place is one of the most comprehensible and the coolest tutorial you’d could see ever. But in this lecture we don’t going to discuss that, in fact, I’m going to take all these "started material" and going to explain to you how this works in a very simple way.

Explore the interface until you feel comfortable to continue. Well, let’s create our first program with Twrilio and Python!

## Twilio Installation using pip:
To install Twilio for Python we need to write: 
	pip install twilio
in the console.

Then we’ll be able to use all the APIs and resources that Twilio offer to us.

## You don't need to know Python
In this project I will to work with Python and I'll do the equivalent stuff without program anything too

## If you know Python this is what you need?
Twilio needs two credentials to work:

```python

account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"

```

Then, you just need to create a “Client” and you’re ready to go and explore all the cool stuff that Twilio has. 

### Send an SMS:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = Client(account_sid, auth_token)

message = client.messages.create(
	to = "+52" + os.environ.get('MY_PHONE_NUMBER'),
	from_ = "+1 719 425 4101",
	body = "Hello, this is my message from python") 

print(message.sid)
```

### Make a Call:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = Client(account_sid, auth_token)

call = client.calls.create(
	to = "+52" + os.environ.get('MY_PHONE_NUMBER'),
	from_ = "+1 719 425 4101",
	url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
```