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

## What you need?
Twilio needs two credentials to work:

```python

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"

```

### Send an SMS:

```python
from twilio.rest import Client

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)

message = client.messages.create(to="+12316851234", from_="+15555555555",
                                 body="Hello there!")
```

### Make a Call:

```python
from twilio.rest import Client

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
```