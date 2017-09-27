import twilio
print(twilio.__version__)

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8bb23196ab7ed56130e358e60cfc6c06"
# Your Auth Token from twilio.com/console
auth_token  = "d26ba82dc1b4ccba47b01b9275b2d316"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917002041687",
    from_="+15182820633",
    body="I'm the best in the world")

print(message.sid)
